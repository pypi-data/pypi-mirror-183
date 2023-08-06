import re
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date
from enum import Enum
from re import Match, Pattern
from typing import NamedTuple, Type, Union

from citation_date import decode_date, docket_date
from citation_docket import (
    Num,
    ac_key,
    ac_phrases,
    am_key,
    am_phrases,
    bm_key,
    bm_phrases,
    cull_extra,
    formerly,
    gr_key,
    gr_phrases,
    l_key,
    pp,
)
from citation_report import REPORT_REGEX, Publisher, Report

from .clean import gr_prefix_clean

DOCKET_DATE_FORMAT = "%b. %d, %Y"


@dataclass
class Docket:
    """
    This abstract class is instantiated later in the process, specifically after a docket `Style` is constructed.

    This cannot be a Pydantic BaseModel because both Docket and Report use a `match` field which is not supported by Pydantic.

    Because of various formatting possibilities, limiting the serial id seems like a better approach.

    So from the raw `ids`, get the `cleaned_ids`, and of these `cleaned_ids`, extract the `@first_id` found to deal with compound ids, e.g. ids separated by 'and' and ','
    """

    match: Match
    short_category: str | None = None
    category: str | None = None
    context: str | None = None
    ids: str | None = None
    cleaned_ids: str | None = None
    docket_date: date | None = None

    def __post_init__(self):
        self.cleaned_ids = self.ids.strip("()[] .,;") if self.ids else None
        self.serial_text = self.first_id or self.cleaned_ids
        if self.serial_text:
            if adjust := gr_prefix_clean(self.serial_text):
                self.serial_text = adjust

    @property
    def first_id(self):
        """Get the first element from a list of separators when possible."""

        def first_exists(char, text):
            return text.split(char)[0] if char in text else None

        if self.cleaned_ids:
            for char in [",", ";", " and ", " AND ", "&"]:
                if res := first_exists(char, self.cleaned_ids):
                    return res
            return self.cleaned_ids
        return None

    @property
    def formatted_date(self):
        if self.docket_date:
            return self.docket_date.strftime(DOCKET_DATE_FORMAT)
        return None

    def __str__(self) -> str:
        if self.serial_text:
            return f"{self.short_category} {self.serial_text}, {self.formatted_date}"
        return "No proper string detected."


@dataclass
class ModelGR(Docket, Report):
    ...


@dataclass
class ModelAM(Docket, Report):
    ...


@dataclass
class ModelAC(Docket, Report):
    ...


@dataclass
class ModelBM(Docket, Report):
    ...


CitationType = Union[
    type[ModelGR], type[ModelAM], type[ModelAC], type[ModelBM], type[Report]
]  # note Report


class DocketModelConstructor(NamedTuple):
    """Docket `dataclass` later populated from data like regex `group names`. Each enum `Style` will allow this constructor to be populated."""

    label: str  # e.g. "General Register", "Administrative Matter"
    short_category: str  # e.g. G.R., A.M.
    group_name: str  # e.g. "gr_phrase", "am_phrase"; see .regexes for details
    init_name: str  # e.g. "gr_mid", "am_init"; see .regexes for details
    docket_regex: str  # this is the docket's regex string is supplemented by date, "formerly", etc.
    key_regex: str  # used for culling `ids` of the docket
    num_regex: str  # "No." used for culling the `ids` of the docket
    model: CitationType  # dataclass model to make, see `CitationType` options


class Style(Enum):
    """
    1. Limited to Docket style members: "GR", "AM", "AC" and "BM"
    2. In order to reference the `value` attributes of member in properties, must use this format: `member.value.attribute`
    3. Each `enum` member has search / match / construct patterns based on `namedtuple` properties (includes a `dataclass` field.)
    4. Each of the members is used in a filtering function `get_docketed_reports()` to determine if a given text matches the member patterns.
    5. If a match is found, a `dataclass`, e.g. "ModelGR", is instantiated with fields supplied by `regex` group names.
    6. Each of the Docket style members may contain an optional `Report` regex pattern, see `pattern` property.
    """

    GR = DocketModelConstructor(
        label="General Register",
        short_category="GR",
        group_name="gr_phrase",
        init_name="gr_mid",
        docket_regex=gr_phrases,
        key_regex=rf"{gr_key}({l_key})?",
        num_regex=Num.GR.allowed,
        model=ModelGR,
    )

    AM = DocketModelConstructor(
        label="Administrative Matter",
        short_category="AM",
        group_name="am_phrase",
        init_name="am_init",
        docket_regex=am_phrases,
        key_regex=am_key,
        num_regex=Num.AM.allowed,
        model=ModelAM,
    )

    AC = DocketModelConstructor(
        label="Administrative Case",
        short_category="AC",
        group_name="ac_phrase",
        init_name="ac_init",
        docket_regex=ac_phrases,
        key_regex=ac_key,
        num_regex=Num.AC.allowed,
        model=ModelAC,
    )

    BM = DocketModelConstructor(
        label="Bar Matter",
        short_category="BM",
        group_name="bm_phrase",
        init_name="bm_init",
        docket_regex=bm_phrases,
        key_regex=bm_key,
        num_regex=Num.BM.allowed,
        model=ModelBM,
    )

    @property
    def pattern(self) -> Pattern:
        """Construct pattern from `docket_regex`"""
        docket = rf"{self.value.docket_regex}"
        dated = rf"(?P<extra_phrase>{formerly}?{pp}?){docket_date}"
        report = rf"(?P<opt_report>\,\s*{REPORT_REGEX})?"
        return re.compile("".join([docket, dated, report]), re.I | re.X)

    def find(self, text: str) -> Match | None:
        """Get first match of member's `pattern` on `text`"""
        return self.pattern.search(text)

    def find_all(self, text: str) -> Iterator[Match]:
        """Get all matches of member's `pattern` on `text`"""
        return self.pattern.finditer(text)

    def cleaned(self, text) -> str:
        """Remove category name from `text`"""
        regex = rf"""{self.value.key_regex}({self.value.num_regex})?"""
        sans_category: Pattern = re.compile(regex, re.I | re.X)
        return sans_category.sub("", text)

    def dockets_made(self, raw: str) -> Iterator[CitationType]:
        """If `self.pattern` matches `raw` text, create a `CitationType` (with possible Report)"""
        for match in self.find_all(raw):
            if match.group(self.value.init_name):
                yield self.value.model(
                    match=match,
                    short_category=self.value.short_category,
                    category=self.value.label,
                    context=(x := match.group(self.value.group_name)),
                    ids=cull_extra(self.cleaned(x.strip(", "))),
                    docket_date=decode_date(match.group("docket_date"), True),
                    publisher=Publisher.get_label(match),
                    volpubpage=match.group("volpubpage"),
                    volume=match.group("volume"),
                    page=match.group("page"),
                )

    @classmethod
    def extract(cls, raw: str) -> Iterator[CitationType]:
        """For each `Style`, create connected `CitationType`s if possible, e.g. `Style.GR` enables the `ModelGR`.

        Args:
            raw_text (str): The text to search for `CitationType` patterns, see `ModelGR`, `ModelAM`, `ModelAC`, `ModelBM`

        Yields:
            Iterator[CitationType]: `Docket` models, i.e. `Style.GR.model`,  which may contain an associated `Report`.
        """
        for styled in cls:
            yield from styled.dockets_made(raw)

import re
from dataclasses import dataclass
from datetime import date
from re import Match, Pattern

from dateutil.parser import parse

from .base import day, month, year
from .base.report import report_date_regex
from .base.us_uk import docket_date_regex

separator = r"[,\.\s]*"

uk = rf"""
(
    (?P<uk_day>{day})
    {separator}
    (?P<uk_month>{month})
    {separator}
    (?P<uk_year>{year})
)
"""

us = rf"""
(
    (?P<us_month>{month})
    {separator}
    (?P<us_day>{day})
    {separator}
    (?P<us_year>{year})
)
"""

POSSIBLE_DATE: Pattern = re.compile(rf"{us}|{uk}", re.I | re.X)


@dataclass
class DatedText:
    "Uses custom regex for matching date-like objects to deal with common typos in citations."

    raw: str
    match: Match | None = None
    text: str | None = None
    dated: date | None = None

    def __post_init__(self):
        self.match = m if (m := self.matches_pattern(self.raw)) else None
        self.text = self.US or self.UK if self.match else None
        self.as_date = self.maker(self.text) if self.text else None

    @classmethod
    def matches_pattern(cls, raw: str) -> Match | None:
        return match if (match := POSSIBLE_DATE.search(raw)) else None

    @classmethod
    def maker(cls, raw: str) -> date | None:
        try:
            return parse(raw).date()
        except Exception:
            ...
        return None

    @property
    def US(self) -> str | None:
        if self.match and self.match.group("us_day"):
            day = self.match.group("us_day")
            month = self.match.group("us_month")
            year = self.match.group("us_year")
            return f"{month} {day}, {year}"
        return None

    @property
    def UK(self) -> str | None:
        if self.match and self.match.group("uk_day"):
            day = self.match.group("uk_day")
            month = self.match.group("uk_month")
            year = self.match.group("uk_year")
            return f"{month} {day}, {year}"
        return None

    @property
    def as_string(self) -> str | None:
        return self.as_date.strftime("%B %d, %Y") if self.as_date else None


report_date = report_date_regex
docket_date = docket_date_regex


def decode_date(text: str, is_output_date_object: bool = False):
    obj = DatedText(text)
    return obj.as_date if is_output_date_object else obj.as_string

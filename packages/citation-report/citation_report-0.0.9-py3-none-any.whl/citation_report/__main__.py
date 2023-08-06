import datetime
from dataclasses import dataclass
from re import Match

from dateutil.parser import parse

from .publisher import Publisher
from .regex import REPORT_PATTERN


@dataclass
class Report:
    """Based on a `Match` object with pre-defined regex group names,
    Extract groups into respective fields.
    """

    match: Match
    publisher: str | None = None
    volpubpage: str | None = None
    volume: str | None = None
    page: str | None = None
    report_date: datetime.date | None = None

    def __post_init__(self):
        self.publisher = Publisher.get_label(self.match)
        self.volpubpage = self.match.group("volpubpage")
        self.volume = self.match.group("volume")
        self.page = self.match.group("page")
        self.report_date = self.convert_date_from_match(self.match)

    def __str__(self) -> str:
        return self.formal_report

    @property
    def formal_report(self):
        return f"{self.volume} {self.publisher} {self.page}"

    @property
    def phil(self):
        if self.publisher == Publisher.PHIL.value.label:
            return self.formal_report
        return None

    @property
    def scra(self):
        if self.publisher == Publisher.SCRA.value.label:
            return self.formal_report
        return None

    @property
    def offg(self):
        if self.publisher == Publisher.OFFG.value.label:
            return self.formal_report
        return None

    def convert_date_from_match(self, match: Match) -> datetime.date | None:
        if text := match.group("report_date"):
            try:
                return parse(text).date()
            except Exception:
                ...
        return None

    @classmethod
    def extract(cls, text: str):
        for match in REPORT_PATTERN.finditer(text):
            yield Report(match)

    @classmethod
    def extract_from_dict(cls, data: dict, report_type: str):
        """
        Assuming a dictionary with any of the following report_type keys
        `scra`, `phil` or `offg`, get the value of the Report property.
        >>> Report.extract_from_dict({"scra": "14 SCRA 314"}, "scra")
        '14 SCRA 314'
        """
        if report_type.lower() in ["scra", "phil", "offg"]:
            if candidate := data.get(report_type):
                try:
                    obj = next(cls.extract(candidate))
                    # will get the @property of the Report with the same name
                    if hasattr(obj, report_type):
                        return obj.__getattribute__(report_type)
                except StopIteration:
                    return None
        return None

    @classmethod
    def get_unique(cls, text: str) -> list[str]:
        """Will only get `Report` volpubpages (string) from the text"""
        reports = [r.volpubpage for r in cls.extract(text) if r.volpubpage]
        return list(set(reports))

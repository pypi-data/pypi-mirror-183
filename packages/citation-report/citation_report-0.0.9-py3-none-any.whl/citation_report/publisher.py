import re
from enum import Enum
from re import Match, Pattern
from typing import NamedTuple

separator = r"[\.,\s]*"

phil_regex = rf"""(?P<PHIL_PUB>
    phil
    {separator}
    (rep)?
    {separator} # 4 Phil. Rep., 545
)"""
scra_regex = r"(?P<SCRA_PUB>SCRA)"
offg_regex = rf"""(?P<OG_PUB>
                (
                    (
                        o
                        {separator}
                        g
                        {separator}
                    )|
                    (
                        off
                        {separator}
                        gaz(ette)?
                        {separator}
                    )
                )
                (
                    (
                        suppl? # Supp. vs. Suppl.; 47 Off. Gaz. Suppl. 12
                        {separator}
                    )|
                    (
                        \(? # 56 OG (No. 4) 1068
                        no # 49 O.G. No. 7, 2740 (1953),
                        {separator} # 46 O.G. No. 11, 90
                        \d{{1,4}}  # note enclosing brackets
                        \)?
                        {separator}
                    )
                )?
            )
        """


class PublisherStyle(NamedTuple):
    label: str
    description: str
    group_name: str
    regex_exp: str


class Publisher(Enum):
    PHIL = PublisherStyle(
        label="Phil.",
        description="Philippine Reports",
        group_name="PHIL_PUB",
        regex_exp=phil_regex,
    )
    SCRA = PublisherStyle(
        label="SCRA",
        description="Supreme Court Reports Annotated",
        group_name="SCRA_PUB",
        regex_exp=scra_regex,
    )
    OFFG = PublisherStyle(
        label="O.G.",
        description="Official Gazette",
        group_name="OG_PUB",
        regex_exp=offg_regex,
    )

    @property
    def pattern(self) -> Pattern:
        return re.compile(self.value.regex_exp, re.I | re.X)

    @classmethod
    def regex_options(cls) -> str:
        return rf"""
            (?P<publisher>
                {cls.SCRA.value.regex_exp}| # contains SCRA_PUB group name
                {cls.PHIL.value.regex_exp}| # contains PHIL_PUB group name
                {cls.OFFG.value.regex_exp} # contains OG_PUB group name
            )
        """

    @classmethod
    def all_patterns(cls) -> Pattern:
        return re.compile(cls.regex_options(), re.X | re.I)

    @classmethod
    def get_label(cls, match: Match):
        for _, m in cls.__members__.items():
            if match.group(m.value.group_name):
                return m.value.label

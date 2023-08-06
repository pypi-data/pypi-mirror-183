import re
from re import Pattern

from citation_date import report_date

from .publisher import Publisher

volume = r"""
    \b
    (?P<volume>
        [12]? # makes possible from 1000 to 2999
        \d{1,3}
        (
            \-A| # See Central Bank v. CA, 159-A Phil. 21, 34 (1975);
            a
        )?
    )
    \b
"""

page = r"""
    \b
    (?P<page>
        [12345]? # makes possible from 1000 to 5999
        \d{1,3}  # 49 Off. Gazette 4857
    )
    \b
"""

volpubpage = rf"""
    (?P<volpubpage>
        {volume}
        \s+
        {Publisher.regex_options()}
        \s+
        {page}
    )
"""

filler = r"""
    (?P<filler>
        [\d\-\.]{1,10}
    )
"""

extra = rf"""
    (?:
        (?:
            [\,\s,\-]*
            {filler}
        )?
        [\,\s]*
        {report_date}
    )?
"""

REPORT_REGEX = rf"{volpubpage}{extra}"

REPORT_PATTERN: Pattern = re.compile(REPORT_REGEX, re.X | re.I)

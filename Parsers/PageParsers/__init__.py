from Parsers.PageParsers.alter_page_parser import AlterYearlyAnnouncement


from datetime import datetime


class YearlyAnnouncement:
    def __init__(self, _from, to):
        if not to:
            to = datetime.now().year

        if to < _from:
            raise ValueError

        self.period = range(_from, to+1)
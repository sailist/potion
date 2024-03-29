from datetime import datetime


def strftime(fmt='%y-%m-%d-%H%M%S', dateobj: datetime = None) -> str:
    """get current date with formatted"""
    if dateobj is not None:
        return dateobj.strftime(fmt)
    return datetime.now().strftime(fmt)


def parse_notion_date(datestr, fmt='%Y-%m-%dT%H:%M:%S.%fZ') -> datetime:
    return datetime.strptime(datestr, fmt)

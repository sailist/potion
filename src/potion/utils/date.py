from datetime import datetime


def strftime(fmt='%y-%m-%d-%H%M%S', dateobj: datetime = None):
    """get current date with formatted"""
    if dateobj is not None:
        return dateobj.strftime(fmt)
    return datetime.now().strftime(fmt)

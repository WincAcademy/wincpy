"""
See:
https://github.com/carpedm20/emoji/blob/master/emoji/unicode_codes.py
"""


class icon:
    thumbsup = u'\U0001F44D '
    thumbsdown = u'\U0001F44E '


class color:
    """
    Format:
        '\033[38;2;<R>;<G>;<B>m '
    """

    winc_blue = '\033[38;2;74;144;226m'
    red = '\033[38;2;212;36;33m'
    green = '\033[38;2;46;220;104m'
    gray = '\033[38;2;152;164;174m'
    end = '\033[m'


class layout:
    class divider:
        width = 50
        level_1 = '=' * width
        level_2 = '-' * width

    list_item = '├───'


class misc:
    logo = """\t\t\t
    █░█░█ █ █▄░█ █▀▀ █▀█ █▄█\n\
    ▀▄▀▄▀ █ █░▀█ █▄▄ █▀▀ ░█░\n"""

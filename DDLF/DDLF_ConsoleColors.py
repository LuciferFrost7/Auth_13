class SettingsParameters:
    END = '\033[0m'
    BOLD = '\033[01m'
    OFF = '\033[02m'  # take of some setting parametrs
    UNDERLINE = '\033[04m'
    STRIKETHROUGH = '\033[09m'
    REVERSE = '\033[07m'  # reverse bg and fg
    LIST = [END, BOLD, OFF, UNDERLINE, STRIKETHROUGH, REVERSE]

class ForeGroundColors:
    END = '\033[0m'
    BLACK = '\033[30m'
    DARKGREY = '\033[90m'
    LIGHTGREY = '\033[37m'
    LIGHTRED = '\033[91m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    ORANGE = '\033[33m'
    LIGHTGREEN = '\033[92m'
    GREEN = '\033[32m'
    LIGHTCYAN = '\033[96m'
    CYAN = '\033[36m'
    BLUE = '\033[34m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    PURPLE = '\033[35m'
    LIST = [BLACK, DARKGREY, LIGHTGREY, LIGHTRED, RED, YELLOW, ORANGE, LIGHTGREEN, GREEN, LIGHTCYAN, CYAN, BLUE,
            LIGHTBLUE, PINK, PURPLE]

class BackgroundColors:
    END = '\033[0m'
    LIGHTGREY = '\033[47m'
    RED = '\033[41m'
    ORANGE = '\033[43m'
    GREEN = '\033[42m'
    BLUE = '\033[44m'
    CYAN = '\033[46m'
    PURPLE = '\033[45m'
    BLACK = '\033[40m'
    LIST = [LIGHTGREY, RED, ORANGE, GREEN, BLUE, CYAN, PURPLE, BLACK]

class ConsoleColors:
    class Settings(SettingsParameters):
        pass
    class color(ForeGroundColors):
        pass
    class background(BackgroundColors):
        pass
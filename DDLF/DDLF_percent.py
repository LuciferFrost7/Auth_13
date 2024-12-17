def value_get(value: float, percent: float) -> float:
    """ Function for get percent of value """
    return value * (percent / 100)

def value_from(value: float, percent: float) -> float:
    """ Function for get before value from after value and percent """
    return value / (percent / 100)

def get_percent(first_value: float, second_value: float, rounding:int = 0) -> float:
    """ Function for get percent from before value and after value """
    return (second_value / first_value) * 100 if rounding == 0 else round(100 * (second_value / first_value), 2 + rounding)


class Percent:
    def __init__(self, percent: float):
        self.percent = (percent / 100)
        print('<class Percent> : percent successfully created')

    def __str__(self):
        return str(self.percent * 100) + '%'

    def __bool__(self):
        return self.percent * 100 == 0

    def __int__(self):
        return round(self.percent * 100)

    def __float__(self):
        return self.percent * 100

    def __repr__(self):
        return str(self.percent * 100) + '%'

    def __eq__(self, other):
        if isinstance(other, Percent):
            return self.percent == other.percent
        elif isinstance(other, int):
            return round(self.percent * 100) == other
        elif isinstance(other, float):
            return (self.percent * 100) == other
        else:
            print('<class Percent> : can\'t equal this value!')
            return None

    def __ne__(self, other):
        if isinstance(other, Percent):
            return self.percent != other.percent
        elif isinstance(other, int):
            return round(self.percent * 100) != other
        elif isinstance(other, float):
            return (self.percent * 100) != other
        else:
            print('<class Percent> : can\'t not equal this value!')
            return None

    def __lt__(self, other):
        if isinstance(other, Percent):
            return self.percent < other.percent
        elif isinstance(other, int):
            return round(self.percent * 100) < other
        elif isinstance(other, float):
            return (self.percent * 100) < other
        else:
            print('<class Percent> : can\'t compare with this value!')
            return None

    def __gt__(self, other):
        if isinstance(other, Percent):
            return self.percent > other.percent
        elif isinstance(other, int):
            return round(self.percent * 100) > other
        elif isinstance(other, float):
            return (self.percent * 100) > other
        else:
            print('<class Percent> : can\'t compare with this value!')
            return None

    def __le__(self, other):
        if isinstance(other, Percent):
            return self.percent <= other.percent
        elif isinstance(other, int):
            return round(self.percent * 100) <= other
        elif isinstance(other, float):
            return (self.percent * 100) <= other
        else:
            print('<class Percent> : can\'t compare with this value!')
            return None

    def __ge__(self, other):
        if isinstance(other, Percent):
            return self.percent >= other.percent
        elif isinstance(other, int):
            return round(self.percent * 100) >= other
        elif isinstance(other, float):
            return (self.percent * 100) >= other
        else:
            print('<class Percent> : can\'t compare with this value!')
            return None

    def __add__(self, other):
        if isinstance(other, Percent):
            return self.percent * 100 + other.percent * 100
        elif isinstance(other, int):
            return self.percent * 100 + other
        elif isinstance(other, float):
            return self.percent * 100 + other
        else:
            print('<class Percent> : can\'t addiction with this value!')

    def __sub__(self, other):
        if isinstance(other, Percent):
            return self.percent * 100 - other.percent * 100
        elif isinstance(other, int):
            return self.percent * 100 - other
        elif isinstance(other, float):
            return self.percent * 100 - other
        else:
            print('<class Percent> : can\'t subbing with this value!')

    def __mul__(self, other):
        if isinstance(other, Percent):
            return self.percent * 100 * other.percent * 100
        elif isinstance(other, int):
            return self.percent * 100 * other
        elif isinstance(other, float):
            return self.percent * 100 * other
        else:
            print('<class Percent> : can\'t multiplicative with this value!')

    def __idiv__(self, other):
        try:
            if isinstance(other, Percent):
                return self.percent * 100 / other.percent * 100
            elif isinstance(other, int):
                return self.percent * 100 / other
            elif isinstance(other, float):
                return self.percent * 100 / other
            else:
                print('<class Percent> : can\'t divide with this value!')
        except:
            print('<class Percent> : can\'t divide with 0!')

    def __mod__(self, other):
        if isinstance(other, Percent):
            return self.percent * 100 % other.percent * 100
        elif isinstance(other, int):
            return (self.percent * 100) % other
        elif isinstance(other, float):
            return (self.percent * 100) % other
        else:
            print('<class Percent> : can\'t mod with this value!')

    def __or__(self, other):
        return bool(self.percent) or bool(other)

    def __and__(self, other):
        return bool(self.percent) or bool(other)

    def __xor__(self, other):
        return bool(self.percent) ^ bool(other)

    def value_get(self, value):
        if isinstance(value, (float, int)):
            return value * self.percent

    def value_from(self, value):
        if isinstance(value, (float, int)):
            return value / self.percent

    def is_percent(self, value: float, part_of_value: float):
        return self.value_get(value) == part_of_value

    def __del__(self):
        self.percent = None
        print('<class Percent> : percent deleted')

PERCENT_100 = Percent(100)
PERCENT_90 = Percent(90)
PERCENT_80 = Percent(80)
PERCENT_75 = Percent(75)
PERCENT_70 = Percent(70)
PERCENT_60 = Percent(60)
PERCENT_50 = Percent(50)
PERCENT_40 = Percent(40)
PERCENT_30 = Percent(30)
PERCENT_25 = Percent(25)
PERCENT_20 = Percent(20)
PERCENT_10 = Percent(10)
PERCENT_5 = Percent(5)
PERCENT_1 = Percent(1)
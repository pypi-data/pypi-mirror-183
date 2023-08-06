import re

class BirthDay:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value:
            db = re.findall(r"[\d]{4}[-][\d]{2}[-][\d]{2}", value)
            if db:
                db_parts = str(db[0]).split("-")
                if int(db_parts[0]) >= 1930 and int(db_parts[1]) <= 12 and int(db_parts[2]) <= 31:
                    self._value = (str(value))
                else:
                    raise ValueError('Invalid date of birth')
            else:
                raise ValueError('Invalid date of birth')
        else:
            self._value = (str(value))

    def __str__(self) -> str:
        return str(self.value)
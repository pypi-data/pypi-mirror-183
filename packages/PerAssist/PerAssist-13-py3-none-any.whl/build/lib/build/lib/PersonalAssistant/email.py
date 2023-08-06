import re
from PersonalAssistant.messages import messages

class Email:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value:
            ph = re.findall(r"[A-z]+[.]*[\w]*[.]*[\w]+[@][a-z]+[.][a-z]{2,10}", value)
            if ph:
                self._value = (str(value))
            else:
                raise ValueError(messages.get(23))
        else:
            self._value = (str(value))

    def __str__(self) -> str:
        return str(self.value)
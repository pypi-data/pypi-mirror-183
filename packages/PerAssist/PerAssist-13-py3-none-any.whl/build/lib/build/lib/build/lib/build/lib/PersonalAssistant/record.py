from datetime import datetime, timedelta
from PersonalAssistant.phone import Phone
from PersonalAssistant.name import Name
from PersonalAssistant.birthday import BirthDay
from PersonalAssistant.email import Email
from PersonalAssistant.address import Address

class Record:
    def __init__(self, user_name: str, user_phones: tuple = (), user_birthday: str = '') -> None:
        self.name: Name = Name(user_name)
        self.phones: list[Phone] = list()
        for uph in user_phones:
            self.add_phone(uph)
        self.birthday: BirthDay = BirthDay(user_birthday)
        self.e_mails: list[Email] = list()
        self.addresses: list[Address] = list()

    def __str__(self) -> str:
        res = str(self.name) + ", phones: "
        for ph in self.phones:
            res += str(ph) + ", "
        res += "birthday: " + str(self.birthday) + ", "
        res += "e-mails: "
        for em in self.e_mails:
            res += str(em) + ", "
        res += "addresses: "
        for ad in self.addresses:
            res += str(ad)

        return res

    def add_phone(self, user_phone: str):
        self.phones.append(Phone(user_phone))

    def days_to_birthday(self)-> int:
        if self.birthday:
            today = datetime.now().date()
            db = datetime(year=datetime.now().year, month=int(str(self.birthday).split("-")[1]),
                          day=int(str(self.birthday).split("-")[2]))
            db = db.date()
            if db < today:
                db += timedelta(days=365)
            return (db - today).days
        else:
            return -1

    def add_addr(self, user_address: str):
        self.addresses.append(Address(user_address))

    def add_email(self, user_email: str):
        self.e_mails.append(Email(user_email))

    def add_birthday(self, user_birthday: str):
        self.birthday = BirthDay(user_birthday)

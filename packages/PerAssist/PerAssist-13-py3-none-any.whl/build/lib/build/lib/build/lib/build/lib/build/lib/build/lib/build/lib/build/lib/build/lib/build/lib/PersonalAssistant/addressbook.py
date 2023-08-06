from collections import UserDict
from PersonalAssistant.record import Record
from PersonalAssistant.messages import messages
from PersonalAssistant.book_saver import BookSaver

class AddressBook(UserDict, BookSaver):

    def add_record(self, record: Record):
        if self.data.get(str(record.name)):
            raise KeyError(f"User {record.name} already exists")
        else:
            self.data.update({str(record.name): record})

    def update_record(self, record: Record):
        if self.get(str(record.name)):
           self.update({str(record.name): record})
        else:
             raise KeyError(f"User {record.name} not found")
   
    def find_user(self, name: str) -> Record:
        res = self.data.get(name)
        if res:
            return res
        else:
            raise KeyError(f"User {name} not found")

    def search(self, promt):
        res = ""
        users = self.values()
        for user in users:
            if promt in str(user):
                res += str(user) + "\n"
        if res:
            return res
        else:
            raise KeyError(messages.get(14))  
    
    def add_phone(self, user: str, phone: str): # пхоня передается в формате 380999279480. Формат хранения либо оставить такой, либо обсудить
        usr = self.find_user(user)
        if usr:
            usr.add_phone(phone)
        else:
            raise KeyError(f"User {user} not found")
    
    def add_address(self, user: str, address: str):
        usr1 = self.find_user(user)
        if usr1:
            usr1.add_addr(address)
        else:
            raise KeyError(f"User {user} not found")

    def add_email(self, user: str, email: str):
        usr = self.find_user(user)
        if usr:
            usr.add_email(email)
        else:
            raise KeyError(f"User {user} not found")

    def add_birthday(self, user: str, birthday: str):
        usr = self.find_user(user)
        if usr:
            usr.add_birthday(birthday)
        else:
            raise KeyError(f"User {user} not found")

    def delete_contact(self, user: str):
        try:
            self.data.pop(user)
        except:
            raise KeyError(f"User {user} not found")
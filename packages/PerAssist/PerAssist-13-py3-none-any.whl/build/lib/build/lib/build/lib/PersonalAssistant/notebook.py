from PersonalAssistant.note import Note
from collections import UserDict
from PersonalAssistant.messages import messages
from PersonalAssistant.book_saver import BookSaver

class NoteBook(UserDict, BookSaver):
    def __init__(self):
        super().__init__()
        try:
            self.load_book('Notes.not')
        except:
            pass

    def get_all_notes(self):
        result = ''
        keys = self.keys()
        for note in keys:
            result += str(self.get(note)) + '\n'
        return result

    def add_note(self, note: Note):
        self.update({str(note.caption): note})

    def del_note(self, promt: str):
        try:
            del self[promt]
            return messages.get(-1)
        except:
            raise KeyError(messages.get(21))  # 21 "There is no note '{promt}'"

    def update_note(self, note: Note):
        if self.get(str(note.caption)):
            self.update({str(note.caption): note})
        else:
            raise KeyError(messages.get(21))  # 21 "There is no note '{note.caption}'"

    def find_note(self, promt: str):
        result = ''
        keys = self.keys()
        for note in keys:
            if str(self.get(note)).find(promt) >= 0:
                result += str(self.get(note)) + '\n'
        if result:
            return result
        raise KeyError(messages.get(20))  # 20 "There is no notes with text '{promt}'"

    def find_notes_tags(self, promt: str):  # поиск заметок, которые имеют данный тег
        print(promt)
        if len(promt) < 2 or promt[0] != '#':
            raise KeyError(ValueError(messages.get(19), promt))  # 19 "Search tag must start with # and contain at least 1 character '{promt}'"
        result = ''
        keys = self.keys()
        for note in keys:
            if promt in self.get(note).tags:
                result += str(self.get(note)) + '\n'
        if result:
            return result
        raise ValueError(messages.get(18))  # 18 "There is no notes with tag '{promt}'"

    def show_all_tags(self):  # выводит список уникальных тегов, которые есть среди всех заметок
        result = []
        keys = self.keys()
        for note in keys:
            for i in self.get(note).tags:
                if i not in result:
                    result.append(i)
        if result:
            return result
        raise ValueError(messages.get(17))  # 17 "There is no tags"

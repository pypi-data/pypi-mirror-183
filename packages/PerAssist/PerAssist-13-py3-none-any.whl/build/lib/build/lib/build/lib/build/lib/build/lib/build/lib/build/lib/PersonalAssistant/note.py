class Note():
    def __init__(self, caption: str, text: str) -> None:
        self.caption = caption
        self._tags = []
        self._text = None
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        r = text.split(' ')
        self._tags = []
        for i in r:
            if i.startswith('#') and len(i) > 1:
                if i not in self._tags:
                    self._tags.append(i)
    @property
    def tags(self):
        return self._tags
    def __str__(self) -> str:
        return f"{self.caption} : {self.text} : Tags: {self.tags}"

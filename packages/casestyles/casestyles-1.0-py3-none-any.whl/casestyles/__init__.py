from functools import cache

__all__ = ["Word", "Name"]

class Word:
    class EmptyValueError(Exception):
        def __init__(self) -> None:
            super().__init__("the value can't be empty")

    class NotLowerValueError(Exception):
        def __init__(self) -> None:
            super().__init__("the value must be lower")

    class NotEnglishValueError(Exception):
        def __init__(self) -> None:
            super().__init__("the value must contain only english letters")

    _value: str
    
    def get(self):
        return self._value

    def set(self, value: str):
        if not value:
            raise self.EmptyValueError

        if not value.islower():
            raise self.NotLowerValueError

        if not value.isalnum():
            raise self.NotEnglishValueError
        
        self._value = value


    def __init__(self, value: str):
        self.set(value)

    def __str__(self):
        return self.get()

class Name:
    class EmptyWordError(Exception):
        def __init__(self) -> None:
            super().__init__("each word in name must not be empty")

    class NotLowerWordError(Exception):
        def __init__(self) -> None:
            super().__init__("each word in name must not be lower")

    class NotEnglishWordError(Exception):
        def __init__(self) -> None:
            super().__init__("each word in name must be alphabet-numeric")

    class NotLowerWordInSnakeCaseError(Exception):
        def __init__(self) -> None:
            super().__init__("each word in snake case name must not be lower")

    class InnerError(Exception):
        def __init__(self) -> None:
            super().__init__("inner error")

    class UnderscoreError(Exception):
        def __init__(self) -> None:
            super().__init__("double underscore and underscores at the and at start in name are not allowed")

    _words: list[Word]

    def __init__(self, words: list[Word]):
        self._words = words

    @classmethod
    def _create_name(cls, words: list[Word]):
        return Name(words)

    @classmethod
    def _create_word(cls, value: str) -> Word:
        return Word(value)

    @classmethod
    def from_words_str_list(cls, words: list[str]):
        try:
            return cls._create_name(list(map(cls._create_word, words)))
        
        except Word.EmptyValueError:
            raise cls.EmptyWordError

        except Word.NotLowerValueError:
            raise cls.NotLowerWordError

        except Word.NotEnglishValueError:
            raise cls.NotEnglishWordError

    @classmethod
    def from_snake_case(cls, value: str) -> "Name":
        try:
            return cls.from_words_str_list(value.split("_"))

        except cls.NotLowerWordError:
            raise cls.NotLowerWordInSnakeCaseError

        except cls.EmptyWordError:
            raise cls.UnderscoreError

    @classmethod
    def from_camel_case(cls, value: str) -> "Name":
        words_str: list[str] = []
        word_str = ""
        for symbol in value:
            if symbol.isupper():
                words_str.append(word_str)
                word_str = ""
            word_str += symbol.lower()
        words_str.append(word_str)
        try:
            return cls.from_words_str_list(words_str)
        
        except (cls.EmptyWordError, cls.NotLowerWordError):
            raise cls.InnerError
    
    @classmethod
    def from_pascal_case(cls, value: str) -> "Name":
        return cls.from_camel_case(value[:1].lower()+value[1:])

    @property
    @cache
    def snake_case(self) -> str:
        return "_".join(map(str, self._words))

    @property
    @cache
    def camel_case(self) -> str:
        camel_case = self.pascal_case
        return camel_case[:1].lower() + camel_case[1:]

    @property
    @cache
    def pascal_case(self) -> str:
        return "".join(map(lambda word: str(word).capitalize(), self._words))
from .naming import character
class Character:
    character={
        character[0]:None,
        character[1]:None,
        character[2]:None
    }

    @classmethod
    def return_character(cls):
        return cls.character

    @classmethod
    def get_character(cls, dict:dict):
        for info in cls.character:
            value=dict.get(info)
            cls.character.update({info:value})
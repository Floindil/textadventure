from ...names_values import character as c
class Character:
    character={
        c[0]:None,
        c[1]:None,
        c[2]:None
    }

    @classmethod
    def get_character(cls, dict:dict):
        for info in cls.character:
            value=dict.get(info)
            cls.character.update({info:value})
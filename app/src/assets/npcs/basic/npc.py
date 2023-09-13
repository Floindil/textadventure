class NPC:
    def __init__(
            self,
            name,
            age,
            eyecolor,
            sex,
            height,
            build,
            haircolor,
            hair_lenght,
            shave,
            profession
            ):
        self.name = name
        self.age = age
        self.eyecolor = eyecolor
        self.sex = sex
        self.height = height
        self.build = build
        self.haircolor = haircolor
        self.hair_lenght = hair_lenght
        self.shave = shave
        self.profession = profession
        self.age_description = self.get_age_description()
        self.calling = self.get_calling()

    def say(self, text: str):
        return f'{self.name}: {text}'
    
    def get_age_description(self):
        if self.age < 16: description = 'underaged'
        elif self.age < 25: description = 'young'
        elif self.age < 40: description = 'middle-aged'
        else: description = 'old'
        return description
    
    def get_calling(self):
        if self.sex == 'Male':
            if self.age < 16: calling = 'Boy'
            else: calling = 'Man'
        elif self.sex == 'Female':
            if self.age < 16: calling = 'Girl'
            else: calling = 'Woman'
class ProfanityFilter:
    def __init__(self):
        self.profanity_list = ['сука', 'блядь', 'блять', 'нахуй', 'піздец', 'пізда', 'пизда', 'йобаний', 'дура',
                               'йобана',
                               'їбать', 'нах', 'пізду', 'піздун',
                               'піздабол', 'піздорезка', 'підар', 'підарас', 'підараска', 'хуйлан', 'хуїла', 'сучка',
                               'дрянь', 'дурак', 'хуя', 'бля',
                               'бл', 'дебіл', 'сук', 'сучий', 'виблядок', 'даун', 'хуйовий', 'піздить', 'пиздити',
                               'піздити',
                               'піздіти', 'пидор']
        self.substitute = '*'

    def censor(self, sentence):
        ''' return censored string'''
        return ' '.join(
            [word if word.lower() not in self.profanity_list else self.substitute * len(word) for word in
             sentence.split()])

    def change_substitute_char(self, new_substitute):
        self.substitute = new_substitute

    def clear_profanity_list(self):
        self.profanity_list.clear()

    def extend_profanity_list(self, pf_list):
        self.profanity_list.extend(pf_list)

    def add_profanity_word(self, word):
        self.profanity_list.append(word)

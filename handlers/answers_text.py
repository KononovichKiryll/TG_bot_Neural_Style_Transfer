lang = 'ENG'
if lang == 'ENG':
    def get_start_answer(name):
        return f'Hi {name}!\n Select what you want to do or \n push /help if you need some help\n'

elif lang == 'RU':
    def get_start_answer(name):
        return f'Привет {name}!\n Выбери что ты хочешь сделать\n или нажми /help если нужна помощь\n'

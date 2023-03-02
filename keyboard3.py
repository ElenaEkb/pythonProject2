#from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class MessageSender:
    def __init__(self, user_id, vk_group_client):
        self.user_id = user_id
        self.vk_group_client = vk_group_client

    def write_msg(self, message):
        params = {'user_id': self.user_id, 'message': message,
                  'random_id': random.randrange(10 ** 7), 'keyboard': keyboard}
        self.vk_group_client.method('messages.send', params)

def create_keyboard(dict_of_buttons):
    colors = {'green': VkKeyboardColor.POSITIVE,
              'red': VkKeyboardColor.NEGATIVE,
              'blue': VkKeyboardColor.PRIMARY,
              'white': VkKeyboardColor.SECONDARY}
    keyboard = VkKeyboard(one_time=True)
    for button, color in dict_of_buttons.items():
        if not button:
            keyboard.add_line()
        else:
            keyboard.add_button(button, color=colors[color])
    return keyboard.get_keyboard()


keyboard_main = create_keyboard({'Поиск': 'green',
                                  'Смотреть': 'blue',
                                  'Удалить': 'red'})

keyboard_favorites = create_keyboard({'Удалить': 'red',
                                      'Главное меню': 'blue'})

keyboard_yes_or_no = create_keyboard({'Да': 'green',
                                      'нет': 'red'})
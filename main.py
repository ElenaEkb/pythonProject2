from bot import *
from vk_api.longpoll import VkEventType, VkLongPoll
from bd import *
from config import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = event.user_id
        if request == 'привет':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('поиск', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('удалить', color=VkKeyboardColor.NEGATIVE)
            keyboard.add_button('смотреть', color=VkKeyboardColor.SECONDARY)
            bot.send_msg(user_id, f'{bot.name(user_id)} Бот готов к поиску, наберите: \n '
                                  f' "Поиск или f" - Поиск людей. \n'
                                  f' "Удалить или d" - удаляет старую БД и создает новую. \n'
                                  f' "Смотреть или s" - просмотр следующей записи в БД.', keyboard)
        elif request == 'поиск':
            bot.get_age_of_user(user_id)
            bot.get_target_city(user_id)
            bot.looking_for_persons(user_id)  # выводит список в чат найденных людей и добавляет их в базу данных.
            bot.show_found_person(user_id)    # выводит в чат инфо одного человека из базы данных.
        elif request == 'удалить':
            creating_database()  # удаляет существующую БД и создает новую.
        elif request == 'смотреть':
            bot.show_found_person(user_id)
        else:
            keyboard = VkKeyboard(one_time=True)
            buttons = ['поиск', 'удалить ', 'смотреть']
            buttons_colors = [VkKeyboardColor.POSITIVE, VkKeyboardColor.NEGATIVE, VkKeyboardColor.SECONDARY]

            for btn, btn_color in zip(buttons, buttons_colors):
                keyboard.add_button(btn, btn_color)

            bot.send_msg(user_id, f'{bot.name(user_id)} Бот готов к поиску, наберите: \n '
                                  f' "Поиск или f" - Поиск людей. \n'
                                  f' "Удалить или d" - удаляет старую БД и создает новую. \n'
                                  f' "Смотреть или s" - просмотр следующей записи в БД.', keyboard)







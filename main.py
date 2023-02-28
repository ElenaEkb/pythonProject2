import vk_api
from bd import *
from bot import *
from config import *
from vk_api.longpoll import VkEventType, VkLongPoll
from keyboard import sender


creating_database()
for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        bot.sender(user_id, msg.lower())
        if request == 'поиск':
            bot.get_age_of_user(user_id)
            bot.get_target_city(user_id)
            bot.looking_for_persons(user_id)  # выводит список в чат найденных людей и добавляет их в базу данных.
            bot.show_found_person(user_id)  # выводит в чат инфо одного человека из базы данных.
        elif request == 'удалить':
            creating_database()  # удаляет существующую БД и создает новую.
            bot.send_msg(user_id, f'  Сейчас наберите "Поиск" ')
        elif request == 'смотреть':
            for i in range(0, 1000):
                offset += 1
                bot.show_found_person(user_id)
                break
        else:
            bot.send_msg(user_id, f'{bot.name(user_id)} Бот готов к поиску, наберите: \n '
                                  f' "Поиск" - найденных людей помещаем в БД. \n'
                                  f' "Удалить" - удаляет старую БД и создает новую. \n'
                                  f' "Смотреть" - просмотр следующей записи в БД.')



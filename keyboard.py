#from vk_api.keyboard import VkKeyboard, VkKeyboardColor
#import json

#keyboard = VkKeyboard(one_time=False, inline=False)
#keyboard.add_button("нажмите, чтобы узнать на что я способен \N{smiling face with sunglasses}", VkKeyboardColor.PRIMARY)
#keyboard.add_button("начать автоматический поиск", VkKeyboardColor.POSITIVE)
#keyboard.add_button("начать поиск по индивидуальным предпочтениям", VkKeyboardColor.POSITIVE)
#keyboard = keyboard.get_keyboard()

#keyboard1 = VkKeyboard(one_time=False, inline=True)
keyboard1.add_button(
    label="смотреть",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "text", "text": "смотреть"},
)

keyboard2 = VkKeyboard(one_time=False, inline=True)
keyboard2.add_button(
    label="Закончить просмотр",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "text", "text": "Закончить просмотр"})

keyboard3 = VkKeyboard(one_time=False, inline=True)
keyboard3.add_button(
    label="Удалить",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "text", "text": "Удалить"})

#keyboard = json.dumps(keyboard, ensure_ascii=False)
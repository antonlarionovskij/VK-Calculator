from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.CTTFMK9FAqi30OEbycat_ukNTOYp93w22GiV3CFaZodr6E1EWYTKN6nx7N-FZV1oDbm-1y9F20T1QD6oyXRiSKB9vsG9-Ui6jWde0DbwpsBMqXnzLtEyNAxdyAlSOm1hdVB0Ix5Mygxhh8my-nGW5dS063w3N60so2RJZPN43B6IJKPj6f0CpSe9e3uvE1iFVqzMaebofiB8OjrtaAJmHQ")
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

def message_from_bot(otvet, keybord):
    Lsvk.messages.send(
        user_id=event.user_id,
        message=otvet,
        random_id=get_random_id(),
        keyboard=keybord,
        )
# Клавиатура основная
def get_menu():
    keyboard = VkKeyboard(one_time=False)
    keys = [["7", "8", "9", "+", "*"],
            ["4", "5", "6", "-", "/"],
            ["1", "2", "3",  "=", "xⁿ"],
            ["0", ".", "±",  "C"],
            ["Exit", "π", "sin", "cos"],
            ["(", ")","n!","√2"]]
    for keyline in range(len(keys)-1):
        for key in range(len(keys[keyline])):
            keyboard.add_button(keys[keyline][key], color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
    for key in range(4):
        keyboard.add_button(keys[5][key], color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


# логика калькулятора
def calc(key):
    global memory
    if key == "=":
# исключение написания слов
        str1 = "-+0123456789.*/)("
        if list(event.message)[0] not in str1:
            message_from_bot('Первым символом должна быть цифра!', None)
            messagebox.showerror("Error!", "You did not enter the number!")
# исчисления
        try:
            result = eval(event.message.get())
            event.message.insert(END, "=" + str(result))
        except:
            event.message.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")


print('Бот запущен')


for event in Lslongpoll.listen():          # Инициируем цикл работы бота
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Калькулятор':
            message_from_bot('Держи!', get_menu()) # VkKeyboard.get_empty_keyboard()
        if event.text == "π":
            message_from_bot(math.pi, get_menu())
        if event.text == "Exit":
            message_from_bot('Выхожу!', VkKeyboard.get_empty_keyboard())
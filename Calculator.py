import vk_api, math
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.CTTFMK9FAqi30OEbycat_ukNTOYp93w22GiV3CFaZodr6E1EWYTKN6nx7N-FZV1oDbm-1y9F20T1QD6oyXRiSKB9vsG9-Ui6jWde0DbwpsBMqXnzLtEyNAxdyAlSOm1hdVB0Ix5Mygxhh8my-nGW5dS063w3N60so2RJZPN43B6IJKPj6f0CpSe9e3uvE1iFVqzMaebofiB8OjrtaAJmHQ")
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

def message_from_bot(otvet):
    Lsvk.messages.send(
        user_id=event.user_id,
        message=otvet,
        random_id=get_random_id(),
        )
# Клавиатура основная

print('Бот запущен')

for event in Lslongpoll.listen():  # Инициируем цикл работы бота
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        request = str(event.text)
        if "+" in event.text or "-" in event.text or "×" in event.text or "÷" in event.text or "sin" in event.text or "cos" in event.text or "pi" in event.text:
            new_request = request.replace("×", "*").replace("÷", "/").replace("sin", "math.sin").replace("cos", "math.cos").replace("pi", 'math.pi')
            try:
                message_from_bot(eval(new_request))
            except SyntaxError:
                message_from_bot("Ошибка")
            except TypeError:
                message_from_bot("Ошибка")
            except NameError:
                message_from_bot("Ошибка")



import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.CTTFMK9FAqi30OEbycat_ukNTOYp93w22GiV3CFaZodr6E1EWYTKN6nx7N-FZV1oDbm-1y9F20T1QD6oyXRiSKB9vsG9-Ui6jWde0DbwpsBMqXnzLtEyNAxdyAlSOm1hdVB0Ix5Mygxhh8my-nGW5dS063w3N60so2RJZPN43B6IJKPj6f0CpSe9e3uvE1iFVqzMaebofiB8OjrtaAJmHQ")
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

def message_from_bot(otvet):
    Lsvk.messages.send(
        user_id=None,
        chat_id=event.chat_id,
        message=otvet,
        random_id=get_random_id(),
        )

for event in Lslongpoll.listen():  # Инициируем цикл работы бота
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            #message_from_bot(str(event.__dict__))
            #message_from_bot(str(event.__doc__))
            #message_from_bot(str(event.__reduce__()))
            message_from_bot(str((event.chat_id)))
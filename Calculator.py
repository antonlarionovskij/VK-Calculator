import vk_api, pyparsing, re, math
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from numeric_string_parser import NumericStringParser

vk_session = vk_api.VkApi(token="vk1.a.CTTFMK9FAqi30OEbycat_ukNTOYp93w22GiV3CFaZodr6E1EWYTKN6nx7N-FZV1oDbm-1y9F20T1QD6oyXRiSKB9vsG9-Ui6jWde0DbwpsBMqXnzLtEyNAxdyAlSOm1hdVB0Ix5Mygxhh8my-nGW5dS063w3N60so2RJZPN43B6IJKPj6f0CpSe9e3uvE1iFVqzMaebofiB8OjrtaAJmHQ")
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

def message_from_bot(otvet):
    Lsvk.messages.send(
        user_id=None,
        chat_id=3,
        message=otvet,
        random_id=get_random_id(),
        )

def is_part_in_list(str_, words):
    for word in words:
        if word.lower() in str_.lower():
            return True
    return False

def multiple_replace(string, signs):
    for key, value in signs.items():
        string = string.replace(key, value)
    return string

signs = {'+':'+',
         '-':'-',
         '*':'*',
         '/':'/',
         '×':'*',
         '÷':'/',
         '^':'^',
         'sin':'sin',
         'cos':'cos',
         'tg':'tan',
         'tan':'tan',
         'pi':'pi',
         'abs':'abs',
         'trunc':'trunc',
         'round':'round',
         'e':'e',
         'Sin':'sin',
         'Cos':'cos',
         'Tg':'tan',
         'Tan':'tan',
         'Pi':'pi',
         'Abs':'abs',
         'Trunc':'trunc',
         'Round':'round',
         'E':'e'
        }

print('Бот запущен')

for event in Lslongpoll.listen():  # Инициируем цикл работы бота
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        request = str(event.text)
        if is_part_in_list(request, list(signs.keys())):
            new_request = multiple_replace(request, signs)
            try:
                bot_otvet = NumericStringParser().eval(new_request)
                message_from_bot(bot_otvet)
            except SyntaxError:
                message_from_bot("Ошибка")
            except TypeError:
                message_from_bot("Ошибка")
            except NameError:
                message_from_bot("Ошибка")
            except TimeoutError:
                message_from_bot("Ошибка")
            except AttributeError:
                message_from_bot("Ошибка")
            except IndexError:
                message_from_bot("Ошибка")
            except pyparsing.exceptions.ParseException:
                message_from_bot("Ошибка")
            except ZeroDivisionError:
                message_from_bot("Деление на ноль")
            except OverflowError:
                message_from_bot("Слишком длинное значение")
            except ValueError:
                message_from_bot("Слишком длинное значение")




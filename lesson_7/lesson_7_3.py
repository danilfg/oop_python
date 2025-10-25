try:
    pass
    """Вызывается код в котором может быть ошибка"""
except ValueError as a:
    pass
    """Отлавливает ошибки ValueError"""

except TypeError as a:
    pass
    """Отлавливает ошибки TypeError"""
else:
    pass
    """выполнится если ошибок нет (не попало в except)"""
finally:
    pass
    """Выполняется всегда, если не было Raise или return"""


import requests

BASE_URL = "http://api.hh.ru"

def get_vacancies(base_url):
    try:
        response = requests.get(f"{base_url}/vacancies")
        response.raise_for_status()
        response_json = response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Возникла ошибка: {e}")
    except ValueError:
        print(f"Не удалось получить json")
    except KeyboardInterrupt:
        print("Остановил руками")
    else:
        try:
            resp_for_return = response_json['item']
        except KeyError as e:
            print(f"Некорректный ключ\nОшибка: {e}")
        else:
            return resp_for_return


resp = get_vacancies(BASE_URL)
print(resp)

"""
Все наследуются от BaseException

ValueError, TypeError — неверные данные/типы
IndexError, KeyError — не нашли индекс/ключ
FileNotFoundError, PermissionError — файловые операции
requests-исключения: Timeout, ConnectionError, HTTPError
KeyboardInterrupt
"""
print('Задача 3. May the force be with you')

# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной.
#
# Внимательно изучите документацию этого API и напишите программу,
# которая выводит на экран (и в JSON-файл) информацию о
# пилотах легендарного корабля Millennium Falcon.
#
# Информация о корабле должна содержать следующие пункты:
# название,
# максимальная скорость,
# класс,
# список пилотов.
#
# Внутри списка о каждом пилоте должна быть следующая информация:
# имя,
# рост,
# вес,
# родная планета,
# ссылка на информацию о родной планете.

import requests
import json


def get_millennium_falcon_info():
    # URL для запроса информации о Millennium Falcon
    url = "https://swapi.dev/api/starships/10/"

    # Отправка GET-запроса к API Star Wars
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Извлечение данных в формате JSON
        data = response.json()

        # Получение информации о пилотах
        pilots_info = []
        for pilot_url in data['pilots']:
            pilot_data = requests.get(pilot_url).json()
            planet_data = requests.get(pilot_data['homeworld']).json()

            pilot_info = {
                'name': pilot_data['name'],
                'height': pilot_data['height'],
                'mass': pilot_data['mass'],
                'homeworld': planet_data['name'],
                'homeworld_url': pilot_data['homeworld'],
            }
            pilots_info.append(pilot_info)

        # Формирование общей информации о Millennium Falcon
        falcon_info = {
            'ship_name': data['name'],
            'max_atmosphering_speed': data['max_atmosphering_speed'],
            'starship_class': data['starship_class'],
            'pilots': pilots_info,
        }

        return falcon_info
    else:
        # Если запрос неудачен, выводим сообщение об ошибке
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None


# Получение информации и вывод на экран
millennium_falcon_info = get_millennium_falcon_info()

if millennium_falcon_info:
    # Вывод на экран
    print(json.dumps(millennium_falcon_info, indent=2))

    # Запись в JSON-файл
    with open('millennium_falcon_info.json', 'w') as json_file:
        json.dump(millennium_falcon_info, json_file, indent=2)

print()

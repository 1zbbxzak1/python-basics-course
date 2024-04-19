print('Задача 5. Web scraping')

# Дан несложный пример HTML-страницы: Sample Web Page.
#
# Изучите код этой страницы и реализуйте программу,
# которая получает список всех подзаголовков сайта (они заключены в теги <h3>).

import requests
from bs4 import BeautifulSoup


def get_subheadings(url):
    # Отправляем GET-запрос к веб-странице
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-кода страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все подзаголовки с тегом <h3>
        subheadings = [heading.text.strip() for heading in soup.find_all('h3')]

        return subheadings
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None


# URL веб-страницы
url = "http://www.columbia.edu/~fdc/sample.html"

# Получаем список подзаголовков
subheadings = get_subheadings(url)

# Выводим результат
if subheadings:
    print(subheadings)

print()

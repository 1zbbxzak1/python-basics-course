print('Задача 2. Функция обратного вызова')

# При работе с сетью и веб-сервисами иногда используется функция callback,
# так называемая функция обратного вызова.
# Это функция, которая вызывается при срабатывании определённого события:
# переходе на страницу, получении сообщения или окончании обработки процессором.
# В неё можно передать функцию, чтобы она выполнилась после определённого события.
# Это используется, например, в HTTP-серверах в ответ на URL-запросы.
# Реализуйте такую функцию.


class App:

    def __init__(self):
        self.routes = {}

    def get(self, path):
        return self.routes.get(path)

    def add_route(self, path, callback_func):
        self.routes[path] = callback_func


app = App()


def callback(path):

    def decorator(func):
        app.add_route(path, func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

print()

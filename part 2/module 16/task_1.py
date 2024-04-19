print('Задача 1. Права доступа')

# Напишите декоратор check_permission, который проверяет,
# есть ли у пользователя доступ к вызываемой функции, и
# если нет, то выдаёт исключение PermissionError.


def check_permission(required_permission):

    def decorator(func):

        def wrapper(*args, **kwargs):
            # Проверяем, есть ли у пользователя необходимое право
            if required_permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(
                    f"PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}"
                )

        return wrapper

    return decorator


# Пример использования:
user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
try:
    add_comment()
except PermissionError as e:
    print(e)

print()

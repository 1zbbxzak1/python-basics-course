print('Задача 5. Синглтон')

# Реализуйте декоратор singleton, который превращает класс в одноэлементный.
# При множественной инициализации объекта этого класса будет сохранён только первый инстанс,
# а все остальные попытки создания будут возвращать первый экземпляр.


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

print()

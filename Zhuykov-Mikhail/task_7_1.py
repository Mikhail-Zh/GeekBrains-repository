import os


def creating_template_project(template):
    """
    Функция создает заготовку для проекта.
    Принимает словарь:
    Ключ - это название создаваемой папки. Если такая папка уже есть к названию добавляет текущую дату и время.
    Значение - это название создаваемой подпапки.
    """
    for key, val in template.items():  # Цикл для определения и создания директорий и поддиректорий.
        if not os.path.exists(key):  # Создает директорию если нет папки с таким же названием.
            os.mkdir(key)
        for item in val:  # Цикл для определения и создания поддиректорий.
            dir_path = os.path.join(os.path.abspath(key), item)  # Директория где нужно создать поддиректорию.
            if not os.path.exists(dir_path):  # Создает директорию если нет папки с таким же названием.
                os.makedirs(dir_path)


project_template = {'my_project': ('settings', 'mainapp', 'adminapp', 'authapp')}  # Заготовка для проекта.

creating_template_project(project_template)

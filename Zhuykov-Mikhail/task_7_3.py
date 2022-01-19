import os
from shutil import copytree


def collecting_templates(project):
    """
    Функция копирует папки с файлами из папок templates в папку templates расположенную в корне my_new_project.
    """
    root = os.path.join(project, 'templates')  # Адрес папки в которую будут копироваться шаблоны.
    if not os.path.exists(root):  # Создает директорию templates если папки с таким названием нет.
        os.makedirs(root)
    for dir_path, dir_names, file_names in os.walk(project):  # Цикл для нахождения папок и файлов.
        for dir_name in dir_names:  # Цикл для получения имен папок из цикла os.walk
            try:
                if dir_path.split('\\')[-1] == 'templates' and dir_path != project:  # Условие для копирования шаблона
                    copytree(os.path.join(dir_path, dir_name), os.path.join(root, dir_name))
            except FileExistsError:  # Исключение, если папка с таким названием уже существует
                continue  # Продолжить, если название папки уже существует


folder = os.path.abspath('my_new_project')
collecting_templates(folder)

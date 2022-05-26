# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в
# проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым. В папках
# mainapp, authapp и аналогичных могут быть и другие файлы, с другими раширениями, кроме тех что приведенны в
# примере. Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации;
# Примечание:
#
# это вполне реальная задача, которая решена, например, во фреймворке django.

import os
from shutil import copytree

project_path = os.path.join(os.getcwd(), 'my_project')

if not os.path.exists(os.path.join(project_path, 'templates')):
    os.mkdir(os.path.join(project_path, 'templates'))

mother_templates_path = os.path.join(project_path, 'templates')


for root, dirs, files in os.walk('my_project'):
    # if root.strip().rsplit("\\", maxsplit=1) == "templates":
    # for dir in dirs:
    if len(dirs) > 0:
        if dirs[0] == 'templates':
            copytree(os.path.join(root, dirs[0]), mother_templates_path, dirs_exist_ok=True)



            # list_dir = os.listdir(os.path.join(root, dirs[0]))
            # for dir in list_dir:
            #     copytree(os.path.join(root, dirs[0], dir), mother_templates_path, dirs_exist_ok=True)
            # for item in os.scandir(os.path.join(root, dirs[0])):
            #     copytree(item, mother_templates_path, dirs_exist_ok=True)

        # print(root, len(dirs), len(files))

# and os.path.abspath(dir) != os.path.abspath(mother_templates_path):
# Урок 10
Для начала работы скопируйте репозиторий на локальную машину:
c помощью команды в терминале

`git clone https://github.com/skypro-008/lesson10-and-tests.git`

Откройте склонированный репозиторий в PyCharm.

### Cоздайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm
Появляется всплывающее окно, Creating virtuan envrironment c тремя полями.
В первом поле выбираем размещение папки с вирутальным окружением, как правило это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпритатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран фаил requirements.txt, находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson10-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значек ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

#### Настройка виртуального окружения завершена!

### Порядок выполнения заданий
#### Часть 1:

- part1/welcome_page
- part1/rules
- part1/feed
- part1/friends
- part1/trends
- part1/tag
- part1/comments
- part1/profile
- part1/settings
- part1/company

Задачи описаны в комментариях в файлах с расширением html
В текущих заданиях вы будете работать с html-версткой. 
После того, как Вы выполнили  задание, попробуйте запустить фаил в браузере.


Если картинка выглядит корректно, проверьте правильность
верстки, запустив таким же образом фаил test.py который находится
в той же директории, что и фаил с заданием.

*Обращаем ваше внимание, что для каждого задания предусмотрены свои тесты
и запускать нужно именно те тесты, которые находятся в папке с заданием*

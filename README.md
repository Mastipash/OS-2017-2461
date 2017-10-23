# OS-2017-2461
Example HTPM5 pserver roject 

## Установка программы

Для того, чтобы установить данный "пакет" на рабочую станцию необходимо

  1. Убедиться в том, что в дистрибутиве Linux установлен Python версии 3.
     Если Python не установлен, то для дистрибутива Debian надо запустить команду
     ```shell
     $ sudo apt install python3
     ```

  2. Установить утилиту создания виртуальных сред программирования Python,
     которая называется `virtualenv`.

     ```shell
     $ sudo install virtualenv
     ```

  3. Создать виртуальную среду и присоединиться к ней. Пусть папка со средой называется `env`.
     ```shell
     $ virtualenv -p python3 env
     $ . env/bin/activate
     ```

  4. Установить необходимые модулей.
     ```shell
     $ pip install pyramid pyramid_debugtoolbar pyramid_chameleon
     ```

  5. Запустить приложение.
     ```shell
     $ python app.py
     ```

     Адрес локального сайта теперь будет - http://127.0.0.1:8080


Всего хорошего!


import socket, sys

client = socket.socket()

ip, port = str(sys.argv[1]), int(sys.argv[2])
try:
    client.connect((ip, port))
except:
    print("Похоже вы неправильно ввели данные, попробуйте еще раз. Пример: \nIP: 127.0.0.1 PORT: 25565")
    sys.exit()
b = True

while True:
    if b == True:
        inp = input('>>> ')
        b = False
    else:
        if inp == 'ex':
            print("Прикрываем лавочку")
            client.send(inp.encode('utf-8'))
            print(data)
            break
        if inp == 'help':
            print('''
            
            ls
            Посмотреть все файлы и папки в вашей деректории

            ex
            Отключиться от сервера

            getdir
            Посмотреть путь к вашей деректории
            
            pydir
            Посмотреть каталог установки python
            
            socksd
            Выключить сервер
            
            winsd
            Выключить компютер вместе с сервером
            
            osinfo
            Информация об ОС на которой был запущен сервер
            
            cd (arg)
            Переход в указанную деректорию,
            (arg) '-' Переход в прошлую деректорию
            (arg) 'mydir' Переход в указанную деректорию если она существует дальше по дереву4
            
            calc (arg)
            Калькулятор,
            (arg) '3+3*3' То что нужно посчитать
            
            cfile (arg)
            Создает файл в деректории по умолчанию,
            (arg) 'test.txt' Имя и расширение создаваемого файла
            
            cdir (arg)
            Создает папку внутри вашей деректории,
            (arg) 'folder' Имя создаваемой папки
            
            rmfile (arg)
            Удаляет файл в деректории по умолчанию,
            (arg) 'test.txt' Имя и расширение удяляемого файла
            
            rmdir (arg)
            Удаляет папку внутри вашей деректории,
            (arg) 'folder' Имя удаляемой папки
            
            refile (arg)..(arg1)
            Переименовывает файл внутри вашей деректории,
            (arg) 'test.txt' Имя файла который надо переименовать
            (arg1) 'test1.txt' Имя в которое файл переименовывается
            
            open (arg)..read
            Чтение и вывод написанного в файле в вашей деректории на экран, с ограниченным числом байт,
            (arg) 'test.txt' Имя файла который надо прочитать
            **ОГРАНИЧЕННОЕ КОЛ-ВО БАЙТ, ФАЙЛ МОЖЕТ ВЫВЕСТИСЬ НЕ ВЕСЬ**
            
            open (arg)..write..(-{arg1}-)
            Заменить весь текст в файле и записать новый,
            (arg) 'test.txt' Имя файла который редактируется
            (-{arg1}-) '-{test message;in file}-' То что будет записанно в файл, ';' означает перенос строки
            
            open (arg)..py
            Открыть файл .py,
            (arg) 'test.py' Имя файла который откроется
            **УЧТИТЕ ЧТО ПОСЛЕ КОМАНДЫ СЕРВЕР СРАЗУ ОТКЛЮЧИТСЯ ДО МОМЕНТА ПОКА НЕ ЗАКОНЧИТСЯ ВЫПОЛНЕНИЕ МОДУЛЯ**
            
            open (arg)..exe
            Открыть файл .exe,
            (arg) 'test.exe' Имя файла который откроется
            
            open (arg)..bat
            Открыть файл .bat,
            (arg) 'test.bat' Имя файла который откроется
            **ВЫ НЕ МОЖЕТЕ ВЫПОЛНЯТЬ КОМАНДЫ CMD.EXE НЕ ЧЕРЕЗ .BAT**
            
            link (arg)
            Открыть ссылку в браузере (Google Chrome),
            (arg) 'vk.com', 'https://vk.com' Имя файла который откроется
            
            ''')
        else:
            client.send(inp.encode('utf-8'))
            dt = client.recv(9999999)
            data = dt.decode('utf-8')
            print(data)
        b = True
        print('\n')
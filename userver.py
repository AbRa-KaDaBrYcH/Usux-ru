try:
    def funcimp():
        exec("import " + a)
    def get_temp(data):
        city = str(data.split(" ")[1])
        mgr = owm.weather_manager()
        obs = mgr.weather_at_place(city)
        weat = obs.weather
        
        temp = weat.temperature('celsius')

        user.send(("В городе " + city + " сейчас " + str(temp["temp"])).encode("utf-8"))

    import socket, threading, os, sys, pyowm
    from threading import Thread
    from datetime import datetime
    from subprocess import Popen
    import subprocess
    import webbrowser as wb

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    tlog = ''
    count = 0
    try:
        try:
            wb.register('chrome', None, wb.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        except:
            wb.register('chrome', None, wb.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
        br = True
    except:
        print("Команда link не работает, отсутсвует браузер Chrome на компьютере")
        br = False
    try:
        ip = input("Введите IP> ")
        port = input("Введите PORT> ")

        server.bind(
            (ip, int(port))
        )
        print("Сервер включен!")
    except:
        input("Похоже вы неправильно ввели данные, попробуйте еще раз. Пример: \nIP: 127.0.0.1 PORT: 25565")
        sys.exit()
        
    server.listen(5)
    log = [f'{datetime.now()}: Сервер Запущен!']
    user, adress = server.accept()
    with open('adr.txt', 'w') as txt:
        txt.write(str(adress))
    print('Законектился')
    run = True
    p1 = path = os.path.abspath('')
    
    #192.168.15.101
    
    while run:
        dt = user.recv(2048)
        data = dt.decode('utf-8')
        if data == 'test':
            user.send(("test").encode("utf-8"))
            print(f'Использованна команда {data}')
            log.append(f'{datetime.now()}: {data}')
        if data == 'pydir':
            user.send((os.path.dirname(sys.executable)).encode("utf-8"))
            print(f'Использованна команда {data}')
            log.append(f'{datetime.now()}: {data}')
        if data == 'winsd':
            log.append(f'{datetime.now()}: {data}')
            
            user.send(("Выключаюсь(").encode("utf-8"))
            server.close()
            os.system('shutdown -s')
        if data == 'osinfo':
            log.append(f'{datetime.now()}: {data}')
            
            user.send((os.name).encode("utf-8"))
        if data == 'socksd':
            log.append(f'{datetime.now()}: {data}')
            
            user.send(("Выключаюсь(").encode("utf-8"))
            sys.exit()
        if data == 'ex':
            log.append(f'{datetime.now()}: {data}')
            
            user.send(("Отключаю успешно").encode("utf-8"))
        if data == 'ls':
            log.append(f'{datetime.now()}: {data}')
            
            ls = os.listdir(path=p1)

            a = (str(ls).split("["))[1].split("]")
            
            user.send((str(a[0])).encode("utf-8"))
            print(f'Использованна команда {data}')
        if data == 'getdir':
            log.append(f'{datetime.now()}: {data}')
            
            user.send(("я сейчас в директории " + p1).encode("utf-8"))
            print(f'Использованна команда {data}')   
        if str(data.split(" ")[0]) == 'cd':
            log.append(f'{datetime.now()}: {data}')
            
            if str(data.split(" ")[1]) == '-':
                c = path.split("\\")
                if path[len(path)-1:len(path)] == '\\':
                    print(path)
                    del c[int(len(c))-1]

                if len(path) == 3 or len(path) == 4:
                    user.send(("Куда дальше то?").encode("utf-8"))
                
                else:
                    del c[int(len(c))-1]
                    path = ''
                    for name in c:
                        path += f'{name}\\'
                    os.path.join(path)
                    user.send(("Я в директории " + path).encode("utf-8"))
                    
                print(path)
            else:
                if os.path.exists(f'{path}\{str(data.split(" ")[1])}'):
                    b = str(data.split(" ")[1])
                    
                    if path[len(path)-1] == '\\':
                        path = f'{path}{b}'
                    else:
                        path = f'{path}\{b}'
                    print(path)
                    os.path.join(path)
                    user.send(("Я в директории " + path).encode("utf-8"))
                else:
                    user.send(("Директория не существует, сорян(").encode("utf-8"))

            os.chdir(p1)
            
            print(f'Использованна команда {data}')
            p1 = path
        if str(data.split(" ")[0]) == 'cfile':
            log.append(f'{datetime.now()}: {data}')
            
            os.chdir(p1)
            name = str(data.split(" ")[1])
            print(f'{p1}\{name}')
            txt = open(f'{p1}\{name}', 'w')
            txt.close()

            user.send(("Создал файл " + name + " в директории " + path).encode("utf-8"))
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'calc':
            log.append(f'{datetime.now()}: {data}')
            
            cifry = str(data.split(" ")[1])
            
            c = int(eval(cifry))
            
            user.send((str(c)).encode("utf-8"))
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'cdir':
            log.append(f'{datetime.now()}: {data}')
            os.chdir(p1)
            try:
                os.mkdir(str(data.split(" ")[1]))
                user.send(("Создал папку " + str(data.split(" ")[1]) + " в директории " + p1).encode("utf-8"))
            except:
                user.send(("Не могу создать папку тк она уже существует").encode("utf-8"))
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'rmdir':
            log.append(f'{datetime.now()}: {data}')
            os.chdir(p1)
            try:
                os.rmdir(str(data.split(" ")[1]))
                user.send(("Удалил папку " + str(data.split(" ")[1]) + " в директории " + p1).encode("utf-8"))
            except:
                user.send(("Извиняй, такой директории не существует(").encode("utf-8"))
                
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'rmfile':
            log.append(f'{datetime.now()}: {data}')
            os.chdir(p1)
            try:
                os.remove(str(data.split(" ")[1]))
                user.send(("Удалил файл " + str(data.split(" ")[1]) + " в директории " + p1).encode("utf-8"))
            except:
                user.send(("Сорян, я не нашел этот файл(").encode("utf-8"))
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'refile':
            log.append(f'{datetime.now()}: {data}')
            os.chdir(p1)
            a = str(data.split(" ")[1])
            try:
                os.rename(str(data.split(" ")[1]), str(data.split(" ")[2]))
                user.send(("Переименовал файл " + str(data.split(" ")[1]) + " на " + str(data.split(" ")[2]) + " в директории " + p1).encode("utf-8"))
            except:
                user.send(("Файл не нашел, сорян").encode("utf-8"))
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'open':
            log.append(f'{datetime.now()}: {data}')

            a = str(data.split(" ")[1])
            b = a.split("..")
            text = ''
            if b[1] == 'read':
                try:
                    try:
                        with open(f'{p1}\{b[0]}', 'r', encoding='utf-8') as txt:
                            ab = txt.read()
                            user.send(("В этом файле написанно:\n" + ab).encode("utf-8"))
                    except:
                        with open(f'{p1}\{b[0]}', 'r') as txt:
                            ab = txt.read()
                            user.send(("В этом файле написанно:\n" + ab).encode("utf-8"))
                except:
                    user.send(("Ошибка! Может этого файла не существует?").encode("utf-8"))
            if b[1] == 'write':
                try:
                    c = str(data.split("..")[2])
                    with open(f'{p1}\{b[0]}', 'w') as txt:
                        wr1 = c.split("-{")
                        wr2 = wr1[1].split("}-")
                        wr = wr2[0].split(";")
                        for i in wr:
                            text += f'{i}\n'
                        txt.write(text)
                        user.send(("Вписал текст выше в файл " + b[0] + " в директории " + p1).encode("utf-8"))
                except:
                    user.send(("Ошибка! Может этого файла не существует?").encode("utf-8"))
            if b[1] == 'py':
                try:
                    if b[2] == 'imp':
                        if1 = threading.Thread(target=impfrom, args=(b[0]))
                        if1.start()
                        user.send(("Открыл питонский файл " + b[0] + " в директории " + p1).encode("utf-8"))
                    else:
                        user.send(("Аргумент " + b[2] + " не найден").encode("utf-8"))
                except:
                    user.send(("Эта функция недоработана, в обновлениях поправлю)").encode("utf-8"))
            if b[1] == 'bat':
                try:
                    p = Popen(b[0], cwd=p1)
                    stdout, stderr = p.communicate()
                    print('bat')
                    user.send(("Включил " + b[0] + " в директории " + p1).encode("utf-8"))
                except:
                    user.send(("Ошибка! Может этого файла не существует?").encode("utf-8"))
            if b[1] == 'exe':
                try:
                    subprocess.call(f'{p1}\{b[0]}')
                    user.send(("Включил " + b[0] + " в директории " + p1).encode("utf-8"))
                except:
                    user.send(("Ошибка! Может этого файла не существует?").encode("utf-8"))
                
            if not(b[1] == 'exe', b[1] == 'bat', b[1] == 'py', b[1] == 'write', b[1] == 'read'):
                user.send(("Аргумент " + b[1] + " не найден").encode("utf-8"))
            
            print(f'Использованна команда {data}')
        if str(data.split(" ")[0]) == 'link':
            log.append(f'{datetime.now()}: {data}')
            if br == True:
                try:
                    try:
                        wb.get('chrome').open_new_tab(str(f'https://{data.split(" ")[1]}'))
                    except:
                        wb.get('chrome').open_new_tab(str(f'http://{data.split(" ")[1]}'))
                    user.send(("Открыл").encode("utf-8"))
                except:
                    try:
                        wb.get('chrome').open_new_tab(str(data.split(" ")[1]))
                        user.send(("Открыл").encode("utf-8"))
                    except:
                        user.send(("Проверь, правильно ли ты ввел ссылку, а то чета зайти не могу(").encode("utf-8"))
            else:
                user.send(("Команда link не работает, отсутсвует браузер Chrome на компьютере").encode("utf-8"))
            print(f'Использованна команда {data}')  
        
        if not(str(data.split(" ")[0]) == 'cd' or str(data.split(" ")[0]) == 'cfile' or str(data.split(" ")[0]) == 'calc'or str(data.split(" ")[0]) == 'cdir' or str(data.split(" ")[0]) == 'rmdir' or str(data.split(" ")[0]) == 'rmfile' or str(data.split(" ")[0]) == 'cd' or str(data.split(" ")[0]) == 'refile' or str(data.split(" ")[0]) == 'open' or str(data.split(" ")[0]) == 'link'):
            if not(data == 'test' or data == 'pydir' or data == 'winsd' or data == 'osinfo' or data == 'socksd' or data == 'ex' or data == 'ls' or data == 'getdir'):
                user.send(("Команду не распознал").encode("utf-8"))
                tlog += f'{datetime.now()}: Не распознал команду {data}'
                print(f'Не распознал команду {data}')
except:
    if not(data == 'ex' or data == 'socksd' or data == 'winsd'):
        log.append(f'{datetime.now()}: {data}')
        for i in log:
            count += 1
            if count >= 2:
                tlog += i
                tlog += '\n'
        tlog += f'{datetime.now()}: Ошибка'
        with open('log.txt', 'w') as ttt:
            ttt.write(tlog)
    
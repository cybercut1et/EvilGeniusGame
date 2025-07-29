# -*- coding: utf-8 -*-
from random import randint
#https://docs.python.org/3/library/random.html
#функция randint из библиотеки random помогает нам реализовать эпизод игры в казино и выбор случайного вопроса в финальной битве
from time import sleep
#https://docs.python.org/3/library/time.html
#функция sleep из библиотеки time нужна нам для реализации функции spellreplic которая позволяет выводить фразы постепенно а не просто вываливать их в консоль принтом
from datetime import datetime
#https://docs.python.org/3/library/datetime.html
#функция datetime нужна для генерации названия для файла лога если пользователь пожелает создать уникальный файл для запуска
#import colorama

def filewriting(filename):
    agr = ''
    while agr != '1' and agr != '2':
        agr = input("Выберите режим записи беседы.\n1) Запись в один файл, который будет очищаться вместе с запуском\n2) Запись в новый уникальный файл\n/Введите номер вашего выбора: ")
    if agr == '1': #программа создает файл и с каждым запуском программы будет чистить его перед записью
        file = open(filename, 'w', encoding="utf-8") #файл создаем с кодировкой utf-8 чтобы записывались ascii арты
        file.truncate(0)  # Очистка файла перед запуском
    elif agr == '2': #программа создает уникальный файл с каждым запуском и записывает все туда
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"log_file_{timestamp}.txt"
        file = open(log_filename, 'w', encoding="utf-8")#файл создаем с кодировкой utf-8 чтобы записывались ascii арты
    return file


def replicinput(file, replic):#записывает инпуты в файл
    reply = input(replic)
    file.write(replic + str(reply) + "\n\n")
    return reply

def story_start():
    chapter_counter = 1
    print(f"\n\nГлава {chapter_counter}:----------------------Начало пути----------------------\n\n")

    # while True:
    ##kapcha = input("Для запуска симуляции введите капчу [ Jl064Db ]")
    ##if kapcha == "Jl064Db":
    ##    break
    ##else:
    ##   pass

    replics1 = ["Вы очнулись в непонятном месте\n", "Запах сырости ударил в ноздри\n",
                "Вы никогда не видели это место ранее, оно не похоже ни на одно место, в котором вы бывали\n",
                "Вы судорожно начинаете вспоминать как вас зовут\n", "A, точно, меня зовут... "]
    for replic in replics1:
        spellreplic(replic)
    nickname = replicinput(file, "/Введите ваш псевдоним: ")

    return nickname, chapter_counter


def albert_einstein(nickname, chapter_counter):
    replics2 = ["Вдруг звенящую тишину прервал старческий голос...\n",
                f"\"Эй {nickname}... пардоньте {nickname}, вы меня слышите вообще?\" - пробормотал неизвестный старик из угла комнаты\n",
                "С первых секунд колебания воздуха в замкнутом пространстве некоторого объёма, ко мне пришло понимание кто меня зовёт.\nЭтот голос был до боли знаком мне ещё со школьной парты...\n",
                "Но ведь этого же не может быть... Он ведь давно погиб при печальных обстоятельствах! Это же ...\n",
                "Из злополучного угла послышалось кряхтение престарелого тела\n",
                f"Да-да вы всё правильно поняли, {nickname} ,это я... швейцарский, немецкий и американский физик-теоретик и общественный деятель-гуманист,\nодин из основателей современной теоретической физики. Лауреат Нобелевской премии по физике 1921 года - Альберт Энштейн\" - изрёк старик\n",
                "\"Вы поворачиваете свою голову в сторону зловещего угла. Вы не можете поверить своим глазам.\nПеред вами красуется голограмма самого дедушки Альберта Энштейна\n",
                f"\033[31m[Вы]\033[0m\n-Прошу у Вас прощения, добрый дедушка Альберт Энштейн. Мне никогда не нравилось слушать про Вас,\nнемецкого старика, на уроках физики Антонины Паркиной©\n",
                "Выдал Ваш рот без вашего на то одобрения\n",
                "\033[34m[Альберт Энштейн]\033[0m\n-Ничего страшного... Сейчас не об этом!\n", "Гаркнула историческая личность\n",
                f"\033[34m[Альберт Энштейн]\033[0m\n-Если Вы хоть раз слышали обо мне, то вы должны представлять всю серьезность моих намерений. Я здесь, чтобы помочь Вам, {nickname}\n",
                f"[Ваши мысли]\n-О чем вообще говорит этот старый давно усопший старец?\n", ]

    for replic in replics2:
        spellreplic(replic)

    # desicion1 влияет на ход истории, и на следущую ситуацию
    flag1 = False

    while True:
        reply = replicinput(file, "Вы отошли от шока и готовы сказать своё слово великому физику-теоретику\n1) Оскорбить\n2) Разузнать что же произошло\nВведите номер вашего выбора: ")
        if reply == "1":
            break
        elif reply == "2":
            flag1 = True
            break
        else:
            pass
    decision1_1(flag1, nickname, chapter_counter)


def decision1_1(flag, nickname, chapter_counter):
    replics_decision1_false = [
        f"\033[31m[Вы]\033[0m\n-Альберт Германович, Вы мерзкая развалина, дождевой червь! Я не хочу присутствовать рядом с Вашей голограммой! Убирайтесь отсюда в ужасе!\n",
        "Ответ престарелой голограммы не заставил себя ждать\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Как мне известно, кто обзывается, тот сам так называется! Более того, сейчас я Вас кокну\n",
        "Сказал Альберт и достал из-за голографической пазухи базуку РПГ\n",
        f"\033[34m[Альберт Энштейн]\033[0m\n-Моли о пощаде, жалкое божье создание, {nickname}!\n"]
    replics_decision1_true = [
        f"\033[31m[Вы]\033[0m\n-Альберт Германович, подскажите, пожалуйста, что вообще здесь происходит?\n",
        f"\033[34m[Альберт Энштейн]\033[0m\n-Вы оказались здесь не просто так, {nickname}...\n",
        "Начал общественный деятель\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Дело в том, что кое кто наломал дров. Всему миру грозит большая опасность...\n",
        f"\033[31m[Вы]\033[0m\n-Что же случилось, великий гений?\n",
        "Голограмма учёного трясущимися руками протянула вам продолговатый предмет, внешне напоминающий пульт от кондиционера\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Это устройство позволяет моментально излечить всех больных в радиусе 300 ярдов. Достаточно просто нажать вот эту приятную глазу кнопку\n",
        "Старец наклонился и показал пальцем на большую красную кнопку, расположенную на предмете который напоминал Вам о жарких летних деньках\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Сейчас мы находимся в моей секретной лаборатории з...\n",
        "Физик-гуманист почему-то запнулся, но довольно скоро продолжил рассказ\n",
        f"\033[34m[Альберт Энштейн]\033[0m\n-Вам, {nickname}, предстоит покинуть стены моей уютной отапливаемой лаборатории и отправиться на поиски заболевших\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Ну что, Вы согласны?\n",
        "[Ваши мысли]\n-Хммм...\n",
        "Не успела бы самая безобидная мысль проскочить в вашей маленькой голове, как старик кинул под Вас дымовую гранату,\nи всё вокруг Вас магически-физическим образом исчезло\n",
        "Последнее что вы услышали были вопли старика\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Осторожно, телепортатор может барахлить ввиду просрочки платежа по счёту на оплату кабельного интернета\n"
    ]

    if flag == False:
        chapter_counter += 1
        print(f"\n\nГлава {chapter_counter}:----------------------Неудачное знакомство----------------------\n\n")

        for replic in replics_decision1_false:
            spellreplic(replic)

        flag1 = False
        while True:
            reply1 = replicinput(file,
                "Перед Вами стоит стоит непростой выбор:\n1) Начать молить о пощаде\n2) Попытаться увернуться\nВведите номер вашего выбора: ")
            if reply1 == "1":
                break
            elif reply1 == "2":
                flag1 = True
                break
            else:
                pass
        decision1_2(flag1, nickname, chapter_counter)
    else:
        for replic in replics_decision1_true:
            spellreplic(replic)
        chapter_cringepoyavlenie(nickname, chapter_counter)

def decision1_2(flag, nickname, chapter_counter):
    ##replics_decision1_false = ["Рука Альберта снова лезет за пазуху\n",f"{nickname}\nНет! Пожалуйста, не доставайте базуку РПГ\n","жалобно проскулили Вы\n",f"\033[34m[Альберт Энштейн]\033[0m\n-Успокойтесь, {nickname}, я всего-лишь хочу найти предварительно распечатанную на принтере для Вас задачу\n","Старик достает листочек с задачей и протягивает её Вам\n","Вы приступаете к чтению спасительной задачи\n","Рассчитайте количество теплоты, необходимое для нагревания 10 кг воды на 50 градусов Цельсия\n",f"[Ваши мысли]\n-Помню, в школе нам говорили, что теплоемкость воды равна 4200 Дж/(кг*C)\n-Хммм... не могу вспомнить формулу количества теплоты....\n-А, точно, количество теплоты равно массе тела, умноженной на теплоемкость данного тела, умноженной на изменение температуры этого же тела. Выходит, надо просто перемножить 4200, 10 и 50.",f"\033[34m[Альберт Энштейн]\033[0m\n-{nickname}, пришло время давать ответ\n","Разразился как гром в ясную погоду голос старца\n"]
    replics_decision1_2_false = ["Вы молите о пощаде, и со временем старик убирает оружие\n",
                                 "\033[34m[Альберт Энштейн]\033[0m\n-Довольно слов!\n", "Прокричал седой деятель-гуманист\n",
                                 "\033[34m[Альберт Энштейн]\033[0m\n-Если действительно хочешь вымолить мою пощаду, реши задачу на тему расчет количества теплоты!\n",
                                 ""]
    replics_decision1_2_true = [
        "Вы пытаетесь увернуться от снаряда РПГ, однако у Вас это не выходит, и зловещий снаряд, усиляемый эффектом Манро, низводит Вас до атомов\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Тебя уничтожила сила научных исследований, щенок!\n",
        "Усмехнулся гений преклонного возраста\n",
        "Игра закончена. Вы мертвы. Плохая концовка\n",
        ";;::loc;:ldxxO00000KXNNNWNK0OxdoooddxkOKNNXXNNNNNXXX0OKKOkOkc,,,,''.''.....\ncc:cloddodkkkO0KKKXXNNNXK0Oxxdl;,;,;clok000O0KKXXXXXKXXK000d:;;;,,;;;'',,,,\nlloooodxkkkO00KXXXXKOkxdooc:;;:;,'',::clldxdddkOOO0KKKKKKKkxdllcloddocclc::\nllodxxkkOO00KXXXX0dc:::::;;'..';;'.'',;::lcc::codxxdddxkOKKKK000OOkkkxdocc:\nloodxk00000KXKOkdc,'''''',,,...',,..'.';;::;;,,:llc:;;coxO0KXXXK000Okxdolll\nooddxkOKXXXOxolc:,..'''''''''...''..''':c:;;::;;;:c:;;;:lk000KKKK00OOkxxddo\ndddxxook0Oo:'......''....',,;,',',;,,,,cc,,;;cc;,,;:;;;:cdkOkkO0KK000OOkkkx\nxxxxkkxxo:'..... ..'.....';:ccc:;::;:::::;,;;clc;,;;;::::ccloddkOKKK0OOkkkx\nkkkkOOOd;,..............',,,:llclc:ldxdddl;;;:llc::::::::::cllodxkOO00Okkkk\nOO000000d,..........''..';,,,;clddddxxxddkd:;:loolllccc::;;::ccllodx00000Ok\nO00000K0l....'.......'''';c::ccllxxxxxkkxxxdodxkxdoooolc::::::::clox0K000Ok\nkOOkkO0k;.....'........';:llldddxkkOOkO0K0000KKOxdddddoloolcc::ccclx00000OO\n000OO00d,.....''..',,..':doldxooxxdxkkkO00KK0KKOOkkkkxxkOkdodxdodxkO00KK000\n0K0kkkxd;.....;c:,:clc;;cdxkxdddxOkxdddxk0KK0000OkOKKKKXKKKKKKOkdoloOXKKKK0\nK0o,'.........'ldxxxocclldkkxxkkOKX0xxxkkOO000O0KOO0KKKKKKK0kxxdoc;;dKKKKKK\nOl,..........'''',coccxkxdxkxkKKXXNNK0OOOOOKKK00OO0XXKK0OkkxxkO0Oxodddld0KK\n:'..........,::::;:ccdOxoox0OO00XNWWNXXXXKKXXKK0kOKXXNX0kxO0000Oxdo:'..,cx0\n,'.............,;cllloxddxO0XXKKXNWWWWWNNXKXXXXKKKKKKXXK0KKKK0kdol:,...',;d\nc'..............,:lodoodxxxk0XXNNWWWWWWWWNNNNNNNNXXXXXXXK0OOO0xl:;'....'';d\nd,............':odddoodkOkOOk0XNNNWWWWWWWWWNNNNXXXXXXK0OOOkooddll:,'.'',ckK\nKd,...........,::::clcclodO00KXXXXKKKXXXNNNNNNXXNNNXK0kkxxl::::;::;,,,;ckKX\nX0dlc;..........';::;,',:dk0KKKXXKKKXXXNNNNNXXXKKXXNK0Okddol:;;;;;;:cdkKXXX\nXK0KX0d,......':c;''.',:cloxxkO000K000KK0KK0OOkkxkOKKXX0Okkoc:;,,,;;cd0XXXX\nXXXXXXo'.....'::'..,;,,,'':cccllllcclllddddolodocllldkOkOkxolc:,,,,:dOXXXXX\nXXXXXXx,......''..',,.....;;''......,,,,;clc::cccc;;;:;:cloolloc:::lOXXNXXX\nXXXXXXKkc,........''......''............',;:,:cclc;::,',;::::::cllllx0KKKXX\nXXXXXXXKd,................'...........'',::,',::c;;:;,,::;,;:;,',;:lOXXKKKK\nX0OKXXXKkl,.......'......',''...''',,,;:::;,,,;;,,;,,;;,,....''',,,lOXXXXXX\nddkKXXNNX0xc'..........''''''''''',,;::cclo::;,,,;;;:;'.......',,;;oKXXXXXX\n0XNXXXXXXNNO:,:ll;''......''',,;;;;:ccccoO0xo:;;;;::'........'';codOXXXXXXX\nXXXXXXXXXXXX0k0XXx:''......',;::lddddxddx0Kkxo:;:;;;,,:lc,',coddOXXXXXXXKXX\nXXXXXKKXXNXNXXXKKKOo:;,,''..;lddxK0kkOkkOKKOkollc;,;;:ddlloldKNXXXNKKXXXXXX\nXXXXX0KXKXXXXKKXXXNXOc;cc:,;;lOK0KK00K000KK0xoodl;::;dKK0KXKKNNXXXNXXXXXXXX\nXXXXXXXXXXXXXXNXK0XXKkdooc;cod0KKKKXXXXXKKK0Ooc::;;,;x0KXNNNKKXXXNNXXXXXXXX\nXXXXXXXXXXXXXXNXkOXXKOoc:;;:d0OkkOKOocxK0Okxko:,,,'';oO0XNNXKKXNXNNNNNXXXXX\nXXXXXXXXNK0XNXNXXXXXKko:;;:oOOkxxk0x:,oKOxxxdl:;,'.';lkKNNNXXNNXXXXXXXXXXXX\nXXXXXXXXXXXNNNXXXKOOkxo:,,cxkkkk0Ol,.',oOOxoccloc'.',;lkKXXXXXXNXXXXXXXXXXX\nXXXXXXXXXXXNXXX0Okl;,''';cddookOO0o.   ,xOxol::;:;....';ldk0KXXXXXXNXKXXXXX\nXXXKKK00Okkdlllc;;,'...,lollclxOOOO;...ckOxc::c:;'.......';clodxxkkOOO000KK\nkkkxxddolc:;,,,''''''..,::lddooxxxxc,;:lddoloolloc;,'..'''.'''',,;;;:::clll\nxxdddddddolccllllcccc::cclxxxxddodkdccllllllcccldxdoc::clc:;;;;;;;:::::::::"
        #"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
    ]
    if flag == True:
        chapter_counter += 1
        print(f"\n\nГлава {chapter_counter}:----------------------Дуэль с ученым----------------------\n\n")
        for replic in replics_decision1_2_true:
            if replic != replics_decision1_2_true[-1]:
                spellreplic(replic)
            else:
                print(replic + '\n')
        spellreplic('Вы разблокировали концовку: "Now I Am Become Death, the Destroyer of Worlds."\n')
        achievements.add('Now I Am Become Death, the Destroyer of Worlds.\n')
        check_for_platinum(achievements)
        wannaretry()
        return
    else:
        print("\n\nГлава_3:Примирение?________________________________________________\n\n")
        for replic in replics_decision1_2_false:
            spellreplic(replic)
        flag1_2 = False

        while True:
            reply = replicinput(file,
                "Перед Вами стоит стоит непростой выбор:\n1) Согласиться решать задачу\n2) Не согласиться решать задачу\n/Введите номер вашего выбора: ")
            if reply == "1":
                break
            elif reply == "2":
                flag1_2 = True
                break
            else:
                pass

    decision1_3(flag1_2, nickname, chapter_counter)


def decision1_3(flag, nickname, chapter_counter):
    replics_decision1_3_false = ["Рука Альберта снова лезет за пазуху\n",
                                 f"\033[31m[Вы]\033[0m\n-Нет! Пожалуйста, не доставайте базуку РПГ\n", "Жалобно проскулили Вы\n",
                                 f"\033[34m[Альберт Энштейн]\033[0m\n-Успокойтесь, {nickname}, я всего-лишь хочу найти предварительно распечатанную на принтере для Вас задачу\n",
                                 "Старик достает листочек с задачей и протягивает её Вам\n",
                                 "Вы приступаете к чтению спасительной задачи\n",
                                 "Рассчитайте количество теплоты, необходимое для нагревания 10 кг воды на 50 градусов Цельсия\n",
                                 f"[Ваши мысли]\n-Помню, в школе нам говорили, что теплоемкость воды равна 4200 Дж/(кг*C)\n-Хммм... не могу вспомнить формулу количества теплоты....\n-А, точно, количество теплоты равно массе тела, умноженной на теплоемкость данного тела, умноженной на изменение температуры этого же тела.\nВыходит, надо просто перемножить 4200, 10 и 50.",
                                 f"\033[34m[Альберт Энштейн]\033[0m\n-{nickname}, пришло время давать ответ\n",
                                 "Разразился как гром в ясную погоду голос старца\n"]
    replics_decision1_3_true = [f"\033[31m[Вы]\033[0m\n-Я не собираюсь решать твои никчемные задачки, старец\n",
                                "Не успели вы договорить, как увидели снаряд, летящий в вашем направлении. Видимо старик успел достать базуку обратно и произвести выстрел\n",
                                "Вы пытаетесь увернуться от снаряда РПГ, однако у Вас это не выходит, и зловещий снаряд, усиляемый эффектом Манро, низводит Вас до атомов\n",
                                "\033[34m[Альберт Энштейн]\033[0m\n-Тебя уничтожила сила научных исследований, щенок!\n",
                                "Усмехнулся гений преклонного возраста\n",
                                ";;::loc;:ldxxO00000KXNNNWNK0OxdoooddxkOKNNXXNNNNNXXX0OKKOkOkc,,,,''.''.....\ncc:cloddodkkkO0KKKXXNNNXK0Oxxdl;,;,;clok000O0KKXXXXXKXXK000d:;;;,,;;;'',,,,\nlloooodxkkkO00KXXXXKOkxdooc:;;:;,'',::clldxdddkOOO0KKKKKKKkxdllcloddocclc::\nllodxxkkOO00KXXXX0dc:::::;;'..';;'.'',;::lcc::codxxdddxkOKKKK000OOkkkxdocc:\nloodxk00000KXKOkdc,'''''',,,...',,..'.';;::;;,,:llc:;;coxO0KXXXK000Okxdolll\nooddxkOKXXXOxolc:,..'''''''''...''..''':c:;;::;;;:c:;;;:lk000KKKK00OOkxxddo\ndddxxook0Oo:'......''....',,;,',',;,,,,cc,,;;cc;,,;:;;;:cdkOkkO0KK000OOkkkx\nxxxxkkxxo:'..... ..'.....';:ccc:;::;:::::;,;;clc;,;;;::::ccloddkOKKK0OOkkkx\nkkkkOOOd;,..............',,,:llclc:ldxdddl;;;:llc::::::::::cllodxkOO00Okkkk\nOO000000d,..........''..';,,,;clddddxxxddkd:;:loolllccc::;;::ccllodx00000Ok\nO00000K0l....'.......'''';c::ccllxxxxxkkxxxdodxkxdoooolc::::::::clox0K000Ok\nkOOkkO0k;.....'........';:llldddxkkOOkO0K0000KKOxdddddoloolcc::ccclx00000OO\n000OO00d,.....''..',,..':doldxooxxdxkkkO00KK0KKOOkkkkxxkOkdodxdodxkO00KK000\n0K0kkkxd;.....;c:,:clc;;cdxkxdddxOkxdddxk0KK0000OkOKKKKXKKKKKKOkdoloOXKKKK0\nK0o,'.........'ldxxxocclldkkxxkkOKX0xxxkkOO000O0KOO0KKKKKKK0kxxdoc;;dKKKKKK\nOl,..........'''',coccxkxdxkxkKKXXNNK0OOOOOKKK00OO0XXKK0OkkxxkO0Oxodddld0KK\n:'..........,::::;:ccdOxoox0OO00XNWWNXXXXKKXXKK0kOKXXNX0kxO0000Oxdo:'..,cx0\n,'.............,;cllloxddxO0XXKKXNWWWWWNNXKXXXXKKKKKKXXK0KKKK0kdol:,...',;d\nc'..............,:lodoodxxxk0XXNNWWWWWWWWNNNNNNNNXXXXXXXK0OOO0xl:;'....'';d\nd,............':odddoodkOkOOk0XNNNWWWWWWWWWNNNNXXXXXXK0OOOkooddll:,'.'',ckK\nKd,...........,::::clcclodO00KXXXXKKKXXXNNNNNNXXNNNXK0kkxxl::::;::;,,,;ckKX\nX0dlc;..........';::;,',:dk0KKKXXKKKXXXNNNNNXXXKKXXNK0Okddol:;;;;;;:cdkKXXX\nXK0KX0d,......':c;''.',:cloxxkO000K000KK0KK0OOkkxkOKKXX0Okkoc:;,,,;;cd0XXXX\nXXXXXXo'.....'::'..,;,,,'':cccllllcclllddddolodocllldkOkOkxolc:,,,,:dOXXXXX\nXXXXXXx,......''..',,.....;;''......,,,,;clc::cccc;;;:;:cloolloc:::lOXXNXXX\nXXXXXXKkc,........''......''............',;:,:cclc;::,',;::::::cllllx0KKKXX\nXXXXXXXKd,................'...........'',::,',::c;;:;,,::;,;:;,',;:lOXXKKKK\nX0OKXXXKkl,.......'......',''...''',,,;:::;,,,;;,,;,,;;,,....''',,,lOXXXXXX\nddkKXXNNX0xc'..........''''''''''',,;::cclo::;,,,;;;:;'.......',,;;oKXXXXXX\n0XNXXXXXXNNO:,:ll;''......''',,;;;;:ccccoO0xo:;;;;::'........'';codOXXXXXXX\nXXXXXXXXXXXX0k0XXx:''......',;::lddddxddx0Kkxo:;:;;;,,:lc,',coddOXXXXXXXKXX\nXXXXXKKXXNXNXXXKKKOo:;,,''..;lddxK0kkOkkOKKOkollc;,;;:ddlloldKNXXXNKKXXXXXX\nXXXXX0KXKXXXXKKXXXNXOc;cc:,;;lOK0KK00K000KK0xoodl;::;dKK0KXKKNNXXXNXXXXXXXX\nXXXXXXXXXXXXXXNXK0XXKkdooc;cod0KKKKXXXXXKKK0Ooc::;;,;x0KXNNNKKXXXNNXXXXXXXX\nXXXXXXXXXXXXXXNXkOXXKOoc:;;:d0OkkOKOocxK0Okxko:,,,'';oO0XNNXKKXNXNNNNNXXXXX\nXXXXXXXXNK0XNXNXXXXXKko:;;:oOOkxxk0x:,oKOxxxdl:;,'.';lkKNNNXXNNXXXXXXXXXXXX\nXXXXXXXXXXXNNNXXXKOOkxo:,,cxkkkk0Ol,.',oOOxoccloc'.',;lkKXXXXXXNXXXXXXXXXXX\nXXXXXXXXXXXNXXX0Okl;,''';cddookOO0o.   ,xOxol::;:;....';ldk0KXXXXXXNXKXXXXX\nXXXKKK00Okkdlllc;;,'...,lollclxOOOO;...ckOxc::c:;'.......';clodxxkkOOO000KK\nkkkxxddolc:;,,,''''''..,::lddooxxxxc,;:lddoloolloc;,'..'''.'''',,;;;:::clll\nxxdddddddolccllllcccc::cclxxxxddodkdccllllllcccldxdoc::clc:;;;;;;;:::::::::"
                                #"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
                                ]

    if flag == False:
        chapter_counter += 1
        print(f"\n\nГлава {chapter_counter}:----------------------Что ожидать от мудреца?----------------------\n\n")
        for replic in replics_decision1_3_false:
            spellreplic(replic)
        flag1_3 = False
        attempt_counter = 1
        while True:
            if attempt_counter == 1:
                reply = replicinput(file, "/Введите ваш ответ в Джоулях: ")
            else:
                reply = replicinput(file,
                    "\033[34m[Альберт Энштейн]\033[0m\n-Ответ неверный! У тебя осталась последняя попытка\n/Введите ваш ответ в Джоулях: ")
            if reply != "2100000" and attempt_counter == 2:
                flag1_3 = True
                break
            elif reply == "2100000":
                break
            else:
                attempt_counter += 1

    else:
        chapter_counter += 1
        print(f"\n\nГлава {chapter_counter}:----------------------Коллапс с Энштейном----------------------\n\n")
        for replic in replics_decision1_3_true:
            spellreplic(replic)
        return

    decision1_4(flag1_3, nickname, chapter_counter)


def decision1_4(flag, nickname, chapter_counter):
    replics_decision1_2_false = [
        f"\033[34m[Альберт Энштейн]\033[0m\n-Хорошо, {nickname}, молодец. Порадовал. У тебя действительно доброе сердце\n",
        "[Ваши мысли]\n-Наверное стоит у него спросить, что вообще тут происходит\n"]
    replics_decision1_2_true = ["Старик достаёт базуку обратно и производит прицельный выстрел\n",
                                "Вы пытаетесь увернуться от снаряда РПГ, однако у Вас это не выходит, и зловещий снаряд, усиляемый эффектом Манро, низводит Вас до атомов\n",
                                "\033[34m[Альберт Энштейн]\033[0m\n-Тебя уничтожила сила научных исследований, щенок!\n",
                                "Усмехнулся гений преклонного возраста\n",
                                "Игра закончена. Вы мертвы. Плохая концовка\n",
                                ";;::loc;:ldxxO00000KXNNNWNK0OxdoooddxkOKNNXXNNNNNXXX0OKKOkOkc,,,,''.''.....\ncc:cloddodkkkO0KKKXXNNNXK0Oxxdl;,;,;clok000O0KKXXXXXKXXK000d:;;;,,;;;'',,,,\nlloooodxkkkO00KXXXXKOkxdooc:;;:;,'',::clldxdddkOOO0KKKKKKKkxdllcloddocclc::\nllodxxkkOO00KXXXX0dc:::::;;'..';;'.'',;::lcc::codxxdddxkOKKKK000OOkkkxdocc:\nloodxk00000KXKOkdc,'''''',,,...',,..'.';;::;;,,:llc:;;coxO0KXXXK000Okxdolll\nooddxkOKXXXOxolc:,..'''''''''...''..''':c:;;::;;;:c:;;;:lk000KKKK00OOkxxddo\ndddxxook0Oo:'......''....',,;,',',;,,,,cc,,;;cc;,,;:;;;:cdkOkkO0KK000OOkkkx\nxxxxkkxxo:'..... ..'.....';:ccc:;::;:::::;,;;clc;,;;;::::ccloddkOKKK0OOkkkx\nkkkkOOOd;,..............',,,:llclc:ldxdddl;;;:llc::::::::::cllodxkOO00Okkkk\nOO000000d,..........''..';,,,;clddddxxxddkd:;:loolllccc::;;::ccllodx00000Ok\nO00000K0l....'.......'''';c::ccllxxxxxkkxxxdodxkxdoooolc::::::::clox0K000Ok\nkOOkkO0k;.....'........';:llldddxkkOOkO0K0000KKOxdddddoloolcc::ccclx00000OO\n000OO00d,.....''..',,..':doldxooxxdxkkkO00KK0KKOOkkkkxxkOkdodxdodxkO00KK000\n0K0kkkxd;.....;c:,:clc;;cdxkxdddxOkxdddxk0KK0000OkOKKKKXKKKKKKOkdoloOXKKKK0\nK0o,'.........'ldxxxocclldkkxxkkOKX0xxxkkOO000O0KOO0KKKKKKK0kxxdoc;;dKKKKKK\nOl,..........'''',coccxkxdxkxkKKXXNNK0OOOOOKKK00OO0XXKK0OkkxxkO0Oxodddld0KK\n:'..........,::::;:ccdOxoox0OO00XNWWNXXXXKKXXKK0kOKXXNX0kxO0000Oxdo:'..,cx0\n,'.............,;cllloxddxO0XXKKXNWWWWWNNXKXXXXKKKKKKXXK0KKKK0kdol:,...',;d\nc'..............,:lodoodxxxk0XXNNWWWWWWWWNNNNNNNNXXXXXXXK0OOO0xl:;'....'';d\nd,............':odddoodkOkOOk0XNNNWWWWWWWWWNNNNXXXXXXK0OOOkooddll:,'.'',ckK\nKd,...........,::::clcclodO00KXXXXKKKXXXNNNNNNXXNNNXK0kkxxl::::;::;,,,;ckKX\nX0dlc;..........';::;,',:dk0KKKXXKKKXXXNNNNNXXXKKXXNK0Okddol:;;;;;;:cdkKXXX\nXK0KX0d,......':c;''.',:cloxxkO000K000KK0KK0OOkkxkOKKXX0Okkoc:;,,,;;cd0XXXX\nXXXXXXo'.....'::'..,;,,,'':cccllllcclllddddolodocllldkOkOkxolc:,,,,:dOXXXXX\nXXXXXXx,......''..',,.....;;''......,,,,;clc::cccc;;;:;:cloolloc:::lOXXNXXX\nXXXXXXKkc,........''......''............',;:,:cclc;::,',;::::::cllllx0KKKXX\nXXXXXXXKd,................'...........'',::,',::c;;:;,,::;,;:;,',;:lOXXKKKK\nX0OKXXXKkl,.......'......',''...''',,,;:::;,,,;;,,;,,;;,,....''',,,lOXXXXXX\nddkKXXNNX0xc'..........''''''''''',,;::cclo::;,,,;;;:;'.......',,;;oKXXXXXX\n0XNXXXXXXNNO:,:ll;''......''',,;;;;:ccccoO0xo:;;;;::'........'';codOXXXXXXX\nXXXXXXXXXXXX0k0XXx:''......',;::lddddxddx0Kkxo:;:;;;,,:lc,',coddOXXXXXXXKXX\nXXXXXKKXXNXNXXXKKKOo:;,,''..;lddxK0kkOkkOKKOkollc;,;;:ddlloldKNXXXNKKXXXXXX\nXXXXX0KXKXXXXKKXXXNXOc;cc:,;;lOK0KK00K000KK0xoodl;::;dKK0KXKKNNXXXNXXXXXXXX\nXXXXXXXXXXXXXXNXK0XXKkdooc;cod0KKKKXXXXXKKK0Ooc::;;,;x0KXNNNKKXXXNNXXXXXXXX\nXXXXXXXXXXXXXXNXkOXXKOoc:;;:d0OkkOKOocxK0Okxko:,,,'';oO0XNNXKKXNXNNNNNXXXXX\nXXXXXXXXNK0XNXNXXXXXKko:;;:oOOkxxk0x:,oKOxxxdl:;,'.';lkKNNNXXNNXXXXXXXXXXXX\nXXXXXXXXXXXNNNXXXKOOkxo:,,cxkkkk0Ol,.',oOOxoccloc'.',;lkKXXXXXXNXXXXXXXXXXX\nXXXXXXXXXXXNXXX0Okl;,''';cddookOO0o.   ,xOxol::;:;....';ldk0KXXXXXXNXKXXXXX\nXXXKKK00Okkdlllc;;,'...,lollclxOOOO;...ckOxc::c:;'.......';clodxxkkOOO000KK\nkkkxxddolc:;,,,''''''..,::lddooxxxxc,;:lddoloolloc;,'..'''.'''',,;;;:::clll\nxxdddddddolccllllcccc::cclxxxxddodkdccllllllcccldxdoc::clc:;;;;;;;:::::::::"
                                #"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
     ]
    if flag == True:
        for replic in replics_decision1_2_true:
            if replic != replics_decision1_2_true[-1]:
                spellreplic(replic)
            else:
                print(replic + '\n')
        spellreplic('Вы разблокировали концовку: "Now I Am Become Death, the Destroyer of Worlds."\n')
        achievements.add('Now I Am Become Death, the Destroyer of Worlds.\n')
        check_for_platinum(achievements)
        wannaretry()
    else:
        # тут надо флаг добавить
        for replic in replics_decision1_2_false:
            spellreplic(replic)
        decision1_1(True,nickname, chapter_counter)

#######################

def chapter_cringepoyavlenie(nickname, chapter_counter):
    chapter_counter += 1
    print(f"\n\nГлава {chapter_counter}:----------------------Неловкое молчание----------------------\n\n")
    start_of_chapter = [
        "Вы находите себя в каком-то непонятном помещении, похожем на казино\n",
        f"[Ваши мысли]\n-Что? Как меня перенесли в это место?\n",
        "Вы хлопаете по карманам и ощущаете присутствие 113 рублей\n",
        "\033[35m[Крупье]\033[0m\n-Эй Вы... Вы планируете играть~с? Иначе я буду вынужден угрожать Вам~с выдворением из данного заведения!\n",
    ]
    for replic in start_of_chapter:
        spellreplic(replic)
    money = 113
    tries = 0
    #spellreplic("/Введите номер вашего выбора: ")
    casinoflag = replicinput(file, "Перед Вами стоит стоит непростой выбор:\n1) Сесть за рулетку\n2) Уйти из казино\n/Введите номер вашего выбора: ")
    while casinoflag != True and casinoflag != False:
        if casinoflag == '1':
            casinoflag = False

        elif casinoflag == '2':
            casinoflag = True
        else:
            casinoflag = replicinput(file, "Перед Вами стоит стоит непростой выбор:\n1) Сесть за рулетку\n2) Уйти из казино\n/Введите номер вашего выбора: ")
    if casinoflag == False:
        spellreplic("\033[31m[Вы]\033[0m\n-Да, я буду играть, все равно один раз живём!\n")
        while money > 0 and casinoflag == False:
            choice = ''
            while choice.isdigit() == False or (int(choice) != 1 and int(choice) != 2 and int(choice) != 3):
                choice = replicinput(file, "\033[35m[Крупье]\033[0m\nВыбирайте~с, красное, черное или может... зеленое?\n1) Красное\n2) Черное\n3) Зеленое\n/Введите номер вашего выбора: ")
            colours = ['', 'Красное', 'Черное', 'Зеленое']
            colour = colours[int(choice)]
            money, tries, casinoflag = casino(money, tries, casinoflag, colour)
    street(nickname, money, chapter_counter)

def casino(money, tries, casinoflag, colour):
    replics_if_won = [
        '\033[35m[Крупье]\033[0m\n-Вижу, сегодня ваш день~с. Продолжайте в том же духе!\n',
        '\033[35m[Крупье]\033[0m\n-Вау, я вижу, вы продолжаете выигрывать~с. Как говорится: хорошему игроку всегда везёт!\n',
        '\033[35m[Крупье]\033[0m\n-Вы только посмотрите: этот человек собирается разорить наше казино! Хе-хе-хе, вы что, я же шучу~с.\n',
        '\033[35m[Крупье]\033[0m\n-Статистика показывает~с, что 99% лудоманов перестают играть прямо перед джекпотом~с. Вижу~с, это не ваш случай\n'
    ]
    replics_if_lost = [
        'Улыбка на вашем лице сменяется гримасой отчаяния - вы проиграли все.\n',
        '\033[35m[Крупье]\033[0m\n-М-да... Похоже, вам не повезло. Ну что-ж, как говорится: тот, кто всегда в выигрыше, — не настоящий игрок. Ведь так~с?\n'
        '\033[31m[Вы]\033[0m\n-Нет, погодите, я еще смогу отыграться! Только дайте...\n',
        'Вы не успеваете договорить, как два амбала хватают вас под мышки\n',
        'Прямо перед тем, как вылететь из входной двери, вы успеваете разгледеть на лице крупье ехидную ухмылку\n'
    ]
    wheel_spinning = 'Крупье запускает колесо. Вы наблюдаете как шарик часто отсткакивает от поверхности барабана...\nКолесо замедляется... И вы видете как шарик выпадает на...\n'
    hit = randint(0, 101) #случайное число которое "выкидывает" игрок
    needed_result = tries * 25 #определяем необходимый результат по принципу 'чем дольше играет тем больше шанс что проиграет'
    needed_result_for_green = 80 #на зеленое шанс всегда одинаковый
    tries += 1
    if colour == 'Зеленое' and hit >= needed_result_for_green: #выигрыишь если повезло на зеленом
        money = money * 10
        spellreplic(wheel_spinning + 'Зеленое!!!\n')
        spellreplic('\033[35m[Крупье]\033[0m\n-Милосердный господь! Да вы везунчик~с!\n')
        spellreplic(f'Вы поставили все свои деньги на зеленое и их количество возросло в 10 раз.\nВаш баланс: {money}\n')
        #вообще разницы выбрал ли человек красное или черное никакой нет кроме того что выводится в консоль но шанс все равно тот же
    elif (colour == 'Красное' or colour == 'Черное') and hit >= needed_result: #выигрышь если выбрал красное или черное
        money = money * 2
        spellreplic(wheel_spinning + colour + '!!!')
        spellreplic(replics_if_won[tries-1])
        spellreplic(f'Вы поставили все свои деньги и скоропостижно получили Х2 от своей суммы.\nВаш баланс: {money}\n')
        while True:
            casinodecision = replicinput(file, "\n1) Играть ещё раз\n2) Уйти из казино\n/Введите номер вашего выбора: ")
            if casinodecision == '1':
                return money, tries, casinoflag
            elif casinodecision == '2':
                casinoflag = True
                return money, tries, casinoflag
            else:
                pass
    else: #проигрышь
        if colour == 'Красное':
            colour = 'Черное'
        else:
            colour = 'Красное'
        spellreplic(wheel_spinning + colour + '...')
        money = 0
        casinoflag = True
        for replic in replics_if_lost:
            spellreplic(replic)
        #spellreplic("Вы с позором проиграли все свои денежные средства и вынуждены  уйди из казино.\n")
        return money, tries, casinoflag #продолжаем

def street(nickname, money, chapter_counter):
    street_replics = [
        "Вы оказываетесь на улице\n",
        "Там вы замечаете плачущего человека, оперевшегося на перила ступенек, ведущих к манящей двери казино\n",
        "\033[36m[Плачущий человек]\033[0m\n-Хватит пялиться на меня!\n",
        "Гаркнул плакса\n",
        "Вы пошатнулись\n",
        "\033[36m[Плачущий человек]\033[0m\n-Ты все равно не в силах понять моего горя... Я проиграл последние 86 рублей!\n",
        "Человек продолжил плакать\n",
        "\033[31m[Вы]\033[0m\n-Думаю, его лучше не беспокоить... Или все-таки стоит? Вдруг он даст ценный лут...\n"
    ]

    for replic in street_replics:
        spellreplic(replic)

    crying_flag = False
    while True:
        reply1 = replicinput(file,
            "Перед Вами стоит стоит непростой выбор:\n1) Побеспокоить\n2) Пройти мимо\n/Введите номер вашего выбора: ")
        if reply1 == "1":
            break
        elif reply1 == "2":
            crying_flag = True
            break
        else:
            pass
    crying_man(nickname, crying_flag, money, chapter_counter)

def crying_man(nickname, crying_flag, money, chapter_counter):
    helped_crying_man = False
    replics_true = [
        "Вы решаете не трогать бедолагу, и проходите мимо\n",
        "По мере удаления от незнакомца вы замечаете, что сзади, в кармане его скинни джинсов, торчит блестящий на солнце смертоносный пеголь\n",
        "[Ваши мысли]\n-Фуух, пронесло. Было бы плохо, если бы меня застрелили из пеголя. Как хорошо, что мной было принято решение пройти мимо.\n"
    ]
    replics_false_and_no_money = [
        "\033[31m[Вы]\033[0m\n-Не плачь, дорогой незнакомец. Мной только что было проиграно намного больше тебя, так что твоё горе ничего не стоит\n",
        "Человек отвечает, закрыв лицо руками\n",
        "\033[36m[Плачущий человек]\033[0m\n-Тебе лучше убираться отсюда, пока ты при памяти!\n",
        "Вы замечаете что-то блестящее в заднем кармане его скинни джинсов. Возможно, это ключи от чего-то ценного\n"]
    replics_false_and_have_money = [
        f"\033[31m[Вы]\033[0m\n-Не плачь, дорогой незнакомец. Лучше порадуйся за меня, теперь у меня в кармане {money} денег\n",
        "Человек отвечает, закрыв лицо руками\n",
        "\033[36m[Плачущий человек]\033[0m\n-Тебе лучше убираться отсюда, пока ты при памяти!\n",
        "Вы замечаете что-то блестящее в заднем кармане его скинни джинсов. Возможно, это ключи от чего-то ценного\n"
    ]
    replics_pistol_death_ending = [
        "Плачущий человек достаёт пеголь и шмаляет по Вам\n",
        "Игра закончена. Вы мертвы. Плохая концовка\n",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXKOdkXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXX0O0d. .lXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNX00000OOOl'. .oNWWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWNWWNWWNNXOO0KXXKK0O0XOl.'kNWWWWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNKk0KKXXKXXK0kdON0c:dkXWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWNNWWWKk000K0koclxOK0lxNKkkdokKWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWNNNkOX0KOo'   .cxKxc0NxxXKxdxkKNNNWWWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nNNNNNNNNNNNNNNNNNNNNNNNNNNNWKxKK00O:     ,d0x:0Wd.,lOXOxxxOXWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNWOxXK0X0d:'..;lkOcoNNl   .;dk00kxOXWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNWOd0K0NNKOOkkOOKolKN0, 'oc,. .;d0OkOKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNXOxx0NNNWNNNWNx:ONNd,cONNXo..  .cxkOOKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNWNOdONNXKXNWNOcdKkl'lNNNNNK0kooc;:odxxx0XNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN0dOOl;,;l0Kclxl:,'';lxKNNXNNNNK0K0xc;d00KNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN0xx:.....clcxlcc::cccccldk0NNXNNNNNk:lxxxkk0NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN0xko,...,,:dxKNKkdc:;;c,..'dXNXNNNNNX0Odll:cx0KNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNXNNNNXkxOd::;:colc:cok0NO' 'lc;,,oOKNNNNNNNNXOl,,;:oOKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNXNNNNNKOkdc:cccccl'   .'',cxNNXK0kxddxk0XNNNNKo;;,'',:d0XNNXNXNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNXXXXXXXXXXXXXXXXXNXXNXXNNXKOkxo:;:,..  ..,ok0NNXXNNNNKOkxkxkOXk:;;'.:l''dKNNXNNXNXXXXXXXXXXXXXXXNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNXNNXXNNNNNNNNNNXOc;;'''.',ccoKNNNNXXNXXXNNXk;.:c,,'..do.,kXNXXNXXXNNNNNNNNNNNNNNNNNNNNN\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0kdlc;,,::',coolokKNNXXXNK: 'kx;,'.'o:.oXNNXXXNXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKklod:,,.. ..'...l0XNXXx. oKkkOxoc'.,o0XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0xOkc:::'   ..',,,coodkd.,Ox:oxox0l. ,kXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK0OOOkkx::xkxl'....,dko;',::;;cl'    .,,,;lkKXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0odOdc'. .lOOxo:'.':kdcoO0kc..,,,,:;...;lokXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0kd:''',:lllodl'';:;:OKOxl,.    'l:''.'lxdkKXXXKXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKXXKXXKKKKKKKKOxl:;,',;..:ooc:'      ..    .lOdlkXXXXKKXXXXXXXXXXXXXXXXXXXXXX\nKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXKKKKKKKOkOxl;'.'.  c0x;.''',:cll:.    .cllkKXKKXXXXXXXXXXXXXXXXXXXXXXXXX\nKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKxkKKKx:,..  ';.     .';:;;;,'. .:ldKKKKKKXKKKKKKKKKKKKKKKKKKKKKKK\nKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKxkKKKKd'..'''...',',:ol'..',,'';;;lx0KKKKKKKKKKKKKKKKKKKKKKKKKKKK\nKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOodkOKk;'lkkdl'.'.   .        .lOkdoOKKKKKKKKKKKKKKKKKKKKKKKKKKKK\nKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkxkxoooxO0Kxlo'     .....';'  .,ldk0KK0KK00KKKKKKKKKKKKKKKKKKKKKK\n00000000000000000000000000000000000000000000KOddk0koc:cl:'....'.';cc;,'',,',:oOK000000000000000000000000000000\n0000000000000000000000000000000000000000000000dcodooxd,.','';;,;:,,.     .',;ckK000000000000000000000000000000\n000000000000000000000000000000000000000000000Odd0Od,;xo;'..,:,... ......'loodx00000000000000000000000000000000\nOOOOOOO000000000000000000000000000000000000000OxxO0x;,lo;.....',;::;;;,,,;lxO000000000000000000000000000000000\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkdxd;.;lllllc:;'..   ...':coOO00OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOxo:';clodl,......',:clodoxOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOxdddoodddoooodddddxxxkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkOkkkkOOOOOOOOOkkOOOOOOOkkOOkOkkOOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\nkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
    ]
    replic_golding_hand = [
        "\033[31m[Вы]\033[0m\n-Протяни свои руки\n",
        "Плачущий человек протягивает Вам руки\n"
    ]
    replic_spit = [
        "Вы плюёте бедолаге в полные надежды руки\n",
        "\033[31m[Вы]\033[0m\n-Нечего было проигрывать! В следующий раз будешь думать осмотрительнее\n"
    ]
    replics_donate = [
        "\033[36m[Плачущий человек]\033[0m\n-Спасибо, добрый человек. Если ты когда-то попадёшь в заварушку\n",
        "Плакса достаёт из заднего кармана скинни джинсов пеголь и прокручивает его как реву\n",
        "\033[36m[Плачущий человек]\033[0m\n-Я накормлю твоих недругов свинцом\n",
        "[Ваши мысли]\n-Видимо он имеет ввиду пули...\n",
        "[Ваши мысли]\n-Как хорошо, что мной было принято решение пожертвовать этому незнакомцу деньги. Было бы плохо, если бы меня застрелили из пеголя.\n",
        "Вы покидаете незнакомца и растворяетесь в горизонте\n"
    ]
    if crying_flag == True: #реплики если вы решили пройти мимо бедного
        for replic in replics_true:
            spellreplic(replic)
        keep_walking(nickname, money, helped_crying_man, chapter_counter)  # Вы продолжаете свой путь, идя куда глаза глядят
    elif crying_flag == False and money == 0:#если вас облапошили и нет денек вообще
        for replic in replics_false_and_no_money:
            spellreplic(replic)
        while True:
            crying_reply = replicinput(file,
                "Перед Вами стоит стоит непростой выбор:\n1) Продолжить беспокоить\n2) Пройти мимо\n/Введите номер вашего выбора: ")
            if crying_reply == "1":
                crying_reply = False
                break
            elif crying_reply == "2":
                crying_reply = True
                break
            else:
                pass
        if crying_reply == True:
            keep_walking(nickname, money, helped_crying_man, chapter_counter)  # Вы продолжаете свой путь, идя куда глаза глядят
        else:
            spellreplic("\033[31m[Вы]\033[0m\n-В данной ситуации скорее ты должен меня успокаивать, ведь мною было проиграно больше денег, а именно 113 рублей, что на 27 рублей больше твоего\n")
            for replic in replics_pistol_death_ending:
                if replic != replics_pistol_death_ending[-1]:
                    spellreplic(replic)
                else:
                    print(replic + '\n')
            spellreplic('Вы разблокировали концовку: "Сынок, у тебя через два дня день рождения, мы с мамой вот задумались серьезно, что бы тебе подарить..."\n')
            achievements.add('Сынок, у тебя через два дня день рождения, мы с мамой вот задумались серьезно, что бы тебе подарить...\n')
            check_for_platinum(achievements)
            wannaretry()
            return
    elif crying_flag == False and money != 0:
        for replic in replics_false_and_have_money:
            spellreplic(replic)
        while True:
            crying_flag_1_money = replicinput(file, "Перед Вами стоит стоит непростой выбор:\n1) Продолжить беспокоить\n2) Позолотить руку\n3) Пройти мимо\n/Введите номер вашего выбора: ")
            if crying_flag_1_money == '1' or crying_flag_1_money == '2' or crying_flag_1_money == '3':
                break
            else:
                spellreplic("/Введите номер вашего выбора: ")
        if crying_flag_1_money == '3':
            keep_walking(nickname, money, helped_crying_man, chapter_counter)
        elif crying_flag_1_money == '1':
            spellreplic("\033[31m[Вы]\033[0m\n-В данной ситуации ты просто обязан заценить мой оглушительный успех, хотя я бы тоже не верил если бы не имел у себя, на руках такую сумму бабла\n")
            for replic in replics_pistol_death_ending:
                if replic != replics_pistol_death_ending[-1]:
                    spellreplic(replic)
                else:
                    print(replic + '\n')
            spellreplic(
                'Вы разблокировали концовку: "Сынок, у тебя через два дня день рождения, мы с мамой вот задумались серьезно, что бы тебе подарить..."\n')
            achievements.add(
                'Сынок, у тебя через два дня день рождения, мы с мамой вот задумались серьезно, что бы тебе подарить...\n')
            check_for_platinum(achievements)
            wannaretry()
            return
        elif crying_flag_1_money == '2':
            for replic in replic_golding_hand:
                spellreplic(replic)
            crying_flag_golding = False
            while True:
                a = replicinput(file, "Перед Вами стоит стоит непростой выбор:\n1) Всё-таки дать денег\n2) Плюнуть\n/Введите номер вашего выбора: ")
                if a == "1":
                    break
                elif a == "2":
                    crying_flag_golding = True
                    break
            if crying_flag_golding == True: #вы ужасный человек и бедолага дает вам сдачи
                for replic in replic_spit:
                    spellreplic(replic)
                for replic in replics_pistol_death_ending:
                    if replic != replics_pistol_death_ending[-1]:
                        spellreplic(replic)
                    else:
                        print(replic + '\n')
                spellreplic(
                    'Вы разблокировали концовку: "Сынок, у тебя через два дня день рождения, мы с мамой вот задумались серьезно, что бы тебе подарить..."\n')
                achievements.add(
                    'Сынок, у тебя через два дня день рождения, мы с мамой вот задумались серьезно, что бы тебе подарить...\n')
                check_for_platinum(achievements)
                wannaretry()
                return
            else: #вы большой молодец и решили помочь бедолаге и дали денежку
                spellreplic(f"Ваш баланс: {money}\n")
                donate = replicinput(file, "/Введите сумму пожертвования: ")
                while donate.isdigit() == False or int(donate) <= 0 or int(donate) > money:
                    spellreplic(f"Ваш баланс: {money}\n")
                    donate = replicinput(file, "/Введите сумму пожертвования (натуральное число, не превышающее кол-во ваших денег): ")
                donate = int(donate)
                money -= donate
                spellreplic(f"\033[31m[Вы]\033[0m\n-Держи {donate} рублей, незнакомец. Тебе это сейчас нужнее, чем мне\n")
                spellreplic(f"/Ваш баланс: {money} рублей\n")
                for replic in replics_donate:
                    spellreplic(replic)
                helped_crying_man = True
                keep_walking(nickname, money, helped_crying_man, chapter_counter)


# в keep_walking еще одну переменные на передачу в функцию money

def keep_walking(nickname, money, helped_crying_man, chapter_counter):  # Вы продолжаете свой путь, идя куда глаза глядят
    replics_walking = [
        "Вы продолжаете свой путь, идя куда глаза глядят\n",
        "Вдруг, примерно в 300 ярдах от себя, Вы замечаете бродячий цирк\n",
        "Вы видите пони, бегемотов, кроко и, непосредственно, артистов, а также певичку в кол-ве 1 шт.\n",
        "[Ваши мысли]\n-Хммм, выглядит подозрительно. К тому же я с детства боюсь кроко. Более того, откуда посреди пустыни он мог появиться!? Надо делать ноги отсюда!\n",
        "Вы шуршите конечностями...\n",
        "Спустя продолжительное время Вы наконец набредаете на какое-то зловещее поселение, укутанное туманом\n",
        "Вы бредёте среди заброшенных покосившихся изб...\n",
        "Вам холодно, у вас засосало под ложечкой...\n",
        "Но вдруг Вы заметили единственное уцелевшее здание, решили зайти внутрь и попытались включить стиральную машину\n",
        "Проклятая железяка предательски начала издавать громкие металлические звуки, отдаленно напоминающие Фредди Крюгера\n",
        "Теперь Ваше присутствие не могло остаться без внимания...\n",
        "Едва успев повернуться, Вы заметили орду зомбаков, стоящую в дверях\n",
        "\033[32m[Зомбаки]\033[0m\n-Если хочешь уцелеть, тебе лучше дать нам денег в количестве 113 рублей\n"
    ]

    flagKeepWalking = False

    for replic in replics_walking:
        spellreplic(replic)
    while True:
        reply = replicinput(file,
            "Перед Вами стоит стоит непростой выбор:\n1) Отказаться\n2) Поинтересоваться зачем им деньги\n/Введите номер вашего выбора: ")
        if reply == "1":
            break
        elif reply == "2":
            flagKeepWalking = True
            break
        else:
            pass

    money_and_zombie(flagKeepWalking, nickname, money, helped_crying_man, chapter_counter)


def money_and_zombie(flag, nickname,money, helped_crying_man, chapter_counter):
    replics_no_money = [f"\033[31m[Вы]\033[0m\n-Чёртовы мертвецы, вы не получите от меня ни копейки денег!\n",
                        "Зомбаков не устраивает Ваш ответ\n",
                        "Толпа нежити надвигается на вас\n",
                        "Вы в страхе пятитесь назад, но вдруг вспоминаете о чудо-устройстве, которое Вам дал Альберт Энштейн. Точнее его копия, достачно хорошо повторяющая оригинал\n"]
    replics_ask_zombie = [f"\033[31m[Вы]\033[0m\n-Зомбаки, а зачем вам деньги? Вы же зомбаки\n",
                          "\033[32m[Зомбаки]\033[0m\n-Как это зачем? Купить экипу, замшевые шмотки и оружки\n",
                          f"\033[31m[Вы]\033[0m\n-Но зачем вам это?\n",
                          "\033[32m[Зомбаки]\033[0m\n-Мы собираемся штурмовать злого гения Альберта Энштейна который планирует уничтожить весь мир"]
    # flagMoneyAndZombie = True
    if flag == False:
        for replic in replics_no_money:
            spellreplic(replic)
        flag1 = False
        while True:
            reply = replicinput(file,
                "Перед Вами стоит стоит непростой выбор:\n1) Достать устройство Энштейна и попытаться вылечить зомбаков\n2) Флиртовать\n/Введите номер вашего выбора: ")
            if reply == "1":
                break
            elif reply == "2":
                flag1 = True
                break
            else:
                pass
        action_with_zombie(flag1, nickname,money, helped_crying_man, chapter_counter)
    if flag == True:
        for replic in replics_ask_zombie:
            spellreplic(replic)
        story_zombie_versus_albert(nickname, money, helped_crying_man, chapter_counter)


def action_with_zombie(flag, nickname,money, helped_crying_man, chapter_counter):
    replicsFlirtZombies = [
        f"\033[31m[Вы]\033[0m\n-Дорогие зомбаки, считаю своим долгом отметить, что вы прекрасно выглядите сегодня!\n",
        "\033[32m[Зомбаки]\033[0m\n-Хи-хи... Правда? Никто никогда не говорил нам таких слов...\n", "Вы с облегчением выдыхаете\n",
        "Вдруг сверху слышится хруст, и в ваших глазах темнеет...\n",
        "Пол второго этажа предательски провалился и накрыл Вас\n",
        "Игра закончена. Вы мертвы. Плохая концовка\n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⡶⠶⠶⠾⠿⠿⠿⠟⠿⠿⠿⠿⣷⠶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⠀⠉⠛⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡾⠛⠁⡀⠀⠀⠀⠀⣴⡶⠶⠶⠶⢤⣄⠀⠀⠀⠀⠀⠙⠒⠲⠤⠤⢤⣤⣤⡤⠤⠖⠚⠛⠻⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⣰⠎⣩⠇⠀⠀⠀⠀⠷⠒⠒⠒⠲⢶⣬⡙⢦⡀⠀⠀⠀⣠⠴⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠁⢀⣉⡍⠁⠀⣠⠀⠀⠀⣀⣀⣀⣠⣤⡤⠬⣿⣷⣅⠀⠰⣞⠀⢀⡴⠁⣀⡴⠶⣀⣀⡀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠟⠀⣴⢋⣨⠃⠀⡴⣃⣤⠾⠟⠛⠉⠀⠀⠀⠀⠀⠀⠈⢿⡍⠀⠀⠉⢉⣠⢜⣵⠞⠋⠉⠐⢾⣇⠀⠀⣤⠖⠲⡄⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⣀⣛⣋⠁⠀⣸⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠈⣹⡟⠓⠢⢤⣄⠀⠀⠹⣧⡸⣅⣠⡴⡃⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡷⠊⠁⢨⡇⠀⢰⡏⠀⠀⠀⠀⠀⢠⡶⣿⣿⣷⡀⠀⠀⠀⢠⣿⠀⠀⠀⢰⡿⠀⠀⠀⠀⠉⠻⣦⡀⠉⢱⠀⢠⠟⠙⣦⠀⢿⡄⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⣴⠏⠀⠀⢸⡇⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⡟⠀⠀⠀⣾⠁⠀⠀⠀⣤⣶⣤⡈⠻⣦⣸⠀⡏⠀⠀⣸⠀⢸⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⠞⠁⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⠀⠀⠀⢀⣿⠁⠀⠀⢸⣿⣄⠀⠀⠸⣿⣾⣿⡇⠀⠈⢿⡀⢧⣀⡴⠃⠀⢸⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⣿⡇⠐⡇⡀⠀⠀⢸⣿⣆⠀⠀⠀⠀⠈⢙⣛⣁⣠⣤⡴⢶⣿⠇⠀⠀⠀⠸⣿⣿⣦⡀⠀⠙⠛⠋⠀⠀⢀⣾⢷⠀⠀⠀⠀⠀⢸⡇⢀⣠⣤⣤⣤⡀\n⠀⣠⡶⠋⠉⠉⠉⠛⠶⣤⣹⣇⠘⡽⡁⠀⠀⠘⣷⡙⢷⣶⡶⠞⠛⠛⠛⠉⠉⠀⣠⣾⠏⠀⣀⠀⣠⠀⢹⣿⣿⣿⣶⣦⠀⠀⠀⢀⣾⠇⠈⠀⠀⠀⠀⠀⣼⡗⠋⠉⠀⠀⠹⣿\n⢰⠏⠀⠀⠀⠀⣀⣀⣀⠈⠙⣿⡄⠹⡄⠀⠀⠀⠘⣷⣄⠙⠛⠷⣶⣤⣤⣤⣶⠟⣿⠏⠀⣰⣿⠀⣿⣧⠀⢿⡿⣿⣿⣿⣤⣤⣶⡿⠁⠀⢀⡰⣄⠀⠀⢰⣿⠖⠚⢦⠀⠀⣼⡟\n⣾⠀⠀⠀⠀⡿⠋⢉⣽⣷⡄⠘⣿⡆⣧⠀⠀⠀⠀⠀⠉⠻⠶⠦⠤⠴⠆⣀⣴⠾⠃⠀⣴⣿⣿⠀⣿⣿⣇⠀⠙⢶⣯⣝⡽⣭⠞⠁⠀⣆⠢⡘⠆⠀⢠⣿⢋⣉⡀⠈⢀⣾⠟⠀\n⠸⣦⡤⢤⣄⠷⡀⢸⣀⡘⣿⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠉⠀⠀⠀⠰⠿⠿⠿⠀⠿⠿⠟⠀⠀⠙⠢⠴⠚⠁⠀⠀⠀⠈⠙⢀⠠⣴⡿⣧⣈⣼⠇⠀⣾⠃⠀⠀\n⠀⠈⠁⠈⠛⠟⣧⠈⢿⡾⠏⠀⠀⣸⠏⠻⣦⣧⣄⠀⠀⠀⠀⠀⢤⢤⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢫⣾⣿⣅⡈⠉⢽⣿⣰⡟⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢫⡇⠀⠀⠀⢀⣴⠟⠀⠀⠀⠉⢻⣆⠀⠀⠀⠀⠈⠳⡝⠑⠀⠀⠀⣠⣤⣶⣶⠶⢶⣶⣦⣤⣄⠀⠀⣀⣀⢤⣄⠀⠀⣰⡿⠟⠉⠉⠙⠻⠿⢾⣿⠟⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠚⠋⠉⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣫⡵⣧⠀⠀⠀⢰⣦⣉⣙⢿⣦⡀⠉⠻⠮⠁⢸⡿⠀⠀⠀⠀⠀⠀⢀⣸⣿⣀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡏⠀⢿⣶⣶⣤⣏⠀⣿⠹⣷⣿⣷⡀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢾⢴⣶⡾⡇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣤⣿⣶⣿⣿⣿⣷⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⣷⣶⣶⠃⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢿⣿⣿⣿⣿⣿⣿⡆⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⢀⡄⠀⢸⣿⣿⣿⣿⠙⣿⣿⠿⣷⢸⡇⢸⠿⣿⣿⣿⣿⡿⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⠂⠀⢸⣿⠋⠉⠹⠶⠿⠆⠀⠈⢉⣉⣙⣀⠀⠉⢙⣿⠃⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⣿⠀⠀⠀⠻⣷⣀⣠⣴⣶⠾⠿⠟⠛⠛⠉⠉⠙⠛⠛⠷⢦⣄⡀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠘⠀⣀⣴⡾⠟⠛⠉⠀⠀⠀⠀⠀⠀⠠⠞⠋⠉⠛⠳⣦⡀⠀⠙⠂⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⠀⠘⠃⠀⠀⣰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⢶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⢀⣀⣤⣤⡶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⠶⠶⠶⠶⠶⠶⠶⠿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        #"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
    ]
    replicsTreatZombies = ["Вы из-за пазухи выхватываете пульт от кондиционера, точнее устройство, напоминающее его\n",
                           f"\033[31m[Вы]\033[0m\n-Ну всё, зомбаки, готовьтесь к принудительному излечению\n",
                           "Прокричали вы и занесли палец над спасительной кнопкой\n",
                           "\033[32m[Зомбаки]\033[0m\n-НЕЕЕЕЕЕТ! ОСТЕПЕНИСЬ! НЕ НАЖИМАЙ!\n", "Вы опешили\n",
                           f"\033[31m[Вы]\033[0m\n-Зомбаки, успокойтесь, я просто хочу вас вылечить\n",
                           "\033[32m[Зомбаки]\033[0m\n-Это злодейское устройство убьёт нас насмерть и Энштейн уничтожит весь мир!\n"]

    if flag == True:
        for replic in replicsFlirtZombies:
            if replic != replicsFlirtZombies[-1]:
                spellreplic(replic)
            else:
                print(replic + '\n')
        spellreplic(
            'Вы разблокировали концовку: "Порой случившееся никак от нас не зависит."\n')
        achievements.add(
            'Порой случившиеся никак от нас не зависит.\n')
        check_for_platinum(achievements)
        wannaretry()
        return
    elif flag == False:
        for replic in replicsTreatZombies:
            spellreplic(replic)
        story_zombie_versus_albert(nickname, money, helped_crying_man, chapter_counter)


def story_zombie_versus_albert(nickname, money, helped_crying_man, chapter_counter):
    replicsZombieVersusAlbert = ["Вы опешили\n", f"\033[31m[Вы]\033[0m\n-Зомбаки, вы с дуба рухнули?\n",
                                 f"\033[31m[Вы]\033[0m\n-Как вы смеете говорить такое о благопочтенной голограмме престарелого гения?\n",
                                 f"\033[31m[Вы]\033[0m\n-Ааа, мне всё ясно... Вы, кажется, хотите запятнать его честь, не так ли?\n",
                                 "\033[32m[Зомбаки]\033[0m\n-Никак нет\n", "\033[32m[Зомбаки]\033[0m\n-Позволь нам объясниться\n",
                                 "\033[32m[Зомбаки]\033[0m\n-Дело в том, что голограмма Альберта Энштейна попала в злые руки, и эти люди хотят уничтожить весь мир, потому что их лидера бросила девушка...\n",
                                 "\033[32m[Зомбаки]\033[0m\n-Они сделали зомби лабораторию в которой превращают всех людей в покорных им зомбарезов\n",
                                 "[Ваши мысли]\n-Помню, Энштейн заикался о какой-то лаборатории з...\n",
                                 "[Ваши мысли]\n-Неужто это лаборатория зомбби?!\n",
                                 "\033[32m[Зомбаки]\033[0m\n-Однако нам повезло выбраться из этой злополучной лаборатории и теперь мы хотим помешать их планам\n",
                                 "\033[32m[Зомбаки]\033[0m\n-Поэтому нам нужны деньги, чтобы купить снарягу и разгромить Энштейна и его армию\n"]
    for replic in replicsZombieVersusAlbert:
        spellreplic(replic)
    while True:
        reply = replicinput(file,
            "Перед Вами стоит стоит непростой выбор:\n\n1) Поверить зомбакам\n2) Не поверить\n/Введите номер вашего выбора: ")
        flag = False
        if reply == "1":
            break
        elif reply == "2":
            flag = True
            break
        else:
            pass

    zombie_wise_or_lie(flag, money, nickname, helped_crying_man, chapter_counter)


def zombie_wise_or_lie(flag, money, nickname, helped_crying_man, chapter_counter):
    replicsZombieLie = [f"\033[31m[Вы]\033[0m\n-Что-то не верю я вам, зомбаки...\n",
                        "Вы из-за пазухи выхватываете пульт от кондиционера, точнее устройство, напоминающее его\n",
                        f"\033[31m[Вы]\033[0m\n-Получайте вот это!\n",
                        "Вы нажимаете привлекающую взгляд кнопку и зомбаки начинают плавиться, в агонии скандируя ваше имя\n",
                        f"\033[32m[Зомбаки]\033[0m\n-{nickname}, {nickname}, {nickname}, ЧТО ТЫ НАДЕЛАЛ?!\n",
                        f"\033[32m[Зомбаки]\033[0m\n-{nickname}, {nickname}, {nickname}, ЧТО ТЫ НАТВОРИЛ?!\n-!%?@#%?\n",
                        "Все зомбаки умерли...", "Вдруг Вам звонит Альберт Энштейн\n", "\033[34m[Альберт Энштейн]\033[0m\n-ХА-ХА-ХА\n",
                        "\033[34m[Альберт Энштейн]\033[0m\n-ТЫ ГЛУПЫЙ ДУРАК! Я ПРОВЁЛ ТЕБЯ!\n",
                        "\033[34m[Альберт Энштейн]\033[0m\n-Эти мертвецы-протестанты готовили набег на мою отапливаемую лабораторию, поэтому я не мог приступить к основной части своего хитрого плана\n",
                        "\033[34m[Альберт Энштейн]\033[0m\n-Но теперь, когда ты уничтожил всех непокорных мне зомбарей, я могу с легкостью завершить мой злодейский план и повергнуть этот мир в хаос!\n",
                        "...\n", "Голограмма Альберта Энштейна повергла весь мир в хаос\n", "Человечество уничтожено\n",
                        "Отапливаемая лаборатория передислоцировалась на планету Нибиру\n",
                        "Игра закончена. Вы мертвы. Плохая концовка\n",
                        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK0OkkxxxxxxxkkO0KKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Oxdlc:;,'''...........'',;:loxk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kdl:,''''''''.......................';cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkoc,'''''''''................................':lxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xl;,,,'''''''.......................................,cd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMWXkl;,,,,''''''''...........................................'cxXWMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMN0d:;,,,,''''''''................................................,o0WMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMN0o:;;,,,,''''''''...................................................'lOWMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMW0o:;;,,,,,''''''''......................................................'l0WMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMXxc;;;,,,,,''''''''.........................................................,dXMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMW0l:;;;,,,,,'''''''''...........................................................:OWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMNxc:;;;,,,,,,'''''''''............................................................,dNMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMXd:::;;;,,,,,'''''''''..............................................................'lXMMMMMMMMMMMMMM\nMMMMMMMMMMMMWKdc::;;;;,,,,,''''''''''.............................................................''cKMMMMMMMMMMMMM\nMMMMMMMMMMMMXdc::;;;;,,,,,,''''''''''..............................................................''cKMMMMMMMMMMMM\nMMMMMMMMMMMXdcc::;;;;,,,,,,'''''''''''..............................................................''lXMMMMMMMMMMM\nMMMMMMMMMMNklc:::;;;;,,,,,,'''''''''''..............................................................'''dNMMMMMMMMMM\nMMMMMMMMMW0occ:::;;;;,,,,,,,'''''''''''.............................................................''';OWMMMMMMMMM\nMMMMMMMMMXxlcc:::;;;;,,,,,,,''''''''''''............................................................''''lXMMMMMMMMM\nMMMMMMMMW0olcc:::;;;;,,,,,,,,''''''''''''............................................................''',kWMMMMMMMM\nMMMMMMMMNkllcc:::;;;;;,,,,,,,'''''''''''''..........................................................'''''oNMMMMMMMM\nMMMMMMMMXdllcc:::;;;;;,,,,,,,,''''''''''''''.......................................................'''''':0MMMMMMMM\nMMMMMMMMKdllcc::::;;;;;,,,,,,,,,''''''''''''''.....................................................'''''';kMMMMMMMM\nMMMMMMMW0oolccc:::;;;;;;,,,,,,,,,'''''''''''''''..................................................'''''',,kMMMMMMMM\nMMMMMMMW0dolccc::::;;;;;;,,,,,,,,,''''''''''''''''...............................................'''''',,,xWMMMMMMM\nMMMMMMMW0dollccc::::;;;;;;,,,,,,,,,,''''''''''''''''..........................................''''''''',,,xWMMMMMMM\nMMMMMMMWKxoolccc:::::;;;;;;,,,,,,,,,,''''''''''''''''''.....................................'''''''''',,,;kMMMMMMMM\nMMMMMMMMXxdollccc::::;;;;;;;,,,,,,,,,,,'''''''''''''''''''''.............................'''''''''''',,,,:OMMMMMMMM\nMMMMMMMMNOdoollccc:::::;;;;;;;,,,,,,,,,,,''''''''''''''''''''''''''..................''''''''''''''',,,,,cKMMMMMMMM\nMMMMMMMMWKxdoollccc:::::;;;;;;;,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,;;dNMMMMMMMM\nMMMMMMMMMNOddolllccc:::::;;;;;;;;,,,,,,,,,,,,,''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,;;:0MMMMMMMMM\nMMMMMMMMMWKkddolllcccc:::::;;;;;;;;;,,,,,,,,,,,,,''''''''''''''''''''''''''''''''''''''''''''',,,,,,,;;;dNMMMMMMMMM\nMMMMMMMMMMN0xdoolllcccc::::::;;;;;;;;;,,,,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''',,,,,,,,;;;;l0MMMMMMMMMM\nMMMMMMMMMMMN0xddoollccccc:::::;;;;;;;;;;,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''''''',,,,,,,,,,,;;;;cOWMMMMMMMMMM\nMMMMMMMMMMMMNOxddoolllcccc::::::;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''',,,,,,,,,,,,,,;;;;::xNMMMMMMMMMMM\nMMMMMMMMMMMMMN0kxdoollllcccc::::::::;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;:::xNMMMMMMMMMMMM\nMMMMMMMMMMMMMMN0kxddoolllccccc:::::::;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;:::cxNMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMWKOxxdooolllcccccc::::::::;;;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;::::lkNMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWX0kxddooollllccccc::::::::::;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,;;;;;;;;;;;;;;::::cco0WMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMNKOkxddooollllcccccc:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::cclxXMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMWNKOkxdddoolllllccccccc:::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::ccld0WMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMWNKOkxxddooolllllcccccccc:::::::::::::::::::::;;;;::::::::::::::::ccclldONMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMWNK0kxxdddoooolllllccccccccccc:::::::::::::::::::::::::::::cccccllldONMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Okxxdddoooolllllllccccccccccccccccc:::::ccccccccccccccllllok0NMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0OkkxxdddooooolllllllllcccccccccccccccccccccccllllloodxOXWMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0Okxxxdddoooooooolllllllllllllllllllllllllooodxk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0Okkxxxddddddoooooooooooooooooooooodddxk0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK00OkkkxxxxxxddddddddddddxxxkkO0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNXXKKK000000000000KKKXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"
                        #"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
                        ]
    replicsZombieWise = [f"\033[31m[Вы]\033[0m\n-Зомбаки, я вам верю\n",
                         "\033[32m[Зомбаки]\033[0m\n-Хорошо, тогда дай нам денег на снаряжение. Нам нельзя терять ни секунды\n"]
    if flag:
        for replic in replicsZombieLie:
            if replicsZombieLie.index(replic) != 1:
                spellreplic(replic)
            else:
                print(replic + '\n')
        wannaretry()
        return
    else:
        for replic in replicsZombieWise:
            spellreplic(replic)
        while True:
            flag = False
            reply = replicinput(file, "Перед Вами стоит стоит непростой выбор:\n1) Дать 113 рублей\n2) Не дать\n/Введите номер вашего выбора: ")
            if reply == "1" and money >= 113:
                break
            elif reply == "1" and money < 113:
                flag = True
                break
            elif reply == "2":
                flag = True
                break
            else:
                pass

    rich_poor_zombies(flag, nickname, helped_crying_man, chapter_counter)


def rich_poor_zombies(flag, nickname, helped_crying_man, chapter_counter):
    chapter_counter += 1
    replicsRichZombie = [
        f"\033[31m[Вы]\033[0m\n-Конечно, вот вам 113 рублей. Купите себя наилучшие оружки и снарягу, и мы выдвигаемся\n",
        f"\033[32m[Зомбаки]\033[0m\n-Благодарим Вас, {nickname}\n", "Зомбаки затариваются в шопе неподалёку\n"]
    replicsPoorZombie = [f"\033[31m[Вы]\033[0m\n-Нет, зомбаки, деньгами я вам не помогу\n",
                         f"\033[31m[Вы]\033[0m\n-Идите как есть. Задавим их числом. Я буду прикрывать с тыла\n",
                         f"\033[31m[Вы]\033[0m\n-Идите как есть. Задавим их числом. Я буду прикрывать с тыла\n"]
    replicsZombieAlways = [f"\033[31m[Вы]\033[0m\n-Но как мы попадём в отапливаемую лабораторию голограммы Энштейна?\n",
                           f"\033[32m[Зомбаки]\033[0m\n-Предоставь это нам, {nickname}\n",
                           "Зомбаки ведут Вас за собой. Вы подходите к книжной полке, один из зомбаков дергает за книгу в кожаном переплете...\n",
                           "Вы успеваете заметить лишь промелькнувшую фразу \"Салтыков-Щедрин\" и в мгновение ока оказываетесь в сусеках отапливаемой лаборатории\n",
                           f"\n\nГлава {chapter_counter}:----------------------Штурм отапливаемой лаборатории----------------------\n\n", "\033[32m[Зомбаки]\033[0m\n-Тссс...\n",
                           "Кто-то из зомбаков пшикнул балончиком с краской\n", f"\033[31m[Вы]\033[0m\n-Как здесь тепло...\n"]

    if flag:
        for replic in replicsPoorZombie:
            spellreplic(replic)
    else:
        for replic in replicsRichZombie:
            spellreplic(replic)
    for replic in replicsZombieAlways:
        spellreplic(replic)

    razvilka(flag, nickname, helped_crying_man, chapter_counter)


def razvilka(flag, nickname, helped_crying_man, chapter_counter):
    chapter_counter += 1
    replicsZombieWithMoney = [
        "Один из зомбаков кивнул утвердительно, однако с его макушки предательским образом соскочил топовый шлем, купленный на ваши деньги в байкерском шопе\n",
        "Упавший предмет, напоминающий шлем, издал громкий гудок\n",
        "Вашу шайку сразу же засекла лазерная сигнализация\n",
        "\033[32m[Один из зомбаков]\033[0m\n-АЙ! Я кажется ранен. Возможно, я при смерти\n",
        "Ваша группа понимает, что по вам  работает противозомбовый лазер\n",
        "Спустя некоторое время атака прекращается...\n",
        "Вы обнаруживаете, что все зомбаки живы, однако они полностью голые и безоружные. Лазер уничтожил всю их снарягу\n",
        f"\033[32m[Зомбаки]\033[0m\n-Спасибо Вам, {nickname}, что дали нам денег на топовый лут! Иначе всех нас бы выстегнула лазерка\n",
        f"\033[31m[Вы]\033[0m\n-Рано радуетесь, зомбаки. Нам еще предстоит серьезная битва!\n",
        f"\n\nГлава {chapter_counter}:----------------------Начало конца----------------------\n\n",
        "Вы вместе с разоруженными зомбаками выбираетесь из вечного мрака теплых сусеков\n",
        "Вы видите перед собой гладиаторскую арену, явно страдающую гигантизмом\n",
        "В её углу расположился гигантский голографический Альберт Энштейн\n", "\033[34m[Альберт Энштейн]\033[0m\n-ХА-ХА-ХА\n",
        f"\033[34m[Альберт Энштейн]\033[0m\n-{nickname}, ты явился сюда с жаждой битвы, воодушевляемый огнём своих амбиций. Но ты действительно думаешь, что можешь бросить вызов мне?!\n",
        "Гений злобно смеётся, но вскоре становится серьезным\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Кто-то должен потушить этот огонь...\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Так пусть это буду я! ДА НАЧНЁТСЯ БОЙ!!!\n", "Вы слегка улыбнулись и хрустнули костяшками\n",
        f"\033[31m[Вы]\033[0m\n-Ну поехали...\n", f"\n\nГлава {chapter_counter + 1}:----------------------Финальная битва----------------------\n\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-В бой мои послушные и покорные зомби!!\n",
        "Лауреат Нобелевской премии закидывает руку вперед, и толпа разъярённых, злых и покорных ему зомбарезов начинает тактическое наступление на Вас и вашу шайку\n",
        "Вы плечом к плечу с разоруженными зомбаками бьётесь долго и доблестно с покорными злому гению зомбарезами\n",
        "Однако ваши ряды редееют, и вы оказываетесь в окружении в разряженной обстановке\n",
        f"\033[34m[Альберт Энштейн]\033[0m\n-Ну вот, {nickname}, ну вот, непокорные зомбаки, ваша песенка спета!\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Пристегните ремни, потому что сейчас мы отправим вас прямым рейсом в преисподнюю\n",
        "Злой гений разразился мерзким, скрипящим, как вилка по кастрюле, хихиканьем\n",
        f"\033[32m[Зомбаки]\033[0m\n-{nickname}, кажется наше время настало... Дай нам пульт от кондиционера... Точнее прибор, похожий на него\n",
        f"\033[31m[Вы]\033[0m\n-Нет! Что вы задумали! Не убивайте себя по-братски!\n",
        f"\033[32m[Зомбаки]\033[0m\n-Другого пути нет, {nickname}. Если хочешь спасти этот мир, дай нам наложить на себя руки\n",
        f"\033[31m[Вы]\033[0m\n-Ни в коем случае! Мы не для этого так долго дружили!\n",
        "Вы, отвлёкшись на вопль голографического старикана, отворачиваетесь\n",
        "В этот момент один из зомбаков, предварительно опросив всю группу дружественной нежити и приняв единогласное решение,\nвыхватывает у вас прибор, напоминающий пульт от кондиционера, и нажимает притягивающую взгляд кнопку\n",
        "Еле слышное нажатие кнопки оглушительно проносится по всей арене...\n",
        "Все зомби, как вражеские, так и дружественные, исчезают\n", "...\n",
        "Вы вытираете текущую по щеке слезу и, стиснув зубы, шепчете в ASMR-микрофон\n",
        f"\033[31m[Вы]\033[0m\n-Ты заплатишь за это, мерзкий старикан! Я опалю твою гнусную бороду!\n"]

    replicsZombieNoMoney = [
        "Один из зомбаков кивнул утвердительно, однако с его макушки предательским образом соскочило садовое ведро, которое он использовал как шлем\n",
        "Упавший предмет, напоминающий садовое ведро, издал громкий гудок\n",
        "Вашу шайку сразу же засекла лазерная сигнализация\n",
        "\033[32m[Один из зомбаков]\033[0m\n-АЙ! Как больно! Я, кажется, собираюсь погибнуть...\n",
        "Ваша группа понимает, что по вам  работает противозомбовый лазер\n",
        "Спустя некоторое время атака прекращается...\n", "Вы обнаруживаете, что все зомбаки анигилированы\n",
        "[Ваши мысли]\n-Эх, был бы у них топовый лут, возможно, они бы выжили\n",
        f"\n\nГлава {chapter_counter}:----------------------Начало конца----------------------\n\n",
        "Вы в одиночку выбираетесь из вечного мрака теплых сусеков\n",
        "Вы видите перед собой гладиаторскую арену, явно страдающую гигантизмом\n",
        "В её углу расположился гигантский голографический Альберт Энштейн\n", "\033[34m[Альберт Энштейн]\033[0m\n-ХА-ХА-ХА\n",
        f"\033[34m[Альберт Энштейн]\033[0m\n-{nickname}, ты явился сюда с жаждой битвы, воодушевляемый огнём своих амбиций. Но ты действительно думаешь, что можешь бросить вызов мне?!\n",
        "Гений злобно смеётся, но вскоре становится серьезным\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Кто-то должен потушить этот огонь...\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-Так пусть это буду я! ДА НАЧНЁТСЯ БОЙ!!!\n", "Вы слегка улыбнулись и хрустнули костяшками\n",
        f"\033[31m[Вы]\033[0m\n-Ну поехали...\n", f"\n\nГлава {chapter_counter + 1}:----------------------Финальная битва----------------------\n\n",
        "\033[34m[Альберт Энштейн]\033[0m\n-В бой мои послушные и покорные зомби!!\n",
        "Лауреат Нобелевской премии закидывает руку вперед, и толпа разъярённых, злых и покорных ему зомбарезов начинает тактическое наступление на Вас\n",
        "Вы, не рыпаясь, достаёте пульт от кондиционера, точнее прибор, похожий на него, и нажимаете притягивающую взгляд кнопку\n",
        "Еле слышное нажатие кнопки оглушительно проносится по всей арене...\n",
        "Все зомбарезы в мгновение ока исчезают\n", f"\033[31m[Вы]\033[0m\n-Это было незаметно для меня\n"]

    replicBeforeFight = [f"\n\nГлава {chapter_counter + 2}:----------------------Последняя из финальных битв----------------------\n\n",
                         f"\033[34m[Альберт Энштейн]\033[0m\n-Это было только начало! Теперь я сам вступлю в дуэль с тобой и наконец-таки кокну тебя, {nickname}\n",
                         "Вы дошли до финальной битвы. Альберт Энштейн будет атаковать Вас силой научных знаний, а именно вопросами общего курса физики,\nответы на которые должен знать каждый\n",
                         "Вам будет предоставлено 5 вопросов с 3 вариантами ответа в каждом, однако только один из вариантов будет правильным.\n",
                         "Чем быстрее вы будете давать правильные ответы, тем больше урона будет получать злой гений. Если же Вы неправильно ответите на вопрос, то урон получите Вы.\n",
                         "На финальную битву у Вас будет 3 попытки. Если вы проиграете во всех, то мир будет уничтожен злым гением.\n",
                         "\033[34m[Альберт Энштейн]\033[0m\n-ДА НАЧНЁТСЯ БОЙ!\n"]

    if flag:
        for replic in replicsZombieNoMoney:
            spellreplic(replic)
    else:
        for replic in replicsZombieWithMoney:
            spellreplic(replic)

    for replic in replicBeforeFight:
        spellreplic(replic)

    battle(nickname, helped_crying_man, 0)


def battle(nickname, helped_crying_man, battle_tries): #невероятнейшая функция финальной битвы
    pegolyer_was = False
    boss_hp = 100
    my_hp = 100
    bad_ending_replics = [
        'Все ваши очки здоровья потрачены, ваше тело томно падает на пол',
        '\033[34m[Альберт Энштейн]\033[0m\n-Вот ты и допрыгалась, блоха!\n',
        'Голограмма Альберта Энштейна повергла весь мир в хаос\n',
        'Человечество уничтожено\n',
        'Отапливаемая лаборатория передислоцировалась на планету Нибиру\n',
        'Игра закончена. Вы мертвы. Плохая концовка\n',
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK0OkkxxxxxxxkkO0KKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Oxdlc:;,'''...........'',;:loxk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kdl:,''''''''.......................';cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkoc,'''''''''................................':lxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xl;,,,'''''''.......................................,cd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMWXkl;,,,,''''''''...........................................'cxXWMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMN0d:;,,,,''''''''................................................,o0WMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMN0o:;;,,,,''''''''...................................................'lOWMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMW0o:;;,,,,,''''''''......................................................'l0WMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMXxc;;;,,,,,''''''''.........................................................,dXMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMW0l:;;;,,,,,'''''''''...........................................................:OWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMNxc:;;;,,,,,,'''''''''............................................................,dNMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMXd:::;;;,,,,,'''''''''..............................................................'lXMMMMMMMMMMMMMM\nMMMMMMMMMMMMWKdc::;;;;,,,,,''''''''''.............................................................''cKMMMMMMMMMMMMM\nMMMMMMMMMMMMXdc::;;;;,,,,,,''''''''''..............................................................''cKMMMMMMMMMMMM\nMMMMMMMMMMMXdcc::;;;;,,,,,,'''''''''''..............................................................''lXMMMMMMMMMMM\nMMMMMMMMMMNklc:::;;;;,,,,,,'''''''''''..............................................................'''dNMMMMMMMMMM\nMMMMMMMMMW0occ:::;;;;,,,,,,,'''''''''''.............................................................''';OWMMMMMMMMM\nMMMMMMMMMXxlcc:::;;;;,,,,,,,''''''''''''............................................................''''lXMMMMMMMMM\nMMMMMMMMW0olcc:::;;;;,,,,,,,,''''''''''''............................................................''',kWMMMMMMMM\nMMMMMMMMNkllcc:::;;;;;,,,,,,,'''''''''''''..........................................................'''''oNMMMMMMMM\nMMMMMMMMXdllcc:::;;;;;,,,,,,,,''''''''''''''.......................................................'''''':0MMMMMMMM\nMMMMMMMMKdllcc::::;;;;;,,,,,,,,,''''''''''''''.....................................................'''''';kMMMMMMMM\nMMMMMMMW0oolccc:::;;;;;;,,,,,,,,,'''''''''''''''..................................................'''''',,kMMMMMMMM\nMMMMMMMW0dolccc::::;;;;;;,,,,,,,,,''''''''''''''''...............................................'''''',,,xWMMMMMMM\nMMMMMMMW0dollccc::::;;;;;;,,,,,,,,,,''''''''''''''''..........................................''''''''',,,xWMMMMMMM\nMMMMMMMWKxoolccc:::::;;;;;;,,,,,,,,,,''''''''''''''''''.....................................'''''''''',,,;kMMMMMMMM\nMMMMMMMMXxdollccc::::;;;;;;;,,,,,,,,,,,'''''''''''''''''''''.............................'''''''''''',,,,:OMMMMMMMM\nMMMMMMMMNOdoollccc:::::;;;;;;;,,,,,,,,,,,''''''''''''''''''''''''''..................''''''''''''''',,,,,cKMMMMMMMM\nMMMMMMMMWKxdoollccc:::::;;;;;;;,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,;;dNMMMMMMMM\nMMMMMMMMMNOddolllccc:::::;;;;;;;;,,,,,,,,,,,,,''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,;;:0MMMMMMMMM\nMMMMMMMMMWKkddolllcccc:::::;;;;;;;;;,,,,,,,,,,,,,''''''''''''''''''''''''''''''''''''''''''''',,,,,,,;;;dNMMMMMMMMM\nMMMMMMMMMMN0xdoolllcccc::::::;;;;;;;;;,,,,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''',,,,,,,,;;;;l0MMMMMMMMMM\nMMMMMMMMMMMN0xddoollccccc:::::;;;;;;;;;;,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''''''',,,,,,,,,,,;;;;cOWMMMMMMMMMM\nMMMMMMMMMMMMNOxddoolllcccc::::::;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''',,,,,,,,,,,,,,;;;;::xNMMMMMMMMMMM\nMMMMMMMMMMMMMN0kxdoollllcccc::::::::;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;:::xNMMMMMMMMMMMM\nMMMMMMMMMMMMMMN0kxddoolllccccc:::::::;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;:::cxNMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMWKOxxdooolllcccccc::::::::;;;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;::::lkNMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWX0kxddooollllccccc::::::::::;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,;;;;;;;;;;;;;;::::cco0WMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMNKOkxddooollllcccccc:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::cclxXMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMWNKOkxdddoolllllccccccc:::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::ccld0WMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMWNKOkxxddooolllllcccccccc:::::::::::::::::::::;;;;::::::::::::::::ccclldONMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMWNK0kxxdddoooolllllccccccccccc:::::::::::::::::::::::::::::cccccllldONMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Okxxdddoooolllllllccccccccccccccccc:::::ccccccccccccccllllok0NMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0OkkxxdddooooolllllllllcccccccccccccccccccccccllllloodxOXWMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0Okxxxdddoooooooolllllllllllllllllllllllllooodxk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0Okkxxxddddddoooooooooooooooooooooodddxk0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK00OkkkxxxxxxddddddddddddxxxkkO0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNXXKKK000000000000KKKXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"
        #"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
    ]
    right_answer_replics = [
        '\033[34m[Альберт Энштейн]\033[0m\n-Как ты смог это отгадать? Тебе наверняка просто повезло!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Ты оказался умнее, чем я думал!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-А ты точно человек? Как тебе это удалось?!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-%^!#?1@%#!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Ахх, сорвалась!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Агрх!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Полундра!\n'
    ]
    wrong_answer_replics = [
        '\033[34m[Альберт Энштейн]\033[0m\n-Получай, %^!#?1@%#!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-И-хи-хи-хи-хи... Да ты тугодум!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Сила знаний сильнее тебя! Ну ты и простофиля!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-***! Извините за мой французский\n',
        f'\033[34m[Альберт Энштейн]\033[0m\n-Червь, {nickname}! Ты червь!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Ты, конечно, умён... Но не умнее меня\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-Без правильного ответа как-то всё не ещкере...\n'
    ]
    #average_questions = [
        #'Как изменяется скорость тел при равномерном движении?\n1) Не изменяется\n2) Увеличивается\n3) Уменьшается',
        #'Какая единица является основной единицей длины в Международной системе (СИ)?\n1) Сантиметр\n2) Миллиметр\n3) Метр',
        #'Какой путь пройдёт поезд, движущийся со v = 72 км/ч за З ч?\n1) 72 км\n2) 690 км\n3) 216 км',
        #'Какую траекторию при движении описывает центр колеса автомобиля относительно прямолинейной дороги?\n1) Прямую линию\n2) Кривую линию\n3) Окружность'
    #]
    normal_questions = {
        'Как изменяется скорость тел при равномерном движении?\n1) Не изменяется\n2) Увеличивается\n3) Уменьшается\n/Введите номер вашего выбора: ' : 1,
        'Какая единица является основной единицей длины в Международной системе (СИ)?\n1) Сантиметр\n2) Миллиметр\n3) Метр\n/Введите номер вашего выбора: ' : 3,
        'Какой путь пройдёт поезд, движущийся со v = 72 км/ч за З ч?\n1) 72 км\n2) 690 км\n3) 216 км\n/Введите номер вашего выбора: ' : 3,
        'Какую траекторию при движении описывает центр колеса автомобиля относительно прямолинейной дороги?\n1) Прямую линию\n2) Кривую линию\n3) Окружность\n/Введите номер вашего выбора: ' : 1,
        'Группа самолётов выполняет фигуры высшего пилотажа. Что можно сказать о движении самолётов друг относительно друга?\n1) Самолёты друг относительно друга не движутся\n2) Самолёты движутся неравномерно\n3) Самолёты движутся равномерно\n/Введите номер вашего выбора: ' : 1,
        'Муха летит со скоростью 18 км/ч. Выразите эту скорость в м/с.\n1) 10 м/с\n2) 5 м/с\n3) 0,1 м/с\n/Введите номер вашего выбора: ' : 2,
        'Скорость зайца равна 15 м/с, а скорость дельфина 72 км/ч. Кто из них имеет большую скорость?\n1) Заяц\n2) Скорости одинаковы\n3) Дельфин\n/Введите номер вашего выбора: ' : 3,
        'Выразите в км/ч первую космическую скорость 8 км/с.\n1) 36 000 км/ч\n2) 28 800 км/ч\n3) 8 000 км/ч\n/Введите номер вашего выбора: ' : 2,
        'Наибольшая скорость шмеля 18 км/ч, а стрекозы 10 м/с. Кто из них может быстрее лететь и во сколько раз?\n1) Шмель в 1,8 раза\n2) Шмель в 1800 раз\n3) Стрекоза в 2 раза\n/Введите номер вашего выбора: ' : 3,
        'За какое время катер, двигаясь со скоростью 72 км/ч, пройдёт 500 м?\n1) 30 с\n2) 20 с\n3) 25 с\n/Введите номер вашего выбора: ' : 3,
        'Какая из следующих формул описывает закон всемирного тяготения Ньютона?\n1) F = ma\n2) F = G * (m1 * m2) / r^2\n3) E = mc^2\n/Введите номер вашего выбора: ' : 2,
        'Как называется процесс передачи тепла через нагретые тела путем перемещения частиц?\n1) Конвекция\n2) Радиация\n3) Кондукция\n/Введите номер вашего выбора: ' : 2,
        'Что такое плотность материала?\n1) Масса, деленная на объем\n2) Сила, действующая на единицу площади\n3) Сила тяжести, действующая на единицу объема\n/Введите номер вашего выбора: ' : 1,
        'Какая единица измерения используется для измерения силы тока в электрической цепи?\n1) Вольт\n2) Ампер\n3) Ватт\n/Введите номер вашего выбора: ' : 2,
        'Что из нижеперечисленного является формой потенциальной энергии?\n1) Кинетическая энергия\n2) Электрическая энергия\n3) Гравитационная энергия\n/Введите номер вашего выбора: ' : 3,
        'Как называется закон сохранения энергии, который гласит, что в изолированной системе полная энергия остается постоянной?\n1) Закон Ньютона\n2) Закон Ома\n3) Закон сохранения энергии\n/Введите номер вашего выбора: ' : 3
    }
    tasty_questions = {
        'Вопрос со звездочкой. Кто сильнее: супермэн или каралсен?\n1) Супермэн\n2) Каралсен\n3) Вопрос не по существу\n/Введите номер вашего выбора: ' : 2,
        'Вопрос со звездочкой. Что круче: аниме или футбик?\n1) Аниме\n2) Футбик\n3) У каждого свои вкусы, поэтому в данном случае невозможно дать объективный ответ\n/Введите номер вашего выбора: ' : 2
    }
    if battle_tries == 0: #жесточайшего масштаба костыль чтобы в первые две попытки вопросы были разными
        normal_question_pull = [0, 1, 2, 3, 4, 5, 6, 7]
    elif battle_tries == 1:
        normal_question_pull = [8, 9, 10, 11, 12, 13, 14, 15]
    else:
        normal_question_pull = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    tasty_question_pull = [0, 1]
    right_answer_pull = [0, 1, 2, 3, 4, 5, 6, 7]
    wrong_answer_pull = [0, 1, 2, 3, 4, 5, 6, 7]
    crying_man_mid_battle = [
        f'\033[34m[Альберт Энштейн]\033[0m\n-Вкуси мой луч научных исследований, {nickname}!\n',
        'Вы ловите вредительный луч своим лицом, как вдруг на поле боя появляется до боли знакомый вам незнакомец\n',
        'В правой руке у него пеголь, который он крутит так, как если бы там у него была рева\n',
        f'\033[36m[Спасенный плакса]\033[0m\n-Лови аптечку, {nickname}\n',
        'Вы восстановили здоровье в кол-ве 20 единиц\n',
        '\033[36m[Спасенный плакса]\033[0m\n-А ты, злобный старикан\n',
        'Прокричал плаксивый пегольер\n',
        '\033[36m[Спасенный плакса]\033[0m\n-Угощайся моим виноградом!\n',
        'И тут владелец пеголя начинает без разбора шмалять по Энштейну\n',
        'Альберт Энштейн получил урон в кол-ве 20 единиц\n',
        '\033[36m[Спасенный плакса]\033[0m\n-Я люблю этот мир, я помогу спасти его!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-А я мир не люблю, я люблю физические явления\n',
        'Альберт Энштейн анигилирует пегольера физическим являнием под названием магнетизм пегольера и грены\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-САЁНАРА, покемон\n',
        'Как ни в чём ни бывало, Энштейн атакует вас следующим вопросом\n'
    ]
    crying_man_final_shot = [
        'Вы замечаете как Альберт Энштейн покачивается из последних сил\n',
        'Похоже на то, что ему осталось недолго\n',
        'Но стоило вам ослабить свою бдительность,\nкак коварный Альберт выпустил в вас самонаводящуюся гранату\n',
        'Искра сомнений промелькнула в вашей маленькой черепушке, но краем глаза вы замечаете своего старого друга пегольера\n',
        'Отважный плакса летел как главный герой хит игры Max Payne без разбора шмаляя в ученого из своего блестящего пеголя\n',
        '\033[36m[Спасенный плакса]\033[0m\n-Я люблю этот мир, я помогу спасти его!\n',
        '\033[34m[Альберт Энштейн]\033[0m\n-А я мир не люблю..., я люблю физические явления...\n',
        'Выдавил из себя злодей в предсмертной агонии\n',
        'Сию же секунду снаряд наводится на теплое дуло пистолета и тело пегольера анигилируется физическим являнием под названием магнетизм пегольера и грены\n',
        'Рожки да ножки разлетелись по площади поля боя\n',
        f'\033[34m[Альберт Энштейн]\033[0m\n-Хех... Я умираю... {nickname}..., видимо, у тебя действительно доброе сердце...\n',
        '\033[31m[Вы]\033[0m\n-Я победил, мир спасён!\n',
        'Голограмма Энштейна неспешно улетучивается. Больше она никого не потревожит\n',
        '..........\n',
        'Но какой ценой...?\n',
        'Игра закончена. Вы победили. Хорошая концовка........... Ведь так?\n',
        '╱╭╱╭╱╯╰╰╲╰╲╮╲╮╲\n▔▏╱▔▂┊┊▂▂▔╲╮╲▕▔\n╱╱▏╱X▕┊╱X╲┃▔╲╮╲\n▔╲▏▔▔╱┈▔▔▔┗╲╮▕▔\n┊┊▏╭╰━━╯╮┈┏╯▕▔┊\n┈┊╲┗┳┳┳━┛┈╱▔╲┊┈\n┊┈╱╲╰━╯╯╱▔╭╱┈┈┈\n┈╱╮╮▔▔▏╱╭╱╯┊┈┈┈\n'
    ]
    good_ending = [
        'Тело Альберта подкашивается, вы замечаете, как мышцы его лица сокращаются в агонии\n',
        f'\033[34m[Альберт Энштейн]\033[0m\n-Неееет! Я умираю! {nickname}, видимо, у тебя действительно доброе сердце...\n',
        'Голограмма Энштейна неспешно улетучивается. Больше она никого не потревожит\n',
        'Ваше дыхание на секунду застыло... Вы одержали победу! Мир спасен!\n',
        'Но...... Что же дальше..?'
        'Игра закончена. Вы победили. Хорошая концовка\n',
        '╱╭╱╭╱╯╰╰╲╰╲╮╲╮╲\n▔▏╱▔▂┊┊▂▂▔╲╮╲▕▔\n╱╱▏╱X▕┊╱X╲┃▔╲╮╲\n▔╲▏▔▔╱┈▔▔▔┗╲╮▕▔\n┊┊▏╭╰━━╯╮┈┏╯▕▔┊\n┈┊╲┗┳┳┳━┛┈╱▔╲┊┈\n┊┈╱╲╰━╯╯╱▔╭╱┈┈┈\n┈╱╮╮▔▔▏╱╭╱╯┊┈┈┈\n'
     ]
    if battle_tries == 3: #после трех неудачных попыток игрок проигрывает
        for replic in bad_ending_replics:
            if replic != bad_ending_replics[-1]:
                spellreplic(replic)
            else:
                print(replic + '\n')
        spellreplic(
            'Вы разблокировали концовку: "Отапливаемые полы покрыли поверхность Нибиру."\n')
        achievements.add(
            'Отапливаемые полы покрыли поверхность Нибиру.\n')
        check_for_platinum(achievements)
        wannaretry()
    else:
        while boss_hp > 0 and my_hp > 0: #если все живы и здоровы просто задает вопрос
            boss_hp, my_hp, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull = question(nickname, boss_hp, my_hp, normal_questions, tasty_questions, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics)
            if my_hp == 0 and boss_hp > 20 and pegolyer_was == False and helped_crying_man == True: #если вам плохо пегольер помогает
                pegolyer_was = True
                for replic in crying_man_mid_battle:
                    spellreplic(replic)
                my_hp += 20
                boss_hp -= 20
                print_hp(nickname, boss_hp, my_hp)
            elif boss_hp == 20 and pegolyer_was == False and helped_crying_man == True: #если плохо энштену пегольер помогает и добивает гада
                pegolyer_was = True
                boss_hp = 0
                for replic in crying_man_final_shot:
                    if replic != crying_man_final_shot[-1]:
                        spellreplic(replic)
                    else:
                        print(replic + '\n')
                spellreplic(
                    'Вы разблокировали концовку: "Человечество не забудет тебя, плакса."\n')
                achievements.add(
                    'Человечество не забудет тебя, плакса.\n')
                check_for_platinum(achievements)
                wannaretry()
            elif my_hp == 0:#если вам очень плохо вы умираете
                battle_tries += 1
                spellreplic('Все ваши очки здоровья потрачены, ваше тело томно падает на пол\n')
                spellreplic(f'Оставшееся количество попыток: {3 - battle_tries}\n')
                battle(nickname, helped_crying_man, battle_tries)
            elif boss_hp == 0:#если боссу очень плохо он умирает
                spellreplic('Здоровье Альберта Энштейна опустилось до нуля\n')
                for replic in good_ending:
                    if replic != good_ending[-1]:
                        spellreplic(replic)
                    else:
                        print(replic + '\n')
                spellreplic(
                    'Вы разблокировали концовку: "Энштейн повержен."\n')
                achievements.add(
                    'Энштейн повержен.\n')
                check_for_platinum(achievements)
                wannaretry()


def question(nickname, boss_hp, my_hp, normal_questions, tasty_questions, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics):
    if len(normal_question_pull) != 0 and len(tasty_question_pull) != 0:
        q = randint(1, 10)
        if q <= 9:
            boss_hp, my_hp, normal_question_pull, right_answer_pull, wrong_answer_pull = deeper_question(nickname, boss_hp, my_hp, normal_questions, normal_question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics)
            return boss_hp, my_hp, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull
        elif q == 10:
            boss_hp, my_hp, tasty_question_pull, right_answer_pull, wrong_answer_pull = deeper_question(nickname, boss_hp, my_hp, tasty_questions, tasty_question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics)
            return boss_hp, my_hp, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull
    elif len(tasty_question_pull) == 0:
        boss_hp, my_hp, normal_question_pull, right_answer_pull, wrong_answer_pull = deeper_question(nickname, boss_hp, my_hp, normal_questions, normal_question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics)
        return boss_hp, my_hp, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull
    elif len(normal_question_pull) == 0:
        boss_hp, my_hp, tasty_question_pull, right_answer_pull, wrong_answer_pull = deeper_question(nickname, boss_hp, my_hp, tasty_questions, tasty_question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics)
        return boss_hp, my_hp, normal_question_pull, tasty_question_pull, right_answer_pull, wrong_answer_pull

#тут вообще жесть за пару дней уже сам забыл как работает эта логика но в целом достает из пулла индекс вопроса и потом удаляет этот индекс
def deeper_question(nickname, boss_hp, my_hp, questions, question_pull, right_answer_pull, wrong_answer_pull, right_answer_replics, wrong_answer_replics):
    pullpull = randint(0, len(question_pull)-1)#случайный индекс и пулла индексов
    pull = question_pull[pullpull]#непосредственно индекс по которому мы будем вызывать вопрос
    question_pull.pop(pullpull)#удаляем индекс вопроса чтобы он больше не попадался
    answer = ''
    while answer != '1' and answer != '2' and answer != '3':#ждем пока игрок ответит
        answer = replicinput(file, (list(questions.keys()))[pull])
    answer = int(answer)
    if answer == questions.get((list(questions.keys()))[pull]):#ответ правильный
        pullpull_replica = randint(0, len(right_answer_pull)-1)#тут по той же логике достаем случайную ответную реплику мольберта
        pull_replica = right_answer_pull[pullpull_replica]
        right_answer_pull.pop(pullpull_replica)#удаляем эту реплику из доступных чтобы не повторялись
        spellreplic(right_answer_replics[pull_replica-1])
        spellreplic('Ответ верный, Альберт Энштейн получает 20 урона\n')
        boss_hp -= 20
        print_hp(nickname, boss_hp, my_hp)
    else:#если ответ неверный все аналогично
        pullpull_replica = randint(0, len(wrong_answer_pull)-1)
        pull_replica = wrong_answer_pull[pullpull_replica]
        wrong_answer_pull.pop(pullpull_replica)
        spellreplic(wrong_answer_replics[pull_replica-1])
        spellreplic('Ответ неверный, вы получаете 20 урона\n')
        my_hp -= 20
        print_hp(nickname, boss_hp, my_hp)
    return boss_hp, my_hp, question_pull, right_answer_pull, wrong_answer_pull #продолжаем


def print_hp(nickname, boss_hp, my_hp): #функция выводит ваше здоровье
    spellreplic('Жизни Альберта Энштейнта: ' + ('[X]' * (boss_hp // 20)) + ('[ ]' * (5 - (boss_hp // 20))) + ' - ' + str(boss_hp) + f'%\nЖизни игрока {nickname}: ' + ('[X]' * (my_hp // 20)) + ('[ ]' * (5 - (my_hp // 20))) + ' - ' + str(my_hp) + '%\n')
    #spellreplic(f'Жизни игрока {nickname}: ' + ('[X]' * (my_hp // 20)) + ('[ ]' * (5 - (my_hp // 20))) + ' - ' + str(my_hp) + '%\n')


# battle(nickname, helped_crying_man, battle_tries)
def wannaretry(): #функция спрашивает не хотите ли вы еще раз сыграть и если хотите то перезапускает игру
    ans = ''
    while ans != '1' and ans != '2':
        ans = replicinput(file, "Хотите сыграть еще раз?\n1) Да\n2) Нет\n/Введите номер вашего выбора: ")
    if ans == '1':
        entrance()
    else:
        return

def write_achievements(achievements):
    with open('achievements.txt', 'w') as f:
        f.truncate(0)
        f.writelines(f"{item}\n" for item in achievements)

def check_for_platinum(achievements):
    achievements.remove('\n')
    if len(achievements) == 6:
        spellreplic("Поздравляем! Вы разблокировали все концовки.\nВ награду вы получаете анекдот.\n\nКупил мужик шляпу, а она ему как раз.\n")

def entrance(): #функция все запускает
    nickname, chapter_counter = story_start()
    albert_einstein(nickname, chapter_counter)
    #chapter_cringepoyavlenie(nickname)

#colorama.init()
#ниже введите пароль "лошадь-любовь" без кавычек чтобы перейти в режим разработчика (не надо ждать вывод текста)
print('Здравствуйте\n')
password = input('\033[30;1m---> нажмите Enter чтобы продолжить\033[0m')

if password == "лошадь-любовь":
    def spellreplic(replic):#2) если пользователь ввел пароль то весь текст вываливается моментально
        print(replic)
        file.write(replic + '\n')
else:
    def spellreplic(replic): #1) если пароль не был введен то весь текст в игре выводится медленно аля игра на rpg maker'е
        file.write(replic + '\n')#записывает фразу в файл
        count = 0
        for x in replic:
            if count == len(replic) - 1:
                print(x)
                sleep(0.025)
                input('\033[30;1m---> нажмите Enter чтобы продолжить\033[0m\n')
            else:
                print(x, end="", flush=True)
                count += 1
                if x in ['.', '?', '!']:
                    sleep(0.25)
                else:
                    sleep(0.025)
        return
print('ВНИМАНИЕ! Пожалуйста не спамьте, а нажимайте Enter и вводите ответы ТОЛЬКО когда вас об этом просит программа,\nиначе может случиться непоправимое')
input('\033[30;1m---> нажмите Enter чтобы продолжить\033[0m')
file = filewriting('log_file.txt')
 #ачивменты это по сути разные концовки которые мы будем записывать в соответствующий файл,
#использование множества оправдано так как игре можно достичь одной концовки несколькими способами
f = open('achievements.txt', 'a+')
f.close()
f = open('achievements.txt', 'r')
achievements = f.readlines()
achievements = set(achievements) #ачивменты являются по сути разными концовками, но так как можно достичь одной концовки разными способами применение множества является оправданным
entrance()
#battle('nikita', True, 0)
#print(achievements)
write_achievements(achievements)
file.close()
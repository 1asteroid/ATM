# Karta ma'lumotlari
data = {"password": "1234", "balance": 8000000.00, "tel_number": "900581240", "card_type": "humo", "card_number": "98606004869566500"}

# Bankamat ma'lumotlari
count_ATM = {"money_1": 100, "money_5": 20, "money_10": 50, "money_20": 15, "money_50": 20, "money_100": 20, "money_200": 20}

value_ATM = {"money_1": 1000, "money_5": 5000, "money_10": 10000, "money_20": 20000, "money_50": 50000, "money_100": 100000, "money_200": 200000}

max_money = 0
for i in count_ATM:
    max_money += value_ATM[i] * count_ATM[i]

def print_exit(lan: str):

    """Tanlovni qaytaruvchi fuknsiya"""

    word = ''
    if lan == '1':
        word = """
        0. Orqaga
back. Chiqish
>>>"""

    if lan == '2':
        word = """0. backwards
back. exit
>>>"""

    if lan == '3':
        word = """0. назад
back. Выход
>>>"""

    return word
def check_enough(money: float):

    """Kartada va bankamatda yetarli pul borligini tekshiruvchi fuksiya : True or False"""

    if data["balance"] >= money * 1.01 and max_money >= money:
        return True
    else:
        return False

def print_withdraw_money(lan: str, summa: float):

    """yechilgan pulni consolga chiqaruvchi funksiya"""

    word = ''
    if lan == '1':
        word = f"""\n
        Kartadan yechildi: {summa * 1.01}
        Kartada qolgan pul: {data["balance"]}\n"""

    if lan == '2':
        word = f"""\n
        Removed from the card: {summa * 1.01}
        Remaining money on the card: {data["balance"]}\n"""

    if lan == '3':
        word = f"""\n
        Деньги сняты с карты: {summa * 1.01}
        Остаток денег на карте: {data["balance"]}\n"""

    return word

def count_money_dec(money: float):

    """Bankamat uchun dastur: pul sonini qaytaradi"""

    count = {}

    listATM = list(value_ATM.keys())

    count = count_ATM.fromkeys(listATM)

    for i in range(len(listATM) - 1, -1, -1):
        number = value_ATM[listATM[i]]
        number = float(number)

        if money >= number:
            count[listATM[i]] = money // number

            number2 = count_ATM[listATM[i]]
            number2 = float(number2)

            number3 = count[listATM[i]]
            number3 = float(number3)

            if number2 >= number3:
                money -= number3 * number
            else:
                count[listATM[i]] = int(number2)
                money -= number2 * number

            count_ATM[listATM[i]] -= int(count[listATM[i]])
            print(f"{listATM[i]}   >>>>  {int(count[listATM[i]])}")

    print(count_ATM)

def withdraw(lan: str, summa: float):

    """Pulni yechish dasturi"""

    def qaytish(lan):

        """qaytish funksiyasi: Pul tanlov yoki dastur boshiga"""

        ex = input(f"{print_exit(lan)}")

        if ex == '0':
            return get_money(lan)

        elif ex == 'back':
            return basic()

        else:

            if lan == '1':
                print("\nBunday buyruq mavjud emas\n")

            if lan == '2':
                print("\nNo such command exists\n")

            if lan == '3':
                print("\nтакой команды не существует\n")

            return qaytish(lan)

    if check_enough(summa):
        count_money_dec(summa)

        price = data["balance"] - summa * 1.01
        data["balance"] = price

        print(print_withdraw_money(lan, summa))
        return qaytish(lan)

    else:
        if lan == '1':
            print("\n>>>Kartada yetarli summa yoq yoki bankamatda<<<")

        if lan == '2':
            print("\n>>>Have a sufficient amount on the card or in the ATM<<<")

        if lan == '3':
            print("\n>>>Иметь достаточную сумму на карте или в банкомате<<<")

        return get_money(lan)

def another_money(lan: str):

    """Xohishga ko'ra summani kiritish uchun ko'rinish foydalanuvchiga qulaylik uchun"""

    word = ''
    if lan == '1':
        word = "Boshqa summa"

    if lan == '2':
        word = "Other amount"

    if lan == '3':
        word = "другая сумма"

    return word

def get_money(lan: str):

    """"Olmoqchi bo'lgan summani kiritish uchun funksiya"""

    value = 0

    ty = input(f"""
                1. 50.000
                2. 100.000
                3. 200.000
                4. 400.000
                5. 500.000
                6. {another_money(lan)}
                
                {print_exit(lan)}""")

    if ty == '1':
        value = 50000.0

    elif ty == '2':
        value = 100000.0

    elif ty == '3':
        value = 200000.0

    elif ty == '4':
        value = 400000.0

    elif ty == '5':
        value = 500000.0

    elif ty == '6':
        if lan == '1':
            value = float(input("Qancha summa yechib olmoqchisiz?\n>>> "))

        if lan == '2':
            value = float(input("How much do you want to withdraw?\n>>> "))

        if lan == '3':
            value = float(input("Сколько вы хотите снять??\n>>> "))

    elif ty == '0':
        return service(lan)

    elif ty == 'back':
        return basic()

    else:
        if lan == '1':
            print("\nBunday buyruq mavjud emas\n")
            return get_money(lan)

        if lan == '2':
            print("\nNo such command exists\n")
            return get_money(lan)

        if lan == '3':
            print("\nтакой команды не существует\n")
            return get_money(lan)

    return withdraw(lan, value)

def balance(lan: str):

    """Karta hisobini qaytaruvchi funksiya"""

    print(f"\n\t\t>>>  {data['balance']} <<<\n")

    def balance_uz(lan: str):

        """funsiyadan orqaga qaytish"""

        need = input(
            """ 0. Orqaga
            back. Chiqish
            >>> """
        )
        return need

    def balance_en(lan: str):

        """return function"""

        need = input(
            """            0. backwards
            back. Exit
            >>> """
        )
        return need

    def balance_ru(lan: str):

        """возвращаемая функция"""

        need = input(
            """            0. назад
            back. Выход
            >>> """
        )
        return need

    if lan == '1':

        action = balance_uz(lan)

        if action == '0':
            return service(lan)

        elif action == "back":
            return basic()

        else:
            print(">>>Aniqlanmagan amal<<<")
            return balance(lan)

    if lan == '2':

        action = balance_en(lan)

        if action == '0':
            return service(lan)

        elif action == "back":
            return basic()

        else:
            print("\n>>>Undefined action<<<\n")
            return balance(lan)

    if lan == '3':

        action = balance_ru(lan)

        if action == '0':
            return service(lan)

        elif action == "back":
            return basic()

        else:
            print("\n>>>Неопределенное действие<<<\n")
            return balance(lan)

def undefined(lan):

    """SMS xizmatidan qaytish uchun funksiya"""

    x = input(f"{print_exit(lan)}")

    if x == '0':
        return message(lan)

    if x == 'back':
        return basic()

    else:
        print(">>>> !!!!!! <<<<")
        return undefined(lan)

def connect(lan: str):

    """SMS xabarnomani yoqish funksiyasi"""

    if lan == '1':
        tel = input("Ulamoqchi bo'lgan telefon raqamni kiriting >>>")

    elif lan == '2':
        tel = input("Enter the phone number you want to connect >>>")

    else:
        tel = input("Введите номер телефона, который хотите подключить >>>")

    if len(tel) != 9 or not(tel.isnumeric()):

        if lan == '1':
            print("Raqam mavjud emas")
            return undefined(lan)

        if lan == '2':
            print("the number does not exist")
            return undefined(lan)

        if lan == '3':
            print("номер не существует")
            return undefined(lan)

    else:
        data["tel_number"] = tel

        if lan == '1':
            print(">>>>> Yoqildi <<<<<")
            return undefined(lan)

        if lan == '2':
            print(">>>>> turned on <<<<<")
            return undefined(lan)

        if lan == '3':
            print(">>>>> включенный <<<<<")
            return undefined(lan)

def cancel(lan: str):

    """SMS habarnomani o'chirish funksiyasi"""

    if len(data["tel_number"]) != 9 or not(data["tel_number"].isnumeric()):

        if lan == '1':
            print("Raqam mavjud emas")
            return undefined(lan)

        if lan == '2':
            print("the number does not exist")
            return undefined(lan)

        if lan == '3':
            print("номер не существует")
            return undefined(lan)

    else:
        data["tel_number"] = "i"

        if lan == "1":
            print(">>>>> o'chirildi <<<<<")

        if lan == "2":
            print(">>>>> deleted <<<<<")

        if lan == "3":
            print(">>>>> удалено <<<<<")

        return undefined(lan)


def message(lan: str):

    """SMS ni ulash yoki o'chirishni tanlash funksiyasi"""

    choose = ''

    if lan == '1':
        choose = input(f"""
        1.Sms habarnomani ulash
        2.Sms habarnomani o'chirish
        
        {print_exit(lan)}
        >>> """)

    if lan == '2':
        choose = input(f"""
        1.Connect sms notification
        2.Delete sms notification

        {print_exit(lan)}
        >>> """)

    if lan == '3':
        choose = input(f"""
        1.Подключить смс-уведомление
        2.Удалить смс-уведомление

        {print_exit(lan)}""")

    if choose == "1":
        return connect(lan)

    elif choose == "2":
        return cancel(lan)

    elif choose == '0':
        return service(lan)

    elif choose == 'back':
        return basic()

    else:
        print(">>>> !!!!!!! <<<<")
        return message(lan)


def fill_card(lan: str):

    """Kartaga pul qo'shish funksiyasi"""

    cash = 1.0

    if lan == '1':
        cash = float(input("Qo'shish uchun pul kiriting: "))

    if lan == '2':
        cash = float(input("Enter money to add: "))

    if lan == '3':
        cash = float(input("Введите деньги, чтобы добавить: "))

    data["balance"] += cash

    return balance(lan)

def change_password(lan: str):

    """karta parolni o'zgartiruvchi funksiya"""

    def end(lan: str):

        """qaytish funksiyasi"""

        tired = input(f"{print_exit(lan)}")
        if tired == '0':
            return service(lan)

        elif tired == 'back':
            return basic()

        else:
            return end(lan)

    new_password = 1

    if lan == '1':
        new_password = input("Yangi parol kiriting: ")

    if lan == '2':
        new_password = input("Access new password: ")

    if lan == '3':
        new_password = input("Введите новый пароль: ")

    data["password"] = new_password
    print(data["password"])
    return end(lan)


def direction(lan: str, type: str):

    """xizmat turiga mos funksiyaga yo'naltiruvchi funksiya"""

    if type == '1':
        return balance(lan)

    elif type == '2':
        return get_money(lan)

    elif type == '3':
        return message(lan)

    elif type == '4':
        return fill_card(lan)

    elif type == '5':
        return change_password(lan)

    elif type == 'back':
        return basic()

def service(lan: str):

    def service_uz(lan:str):

        """xizmatlar ro'yhati"""

        service_type = input(
            """\n\t\t>>>Xizmat turini tanlang<<
                > 1. Kartadagi pul
                > 2. Pul yechib olish
                > 3. SMS xabornomani ulash yoki o'chirish
                > 4. Kartani to'ldirish
                > 5. Parolni almashtirish
                
                > back. Chiqish
                
                >>> """)
        return direction(lan, service_type)

    def service_en(lan: str):

        """list of services"""

        service_type = input(
            """\n\t\t>>>Select the type of service<<
                > 1. Money on the card
                > 2. Withdraw money
                > 3. Enable or disable SMS notification
                > 4. Fill the card
                > 5. Change password
    
                > back. Exit
                
                >>> """)
        return direction(lan, service_type)

    def service_ru(lan: str):

        """список услуг"""

        service_type = input(
            """\n\t\t>>>Выберите тип услуги<<
                > 1. Деньги на карте
                > 2. Снять деньги
                > 3. Включить или отключить SMS-уведомление
                > 4. Заполнение карты
                > 5. Изменить пароль
    
                > back. Выход
                
                >>> """)
        return direction(lan, service_type)

    if lan == '1':
        return service_uz(lan)

    if lan == '2':
        return service_en(lan)

    if lan == '3':
        return service_ru(lan)

def check_code(lan: str, code: str):

    """Kodni solishtirish"""

    if code == data['password']:
        return service(lan)

def register_uz(lan: str):

    """kodni tekshirish funcsiyasi"""

    print("\n>>> Registiratsiya bo'limi <<<\n")
    n = 3
    code = input("=>pin codeni kiriting: ")

    while n >= 1:
        if code != data['password']:
            print("Pin code xato kiritildi!!!")
            code = input("=>pin codeni kiriting: ")
            n -=1

        else:
            return check_code(lan, code)

        n -= 1

        if n == 0:
            print("\n>>>>3 tadan ortiq notog'ri urinish sabab kartangiz blokland<<<<<\n")
            return basic()

    return check_code(lan, code)

def register_en(lan: str):

    """code validation function"""

    print("\n>>> Registration part <<<\n")
    n = 3
    code = input("=>Enter the pin code: ")

    while n > 1 and code != data['password']:
        print("Pin-code was entered incorrectly")
        code = input("=>Enter the pin code: ")
        n -= 1

        if n == 1:
            print("\n>>>>Your card has been blocked due to more than 3 incorrect attempts<<<<<\n")
            return basic()


    return check_code(lan, code)

def register_ru(lan: str):

    """ функция проверки кода """

    print("\n>>> отдел регистрации <<<\n")
    n = 3
    code = input("=>введите пин-код: ")

    while n > 1 and code != data['password']:
        print("пин-код неверен!!!")
        code = input("=>введите пин-код: ")
        n -= 1

        if n == 1:
            print("\n>>>>Ваша карта заблокирована из-за более чем 3 неправильных попыток<<<<<\n")
            return basic()

    return check_code(lan, code)


def basic():

    """Tilni tanlash funksiyasi"""

    language = input(
        """>>Tilni tanlang / choose language / выберите язык <<
            > 1 . Uzb
            > 2 . Eng
            > 3 . Rus
            >>> """)
    if language == '1':
        return register_uz(language)
    elif language == '2':
        return register_en(language)
    elif language == '3':
        return register_ru(language)
    else:
        print("\nAniqlanmagan til / Unspecified language / Неуказанный язык \n")
        return basic()

if __name__ == "__main__":
    basic()

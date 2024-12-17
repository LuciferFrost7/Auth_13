from DDLF.DDLF_ConsoleColors import ConsoleColors as cc
import json
import datetime as dt

class User:
    __name = "USER"
    __permission = False

    def __init__(self, name) -> None:
        self.name = name

    def send_message(self, message) -> None:
        print(f'{cc.color.BLUE}<User {self.__name}> {message}{cc.Settings.END}')

class Admin(User):
    __name = "ADMIN"
    __permission = True

    def __init__(self, name) -> None:
        super().__init__(name)

    def send_message(self, message) -> None:
        print(f'{cc.color.PURPLE}<Admin {self.__name}> {message}{cc.Settings.END}')

class Error:
    def send_message(message) -> None:
        print(f'{cc.Settings.BOLD}{cc.color.LIGHTRED}<Error> {message}!{cc.Settings.END}')

class Warning:
    def send_message(message) -> None:
        print(f'{cc.color.RED}<Warning> {message}!{cc.Settings.END}')

class DataBase:
    __file_name = None
    __Users = None
    __Admins = None
    count_of_users = None

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__Users = []
        self.__Admins = []
        self.count_of_users = 0

    def send_message(self, message) -> None:
        print(f'{cc.Settings.BOLD}{cc.color.ORANGE}<DataBase> {message}{cc.Settings.END}')

    def add_user(self, login: str, email: str, password: str, image_name: str) -> bool:
        if login.lower() in self.__Users:
            self.send_message(f'user "{login}" have in DataBase!')
            return False

        with open(self.__file_name, 'r', encoding='utf-8') as file:
            Jfile = json.load(file)

        if login.lower() in [x.lower() for x in Jfile['Users']]:
            self.send_message(f'user "{login}" have in DataBase!')
            return False

        Jfile['Users'][login] = {'email': email, 'password': password,
                             'first_name': None, 'last_name': None, 'gender': None,
                             'reg_date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                             'birthday': None, 'image_index':image_name}
        Jfile['count'] += 1
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(Jfile, file, ensure_ascii=False, indent=4)
        self.__Users.append(login.lower())
        self.send_message(f'user "{login}" successfully appended in DataBase!')
        return True

    def add_information_parametr(self, login: str, question: str, opinion: str) -> bool:
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            Jfile = json.load(file)

        if login.lower() not in [x.lower() for x in Jfile['Users']]:
            self.send_message(f'user "{login}" not exist in DataBase!')

        for i in Jfile['Users']:
            if i.lower() == login.lower():
                Jfile['Users'][i]['question'] = opinion

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(Jfile, file, ensure_ascii=False, indent=4)
        self.send_message(f'user "{login}" successfully appended new information in DataBase!')
        return True


    def get_user(self, login: str) -> dict:
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            Jfile = json.load(file)

        if login.lower() not in [x.lower() for x in Jfile['Users']]:
            self.send_message(f'user "{login}" do not exist in DataBase!')
            return False

        for i in Jfile['Users']:
            if i.lower() == login.lower():
                self.send_message(f'user "{login}" successfully finded in DataBase!')
                return Jfile['Users'][i]

    def delete_user(self, login: str) -> bool:
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            Jfile = json.load(file)

        if login.lower() not in [x.lower() for x in Jfile['Users']]:
            self.send_message(f'can\'t remove user "{login}", because user do not exist in DataBase!')
            return False

        for i in Jfile['Users']:
            if i.lower() == login.lower():
                del Jfile['Users'][i]
                break;

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(Jfile, file, ensure_ascii=False, indent=4)
        self.send_message(f'user "{login}" successfully removed from DataBase!')
        if login.lower() in self.__Users:
            self.__Users.remove(login.lower())
        return True

    def change_user_information(self, login: str, password: str=None, first_name: str=None, gender: str=None,
                                    last_name: str=None, birthday: str=None) -> bool:
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            Jfile = json.load(file)

        if login.lower() not in [x.lower() for x in Jfile['Users']]:
            self.send_message(f'user "{login}" do not exist in DataBase!')
            return False

        for i in Jfile['Users']:
            if i.lower() == login.lower():
                Jfile['Users'][i]['password'] = password
                Jfile['Users'][i]['first_name'] = first_name
                Jfile['Users'][i]['last_name'] = last_name
                Jfile['Users'][i]['birthday'] = birthday
                Jfile['Users'][i]['gender'] = gender

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(Jfile, file, ensure_ascii=False, indent=4)
        self.send_message(f'user "{login}" successfully changed all information in DataBase!')
        return True

    def count_update(self):
        with open(self.__file_name, 'r', encoding='utf-8') as f:
            self.count_of_users = json.load(f)['count']
            return self.count_of_users

class Server:
    __Chars = 'qwertyuiopasdfghjklzxcvbnm_0123456789'
    __PasswordChars = __Chars + '!@#$%'
    __IP = "127.0.0.1"
    __PORT = 7714
    __NAME = None
    __ADMIN_LIST = []
    __USER_LIST = []
    is_need_name = None
    __DataBase = None

    def __init__(self, name, dataBaseName, is_need_name = False) -> None:
        self.__NAME = name
        self.is_need_name = is_need_name
        self.DataBase = DataBase(dataBaseName)

    def Error(self, message) -> None:
        Error.send_message(message)
        return None

    def send_message(self, message) -> None:
        print(f'{cc.color.GREEN}<server{ " " + self.__NAME if self.is_need_name else ""}> {message}{cc.Settings.END}')

    def is_correct_password(self, password: str) -> bool:
        if not isinstance(password, str):
            Error.send_message(f'{type(password)} type can\'t be a password!!!')
            return False

        if len(password) < 8:
            Warning.send_message('Password length less than 8 characters!')
            return False

        if len(password) >= 50:
            Warning.send_message('Password must be less than 50 characters!')
            return False

        if password[0] in '0123456789':
            Warning.send_message('Password can\'t start with numbers!')
            return False

        upper_case_flag = False
        lower_case_flag = False
        digit_flag = False
        for char in password:
            if char.lower() not in self.__PasswordChars:
                Warning.send_message(f'Password can\'t contain {char} symbol!')
                return False
            if char in self.__Chars[:26]:
                lower_case_flag = True
            elif char in self.__Chars[:26].upper():
                upper_case_flag = True
            elif char.isdigit():
                digit_flag = True
        return upper_case_flag and lower_case_flag and digit_flag

    def is_correct_login(self, login: str) -> bool:
        if not isinstance(login, str):
            Error.send_message(f'{type(login)} type can\'t be a login!')
            return False

        if len(login) < 3:
            Warning.send_message('Login must be more than 3 characters!')
            return False

        if len(login) >= 51:
            Warning.send_message('Login must be less than 50 characters!')
            return False

        if login[0] in '0123456789':
            Warning.send_message('Login can\'t start with numbers!')
            return False

        for char in login.lower():
            if char not in self.__Chars:
                Warning.send_message(f'Login can\'t contain {char} symbol!')
                return False
        return True

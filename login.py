"""
This program controls user login, logout, password setting rules.
"""
import os
from time import sleep


users = {'John': {
         'Name and Surname': 'John Doe',
         'Password': 'password',
         },
         'Jane': {
         'Name and Surname': 'Jane Doe',
         'Password': '12345678',
},
    'Olcay': {
    'Name and Surname': 'Olcay Soyuhan',
    'Password': '1923',
}
}


def clear_screen() -> None:
    """
    This function clears the terminal
    Input : None
    Output : None
    """
    if os.name == 'nt': # 'nt' -> Windows software
        os.system('cls')
    else: # OSX or Linux distr.
        os.system('clear')


def sleep_screen() -> None:
    """
    This function sleep the terminal
    Input : None
    Output : None
    """
    sleep(1)


def login_form() -> str:
    """
    This function redirects user login operations
    Input : None
    Output : String
    """
    clear_screen()
    user_name = input('Kullanıcı adı :').strip()
    user_name = user_control(user_name)
    if user_name:
        user_password = password_control(user_name)
        if user_password:
            home_page(user_name)
        else:
            return
    else:
        clear_screen()


def user_control(user_name: str):
    """
    This function controls user logout operations
    Input : String
    Output : Boolen or string
    """
    if user_name.lower() == 'q':
        print('Çıkış yapılıyor...')
        sleep_screen()
        return False
    return user_name_control(user_name)


def user_name_control(user_name) -> str:
    """
    This function checks whether the username is registered or not.
    Input : String
    Output : String
    """
    if user_name in users:
        return user_name
    print('Kullanıcı adı bulunamadı!')
    sleep_screen()
    return login_form()


def password_control(user_name: str) -> bool:
    """
    This function checks user password
    Input : String
    Output : Boolean
    """
    user_access = 3
    while user_access:
        clear_screen()
        user_password = input(f'Parola ({user_access} / 3) :').strip()
        if user_password == users[user_name]['Password']:
            return True
        user_access -= 1
        if user_access:
            print('Girmiş olduğunuz parola hatalı! Lütfen tekrar deneyin...')
            sleep_screen()
    clear_screen()
    print('3 defa hatalı paralo girdiniz!')
    sleep_screen()
    clear_screen()
    return False


def home_page(user_name: str) -> str:
    """
    This function writes the main menu and user name to the screen
    Input : String
    Output : String or Boolean
    """
    clear_screen()
    print(f"""
          Hoş geldin {user_name}\n
          1 --> uygulama 1
          2 --> uygulama 2
          3 --> change password
          4 --> logout\n
          """)
    while True:
        home_page_choice = input('İşlem :')
        if home_page_choice in '1234':
            if home_page_choice == '1':
                pass
            elif home_page_choice == '2':
                pass
            elif home_page_choice == '3':
                user_password_change(user_name)
            elif home_page_choice == '4':
                return login_form()
        else:
            print('Hatalı giriş yaptınız!')
        return False


def user_password_change(user_name: str) -> str:
    """
    This function checks the user password and checks the rules for setting 
    new passwords.

    Input : String
    Output : String
    """
    user_password = password_control(user_name)
    if user_password:
        new_password_access = 3
        pass_has_char = False
        character_is_lower = False
        character_is_upper = False
        while new_password_access:
            clear_screen()
            special_characters = '?, @, !, #, %, +, -, *, %'
            print(f"""
              Şİfre oluşturma kuralları:
              En az 8 karakterden oluşur.
              Harflerin yanı sıra, rakam ve '{special_characters}' gibi 
              özel karakterler içerir.
              Büyük ve küçük harfler bir arada kullanılır.
              """)
            new_user_password = input(
                f'Yeni parola girin ({new_password_access} / 3) :')
            if len(new_user_password) >= 8:
                for character in new_user_password:
                    if character in special_characters:
                        pass_has_char = True
                    elif character.islower():
                        character_is_lower = True
                    elif character.isupper():
                        character_is_upper = True
                if character_is_lower and character_is_upper and pass_has_char:
                    return user_repeat_password_check(user_name,
                                                      new_user_password)
                new_password_access -= 1
            else:
                new_password_access -= 1
        print('Parola oluşturma kurallarına uygun giriş yapınız!')
        sleep_screen()
        return home_page(user_name)
    return home_page(user_name)


def user_repeat_password_check(user_name: str, new_user_password: str) -> str:
    """
    This function retrieves the new password from the user and changes 
    the password.
    Input : String
    Output : String
    """
    re_new_user_password = input('Yeni parolayı tekrar girin :')
    if re_new_user_password == new_user_password:
        users[user_name].update({'Password': new_user_password})
        return home_page(user_name)
    print('Parolalar aynı değil!')
    sleep_screen()
    return home_page(user_name)


login_form()

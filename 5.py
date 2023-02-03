def verify_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True
    return has_lower and has_upper and has_digit and has_special


password = input("Введите пароль: ")
if verify_password(password):
    print("Подходящий пароль")
else:
    print("Не подходящий пароль")

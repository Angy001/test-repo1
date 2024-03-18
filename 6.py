while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8 or password.isupper():
    	print('Недопустимый пароль. Придумайте новый') 
    elif password.islower():
        print('Недопустимый пароль. Придумайте новый')
    else:
        print('Надежный пароль')
        break
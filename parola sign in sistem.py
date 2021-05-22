username = input('Introduceti username-ul: ')
parola = input('introduceti o parola: ')
f = open('user1.txt', 'r')
content = f.read()
if parola in content and username in content:
    print('Buna, ' + username + '!')
elif username not in content:
    print('Nume de utilizator gresit')
elif parola not in content:
    print('Parola gresita')
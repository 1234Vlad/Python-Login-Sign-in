# Python-Login-Sign-in
#Login
import datetime
import random
username = input('Introduceti username-ul: ')
parola = input('introduceti o parola: ')
data_de_alaturare = str(datetime.datetime.now())
popularitate = str(random.randrange(4, 100))
f = open('user1.txt', 'a')
f.write(username + '\n')
f.write(parola + '\n')
f.write(data_de_alaturare + '\n')
f.write(popularitate + '\n')
f = open('cautare useri.txt', 'a')
f.write(username + '\n')

#Sign In
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

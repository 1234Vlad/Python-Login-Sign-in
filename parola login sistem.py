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


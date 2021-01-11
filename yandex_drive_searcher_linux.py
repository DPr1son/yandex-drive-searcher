import requests
import random
import colorama
import sys
file = open('workings_drives_yandex.txt', 'a')
g = str("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_")

def gen():
	global g
	i = str("http://yadi.sk/d/" + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g))
	check(i)
def check(url):
	r = requests.get(url)
	print("\033[33m" + url)
	if r.status_code == 404:
		print("\033[31mДиск не рабочий! | Drive not working!")
	else:
		print("\033[32mДиск рабочий! | Drive is working!")
		file.write('\n' + url)
	gen()
sys.setrecursionlimit(999999999)
gen()

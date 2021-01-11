import requests
import random
import sys
file = open('workings_drives_yandex.txt', 'a')
g = str("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_")

def gen():
	global g
	i = str("http://yadi.sk/" + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g))
	check(i)
def check(url):
	r = requests.get(url)
	print("url)
	if r.status_code == 404:
		print("Диск не рабочий! | Drive not working!")
	else:
		print("Диск рабочий! | Drive is working!")
		file.write('\n' + url)
	gen()
sys.setrecursionlimit(999999999)
gen()

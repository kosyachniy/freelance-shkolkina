import json
import time
from multiprocessing import Process

from fastapi import FastAPI
from pydantic import BaseModel
import Levenshtein

from google_sheets import read


with open('sets.json', 'r') as file:
	sets = json.loads(file.read())
	APPROXIMATION = sets['approximation']
	SHEET = sets['sheet']

LOCK = True


app = FastAPI(title="Cities")


class CityInput(BaseModel):
	city: str


def get_cities():
	with open('cities.json', 'r') as file:
		cities = json.loads(file.read())

	return list(map(lambda i: i.lower(), cities))

def background():
	while True:
		cities = get_cities()

		try:
			cities_new = read(SHEET, 'Лист1', 1, 2, 1, 1000)
		except Exception as e:
			print('ERROR `read`', e)
			time.sleep(1)
			continue

		try:
			cities_new = [i[0] for i in cities_new if len(i)]
		except Exception as e:
			print('ERROR `convert` for {}'.format(cities_new), e)
		else:
			cities_proc_new = list(map(lambda i: i.lower(), cities_new))

			if cities_proc_new != cities:
				with open('cities.json', 'w') as file:
					print(json.dumps(cities_new, ensure_ascii=False, indent='\t'), file=file)

		time.sleep(600)

def find(word):
	word = word.lower()
	result = None
	dist = None
	cities = get_cities()

	for city in cities:
		dist_cur = Levenshtein.distance(word, city)

		if dist == None or dist_cur < dist:
			dist = dist_cur
			result = city

	if dist > APPROXIMATION:
		return None

	return result.title()


@app.post('/')
async def check(req: CityInput):
	global LOCK

	if LOCK:
		LOCK = False
		process = Process(target=background)
		process.start()

	return find(req.city)
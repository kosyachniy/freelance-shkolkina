import json

from fastapi import FastAPI
from pydantic import BaseModel
import Levenshtein


with open('sets.json', 'r') as file:
	sets = json.loads(file.read())
	APPROXIMATION = sets['approximation']
	CITIES = sets['cities']


app = FastAPI(title="Cities")
cities = list(map(lambda i: i.lower(), CITIES))


class CityInput(BaseModel):
	city: str


def find(word):
	word = word.lower()
	result = None
	dist = None

	for city in cities:
		dist_cur = Levenshtein.distance(word, city)

		if dist == None or dist_cur < dist:
			dist = dist_cur
			result = city

	if dist > APPROXIMATION:
		return None

	return result.title()


@app.post('/')
async def add(req: CityInput):
	return find(req.city)
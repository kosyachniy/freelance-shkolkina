import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Read keys
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

# Auth
httpAuth = credentials.authorize(httplib2.Http())

# Select API
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


def _convert_to_letters(x):
	res = ''
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	while (x > 0):
		position = x % 26
		res = ('Z' if position == 0 else chr(97 + (position - 1 if position > 0 else 0))) + res
		x = (x - 1) // 26

	return res.upper()

def _convert_to_numbers(x):
	number = 0
	p = 1

	for i in list(range(len(x)))[::-1]:
		number += (ord(x[i]) - ord('A') + 1) * p
		p *= 26

	return number


def write(sheet, name, data, offset_x=1, offset_y=1):
	service.spreadsheets().values().batchUpdate(spreadsheetId=sheet, body={
		"valueInputOption": "RAW",
		"data": [{
			"range": "{}!{}{}:{}{}".format(name, _convert_to_letters(offset_x), offset_y, _convert_to_letters(offset_x+len(data[0])), len(data)+offset_y),
			"majorDimension": "ROWS",
			"values": data,
		}]
	}).execute()

def read(sheet, name, opening, start, ending, stop):
	results = service.spreadsheets().values().batchGet(
		spreadsheetId=sheet,
		ranges=["{}!{}{}:{}{}".format(name, _convert_to_letters(opening), start, _convert_to_letters(ending), stop)],
		valueRenderOption='FORMATTED_VALUE',
		dateTimeRenderOption='FORMATTED_STRING',
	).execute()

	try:
		return results['valueRanges'][0]['values']
	except:
		return []
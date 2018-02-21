import requests
from bs4 import BeautifulSoup
import json


def func(query):
	data = {}
	data['books'] = []

	locs = []
	loc = []
	st = []

	path = "https://catalyst.library.jhu.edu/catalog?q="
	fpath = path + query
	html = requests.get(fpath)
	soup = BeautifulSoup(html.text, "html.parser")
	divTag = soup.find_all("div", {"class": "document blacklight-book blacklight-print"})
	print("\n")
	for dv in divTag:
		title = dv.find("div", {"class": "col-sm-9 col-lg-10 item-heading-column" })
		name = title.find("a").text
		holdings = dv.find_all("li", {"class": "holding list-group-item" })
		for holding in holdings:
			status = holding.select('div[class*="status col-xs-4"]')[0].text.lstrip().rstrip().replace("\n","")
			place = holding.find("div", {"class":"collection col-sm-8"}).text.lstrip().rstrip().replace("\n","")
			shelf = holding.find("div", {"class":"call-number col-xs-8"}).text.lstrip().rstrip().split("\n")[0]
			loc.append(place)
			loc.append(shelf)
			locs.append(loc)
			st.append(status)
			loc = []
		data['books'].append({
			'name': name,
			'location': locs,
			'status': st
			})

	jstring = json.dumps(data)
	return json.loads(jstring)
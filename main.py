import requests
from bs4 import BeautifulSoup


while True:

	pokemon = input("Type a pokemon to search for (Not case sensitive) \n>>").capitalize()
	print()
	
	url = "https://bulbapedia.bulbagarden.net/wiki/" + pokemon + "_(Pok%C3%A9mon)"

	
	response = requests.get(url)
	html = response.text
	
	soup = BeautifulSoup(html, "html.parser") # gets HTML of page
	 
	print(f"Image - https:{soup.find_all('img')[2]['src']}")
	print("(If link doesn't work, reload the page to fix it)\n")
		

	
	for spans in (soup.find_all("span")): # Gets all Spans on the page
		if spans.text == "Stat": # Gets the specific span labelled "Stat"
			stats = (spans.parent.parent.parent.parent).find_all("span") # Finds all spans of this table
			break
	
	
	
	for stat in stats[1:7]:
		print(f"{stat.text} = {stat.parent.parent.parent.find_all('div')[1].text}") # Prints each stat in table
	
	
	print("\n")

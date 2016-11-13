import json
import urllib.request
def get(arg):
	response = urllib.request.urlopen("https://www.googleapis.com/customsearch/v1?key=AIzaSyDAmhrmizdXy8fCA1XOhRREoqx0E6wu-s4&cx=016734205687455053515:rtx4ejkkseu&defaultToImageSearch=True&searchtype=image&q=" + arg)
	html = response.read().decode('utf-8')
	html_split = html.split()
	#print(html_split)
	for i in range(0,len(html_split)):
		if html_split[i] == "\"cse_image\":":
			return html_split[i + 4].replace("\"", "")

	

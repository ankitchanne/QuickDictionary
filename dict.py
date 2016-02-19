import urllib
import sys
import json
phrase = sys.argv[1]
url = "https://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&pretty=true&phrase="+phrase
response = urllib.urlopen(url)

answer= json.load(response)
for i in range(5):
	print str(i+1)+") "+answer["tuc"][0]["meanings"][i]["text"]
	
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definit(word):
	word = word.lower()
	if word in data:
		return (data[word])
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead ? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
		if yn == "Y":
			return ("\n- ".join(data[get_close_matches(word, data.keys())[0]]))
		elif yn == "N":
			return ("This word doesn't exist")
		else:
			return ("I dodn't understand what you mean")
	else:
		return ("This word doesn't exist")

word = input("Enter a word: ")

output = definit(word)

if type(output) == list:
	for item in output:
		print("-", item)
else:
	print(output)



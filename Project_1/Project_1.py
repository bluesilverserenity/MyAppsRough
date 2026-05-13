import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if ans == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif ans == "N":
            return "Word does not exist. Please double check it."
        else:            return "We didn't understand your entry."
    else:
        return "Word not found."

word = ""

while word != "close":
    word = input("Enter a word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
        continue

import json
from difflib import get_close_matches

# load JSON data from `data.json` into a Python dictionary named `data`
data = json.load(open("data.json"))

def translate(word):
    # normalize input to lowercase for case-insensitive lookup
    word = word.lower()
    # if the exact word exists in data, return its definition(s)
    if word in data:
        return data[word]
    # if no exact match but there are close matches, ask user to confirm the suggestion
    elif len(get_close_matches(word, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]) # get the closest match and ask user to confirm
        if ans == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        # if user denies, tell them the word does not exist
        elif ans == "N":
            return "Word does not exist. Please double check it."
        else:            return "We didn't understand your entry."
    else:
        return "Word not found."

word = ""

# keep asking the user for words until they type "close"
while word != "close":
    word = input("Enter a word: ")
    output = translate(word)
    # if the output is a list of definitions, print each on a new line
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
        continue

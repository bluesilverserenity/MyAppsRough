import json

data = json.load(open("data.json"))
word = input("Enter a word: ")
print(data[word])

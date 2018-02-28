import json
from difflib import get_close_matches
data = json.load(open("data.json"))
j=0
def translate(word):
    if word in data:
        global j
        j = 1
        return data[word]
    else:
        return similar(word)

def similar(word):
    if len(get_close_matches(word, data.keys())) > 0:
        check = input("did you meant %s ? y for yes, n for nope  " % get_close_matches(word, data.keys())[0]).upper()
        if check == "Y":
                return data[get_close_matches(word, data.keys())[0]]
                global j
                j = 1
        if check == "N":
            return "ok, your word does not exist"
        else:
            return "ops, something went wrong, try to retype "

    else:
        return "the word does not exist, recheck"
while True:
    word = input("tell me the word, type exit1 to quit: ").lower()
    if word== "exit1":
        break
    out = translate(word)
    if j == 0:
        print(out)
    else:
        for i in out:
            print(i)

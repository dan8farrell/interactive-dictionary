import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_word(w):
    w = w.lower().strip()
    if word in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]         
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, enter N if no." % get_close_matches(w,data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or "n":
            return "Sorry dude... we don't know what you want here..."
        else:
            return "Try again... spell right... or hit y or n next time ya snazzle ya snorps."    
    else:
        return "fagget...."

word = input("Pick any word and I'll tell you what it means:")
output = (find_word(word))

if type(output)== list:
    for item in output:
        print (item)

else:
    print(output)
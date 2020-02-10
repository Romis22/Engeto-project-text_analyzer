'''
author = 
'''
TEXTS = [
'''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# line separation definition
line_separation = "-"*60

# list of usernames and passwords
USERNAMES = ["bob", "ann", "mike", "liz"]
PASSWORDS = ["123", "pass123", "password123", "pass123"]
# dict with pars of usernames and passwords
#dict_usernames_passwords = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

# greeting for user
print(line_separation)
print("Hello, welcome to text analyzer program.")
print(line_separation)

# get username and password
username = str(input("Please enter your username:"))
password = str(input("Please enter your password:"))

# check registration of user
attempt = 3
while attempt > 0:
    #if username in dict_usernames_passwords.keys() and password == dict_usernames_passwords[username]:
    if username in USERNAMES and password == PASSWORDS[USERNAMES.index(username)]:
        print(line_separation)
        print("Your combination of username and password is correct.")
        print(line_separation)
        break
    else:
        attempt -= 1
        if attempt == 0:
            print ("Program shutdown")
            quit()
        print(line_separation)
        print("Combination of username and password is incorrect.You have", attempt, ("attempt." if attempt == 1 else "attempts."))
        print(line_separation)
        username = str(input("Please enter your username:"))
        password = str(input("Please enter your password:"))

# choice of TEXTS
print("You can choose from", len(TEXTS), "texts:")
print(line_separation)
for text in TEXTS:
    print(TEXTS.index(text)+1, " - ", text[:40]+"...")

    # predefined invalid choice
choice_of_text = 0

    # get user choice, check validity, eventualy ask again for choice
while type(choice_of_text) != int or not 0 < choice_of_text <= len(TEXTS):
    print(line_separation)
    choice_of_text = (input("What text do you choose? Chose between [1-"+str(len(TEXTS))+"]"))
    try:
        choice_of_text = int(choice_of_text)
    except Exception as e:
        print(e)

# chosen text
chosen_text = str(TEXTS[choice_of_text-1])

# analysis of text
    # variable defenition
sum_of_words = 0
sum_of_title_words = 0
sum_of_upper_words = 0
sum_of_lower_words = 0
sum_of_numeric_words = 0
sum_of_numbers = 0
lengths_of_words = []

    # text separation and cleaning
chosen_text = chosen_text.replace("\n"," ")
chosen_text = chosen_text.replace("  "," ")
splited_words = chosen_text.split(" ")

    # conditions - je možné přepsat pomocí slovníku a metody get? > viz Use case 1 while loop
while splited_words:
    word = splited_words.pop()
    word = word.strip("$%&'()*+,-./:;<=>!?@[\]^_`{|}~\"")
    if len(word) != 0:
        sum_of_words += 1
        lengths_of_words.append(len(word))
    if word.istitle():
        sum_of_title_words += 1
    if word.isupper():
        sum_of_upper_words += 1
    if word.islower():
        sum_of_lower_words += 1
    if word.isnumeric():
        sum_of_numeric_words += 1
        sum_of_numbers = sum_of_numbers + int(word)

    # make a set of unique lengths od words
set_of_len_words = set(lengths_of_words)

# results
    # sums of word types
print(line_separation)
print("There are",sum_of_words, "words in the selected text.")
print("There are",sum_of_title_words, "titlecase words.")
print("There are",sum_of_upper_words, "uppercase words.")
print("There are",sum_of_lower_words, "lowercase words.")
print("There are",sum_of_numeric_words, "numeric words.")
print(line_separation)

    # lengths of words
for i in set_of_len_words:
    sum_of_lengths = lengths_of_words.count(i)
    print(i, sum_of_lengths * "*", sum_of_lengths)

    # sum of numeric-only words
print(line_separation)
print("If we summed all the numbers in this text we would get:", sum_of_numbers)
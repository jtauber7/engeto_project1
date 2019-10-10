# '''
# author = Jan Tauber
# '''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
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
# User-passwords
userpass = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
# Greet user and get log in
print("-" * 40)
print("Welcome to the app. Please log in:")
username = input("USERNAME: ")
passw = input("PASSWORD: ")
print("-" * 40)

# check users and passwords
if username not in userpass:
    print("Your username does not exist. Please contact us to register.")
    exit()
if userpass[username] != passw:
    print("Your password is not correct. The script will stop.")
else:
    # Text choosing
    choose = int(input("We have 3 texts to be analyzed.\n"
                       "Enter a number btw. 1 and 3 to select: "))
    if choose not in (1, 2, 3):
        print("Wrong selection of the text, script will stop.")
    else:
        print("-" * 40)
        textlist = TEXTS[choose-1].split()
        textstr = TEXTS[choose-1]  # variable for counting letters for bar chart
        numsum = float()  # variable for counting sum of numeric strings

        # counting words
        print("There are ", len(textlist), " words in the selected text.")

        # counting specific words
        index = 0
        titlecase = 0
        uppercase = 0
        lowercase = 0
        numstr = 0
        while index < len(textlist):
            if textlist[index].istitle():
                titlecase += 1
            if textlist[index].isupper():
                uppercase += 1
            if textlist[index].islower():
                lowercase += 1
            if textlist[index].isdigit():
                numstr += 1
                numsum = numsum + float(textlist[index])  # calculate sum of numeric words
            index += 1
        print("There are", titlecase, "titlecase words.")
        print("There are", uppercase, "uppercase words.")
        print("There are", lowercase, "lowercase words.")
        print("There are", numstr, "numeric strings.")
        print("-" * 40)

        # bar chart frequencies and delete punctuations
        punctuations = """."!',"""  # remove punctuations and save as a new string
        index = 0
        textstr_nopunct = ""
        while index < len(textstr):
            if textstr[index] not in punctuations:
                textstr_nopunct = textstr_nopunct + textstr[index]
            index += 1

        barchart = {}  # save selected text with no punctuations as a list and count into dict
        index = 0
        textlist = textstr_nopunct.split()
        while index < len(textlist):
            barchart[len(textlist[index])] = barchart.get(len(textlist[index]), 0) + 1
            index += 1

        index = 1  # print a bar chart with frequencies
        while index <= max(barchart):
            if index in barchart.keys():
                print(index, "*" * barchart[index], barchart[index])
            index += 1
        print("-" * 40)

# sum of the numbers counted while counting specific words
        print("If we summed all the numbers in this text we would get: ", numsum)
        print("-" * 40)

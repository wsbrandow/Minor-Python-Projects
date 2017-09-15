while True: #makes code loop

    original = input("Please enter a word: ")

    pyg = "ay"

    if len(original) > 0 and original.isalpha():
        word = original.lower() # then makes input lower case
        first = word[0] # then also defines "first" as the first letter
        if first in "aeiou": # if "first" is a vowel
            new_word = word # skip taking first letter
            pig_latin = new_word + pyg
        else: # if "first" variable is not a vowel
            new_word = word[1:] # takes "word" sans first letter
            pig_latin = new_word + first + pyg
        print (pig_latin)

    else:
        print ("Please enter a word")

# the order of variables on lines will affect how python reads them


    

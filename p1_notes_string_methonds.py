sentence = ("The quick brown fox jumps over the lazy dog.")

print(sentence.split()) #splits the sentence so that it becomes a list that goes such as ['word', 'other word']

fixed = sentence.replace("fox" , 'wolf') # replaces a word of the sentence

name = input("What is your name: ")

print("Hello " + name.strip().title()) # keeps it normal when our user is incredibly stupid
# strip removes EVERY white space

print(sentence.lower()) # makes everything lowercase

print(sentence.upper()) # capitalizes every word

print(sentence.capitalize()) # capitalizes the first letter of the sentence

print(sentence.title()) # capitalizes the first letter of every word

print(fixed)

print(full_name.isalpha()) # Checks if the entire thing is characters
print(full_name.isnumeric()) # Checks if the entire thing is numbers
print(full_name.isupper()) # Checks is all the string is uppercase

print(f"Hello {full_name} welcome to my program.") # lets us not throw in extra things like spaces or +'s

# formatted string
print(f"hello {fixed.title()} {last_fixed} welcome to my program.")

letter = input("Give me a letter: ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter +chr(number_value)
print(f"your letter was {letter} now it is {new_letter}") # Does stuff
#######################################################

#Github Repo Link

#Name : Ashis Rai
#Section : A
#Student ID Number : 02240334

#######################################################

#REFERENCES
# https://youtu.be/lmR4s8D_5k0?si=53PWFWA5d1O8T4C1
# https://youtu.be/LyymFN9t4kw?si=-w2jAU1Fa5Y4guNW
# https://youtu.be/Mi3j54ZMxOc?si=Mlx7cGFwJ19w-X_A
# https://youtu.be/FNOpWah3saA?si=n7igQvk1DpxqpZCb

########################################################
#SOLUTION
########################################################
import re

#Read the dictionary_file
def readDictionaryFile(dictionaryFilename):
    with open(dictionaryFilename, "r", encoding="utf-8") as file:
        return set(file.read().splitlines()) 

#Find Errors
def findErrors(textFilename, dictionaryWords):
    errors = []
    with open(textFilename, "r", encoding="utf-8") as file:
        for lineNumber, line in enumerate(file, start=1):
            for match in re.finditer(r'[\u0F00-\u0FFF]+', line):
                word = match.group().replace("།", "་")
                if word not in dictionaryWords:
                    errors.append((word, lineNumber, match.start()))
    return errors

#Print Errors
def printErrors(errors):
    if errors:
        for word, line, pos in errors:
            print(f"'{word}' at line {line}, position {pos}")
    else:
        print("No misspelled words found.")

#Spell Checker
def main():
    dictionaryFile = input("Enter the dictionary file: ")
    textFile = input("Enter the text file: ")

    dictionaryWords = readDictionaryFile(dictionaryFile)
    errors = findErrors(textFile, dictionaryWords)
    printErrors(errors)

main()
########################################################

#Other parts of code required for the solution

#Importing the input_file and dictionary file from the url

# import requests
# url ="https://csf101-server-cap1.onrender.com/get/input/334"
# response = requests.get(url)

# with open("input_file.txt","wb") as file:
#     file.write(response.content)

# print("Input file downloaded")

# url ="https://csf101-server-cap1.onrender.com/get/dictionary"
# response = requests.get(url)

# with open("dzongkha_dictionary.docx","wb") as file:
#     file.write(response.content)

# print("Input file downloaded")

# Converting the docx file into text

# import docx2txt as d2t
# dfile="dzongkha_dictionary.docx"
# tfile="dzongkha_dictionary.txt"

# doc=d2t.process(dfile)
# file=open(tfile, "w",encoding="utf-8")
# file.write(doc)
# file.close()

# print("file converted")

# #Cleaning the dictionary file

# import re

# with open('C:/Users/ash5z/Desktop/Practical Assignment I/dzongkha_dictionary.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()


# dictionary = {}


# for line in lines:
    
#     line = line.strip()
    
    
#     dzongkha_words = re.findall(r'[\u0F00-\u0FFF]+', line)

    
#     if dzongkha_words:
        
#         dzongkha_text = ' '.join(dzongkha_words)
#         split_words = dzongkha_text.split("།")
#         for word in split_words:
#             word = word.strip()
#             if word:
#                 dictionary[word] = word
#         dictionary[dzongkha_text] = dzongkha_text  


# with open('C:/Users/ash5z/Desktop/Practical Assignment I/cleaned_dzongkha_dictionary.txt', 'w', encoding='utf-8') as file:
#     for word in dictionary.keys():
#         file.write(word + '\n')

# print(f"Processed {len(dictionary)} Dzongkha word entries.")

########################################################
import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Dzongkha_spell_checker.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    dictionary_file = "cleaned_dzongkha_dictionary.txt" 
    main(input_file, dictionary_file)

# Desc      : A python CLI program to get definition of English word
# Author    : Hiiruki <hi@hiiruki.dev>
# URL       : https://github.com/hiiruki/PyDict

import requests

print("""
 /$$$$$$$            /$$$$$$$  /$$             /$$    
| $$__  $$          | $$__  $$|__/            | $$    
| $$  \ $$ /$$   /$$| $$  \ $$ /$$  /$$$$$$$ /$$$$$$  
| $$$$$$$/| $$  | $$| $$  | $$| $$ /$$_____/|_  $$_/  
| $$____/ | $$  | $$| $$  | $$| $$| $$        | $$    
| $$      | $$  | $$| $$  | $$| $$| $$        | $$ /$$
| $$      |  $$$$$$$| $$$$$$$/| $$|  $$$$$$$  |  $$$$/
|__/       \____  $$|_______/ |__/ \_______/   \___/  
           /$$  | $$                                  
          |  $$$$$$/                                  
           \______/                                   

A Python CLI Program to Get Definition of English Word
                    by @hiiruki
                     
""")

# Ask for user input
word = input("Enter a word: ")

# Make API request
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
response = requests.get(url)

# Parse JSON data
data = response.json()

# Print information
print("\n")
print("-" * 50)
for item in data:
    print(f"\nWord     : {item['word']}")

    if 'phonetics' in item:
        print("Phonetics:")
        for phonetic in item['phonetics']:
            if 'text' in phonetic:
                print(f"\tText       : {phonetic['text']}")
            if 'audio' in phonetic:
                print(f"\tAudio      : {phonetic['audio']}")
            if 'sourceUrl' in phonetic:
                print(f"\tSource URL : {phonetic['sourceUrl']}")

    if 'meanings' in item:
        print("Meanings:")
        for meaning in item['meanings']:
            print(f"\tPart of Speech: {meaning['partOfSpeech']}")
            if 'definitions' in meaning:
                print("\tDefinitions:")
                for definition in meaning['definitions']:
                    print(f"\t\t- {definition['definition']}")
                    if 'synonyms' in definition:
                        print(f"\t\t  Synonyms: {', '.join(definition['synonyms'])}")
                    if 'antonyms' in definition:
                        print(f"\t\t  Antonyms: {', '.join(definition['antonyms'])}")
            if 'synonyms' in meaning:
                print(f"\tSynonyms: {', '.join(meaning['synonyms'])}")
            if 'antonyms' in meaning:
                print(f"\tAntonyms: {', '.join(meaning['antonyms'])}")

    if 'license' in item:
        print(f"License     : {item['license']['name']}")
        print(f"License URL : {item['license']['url']}")
    if 'sourceUrls' in item:
        print(f"Source URL  : {item['sourceUrls'][0]}")

    print("-" * 50)
    print("\n")

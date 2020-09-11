#  getting the sys module and setting command line args
import sys 
script, encoding, error = sys.argv

# define a function with 3 params
def main(language_file, encoding, errors):
    # reading the file that is given line by line
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<==>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)


"""
Breaking It
Rough ideas include the following:
1. Find strings of text encoded in other encodings and place them in the
ex23.py file to see how it breaks.
2. Find out what happens when you give an encoding that doesn’t exist.
 
2. Find out what happens when you give an encoding that doesn’t exist.
3. Extra challenging: Rewrite this using the b'' bytes instead of the UTF-8 strings, effectively reversing the script.
4. If you can do that, then you can also break these bytes by removing some to see what happens. How much do you need to remove to cause Python to break? How much can you remove to damage the string output but pass Python’s decoding system.
5. Use what you learned from item 4 to see if you can mangle the files. What errors do you get? How much damage can you cause and get the file past Python’s decoding system?
"""

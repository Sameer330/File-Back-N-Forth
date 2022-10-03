import os
import sys
import time
import json

filename = "test.txt"

with open(os.path.join(sys.path[0], filename), "r", encoding="utf-8") as file:
    letters = file.read()
    # Extract text from file
file.close()

file_size = len(letters)

char_list = []
# Stores char-by-char from file

char_locs = {}
# Stores { 'char': [list of indices] }

for char in letters:
    char_list.append(char)

char_locs['filename'] = filename
char_locs['filesize'] = file_size

for i in range(file_size):
    if char_list[i] not in char_locs:
        char_locs[char_list[i]] = []
        char_locs[char_list[i]].append(i)
    elif char_list[i] in char_locs:
        char_locs[char_list[i]].append(i)


with open(os.path.join(sys.path[0], "compressed.txt"), "w") as output:
    json.dump(char_locs, output)

print("Original: ", sys.getsizeof(char_list), "Bytes")

print("Compressed: ", sys.getsizeof(char_locs), "Bytes")
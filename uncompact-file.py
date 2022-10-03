import os
import sys
import time
import json

with open(os.path.join(sys.path[0], "compressed.txt"), "r") as input:
    data = json.load(input)

    input.close()

char_list = []

for i in range(data['filesize']):
    char_list.append(" ")

output = open(os.path.join(sys.path[0], "recovered.txt"), "w")
# char_list = str(char_list).replace("['", "")
# char_list = str(char_list).replace("']", "")



for key in data.keys():
    if type(data[key]) == str:
        continue
    elif type(data[key]) == list:
        for i in data[key]:
            char_list[i] = key

output = open(os.path.join(sys.path[0], "recovered.txt"), "w")

text = ""

for i in char_list:
    text += i

output.write(text)
output.close()

# Simulate the network topology with 'n' number of nodes and perform http request and a response
# along with suitable error code message
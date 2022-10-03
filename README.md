# File-Back-N-Forth

## Text File Conversion to JSON Format

A set of python scripts to convert a text file to JSON file and back to text file.

### How does it work?

    (I) Text File to JSON Format
        1. You give a text(.txt) file as input.
        2. The script iterates through the text content(character by character).
        3. Creates a dictionary(dict()) and add characters from text as keys.
        4. If character does not exist, creates and key and assigns an empty list to it
           and appends that character's index location.
        5. If character already exists, appends the index location of that character
           to existing list.
        6. This dictionary is written as is to a text file
    
    (II) JSON Format to Text File
        1. The script reads the JSON File as a dictionary data structure.
        2. First, the text length is read from the key - 'file_size'
        3. A list of whitespaces of length equal to 'file_size' is created.
        4. Then iterates through keys of the dictionary.
        5. For every key iteration, iterate through its list of indices.
        6. Place the key in the 'whitespaces list' in the indices mentioned in the list.
        7. (Optional) A key called 'filename' also exists.

### Created by Sameer Ankalagi
### GitHub.com/Sameer330

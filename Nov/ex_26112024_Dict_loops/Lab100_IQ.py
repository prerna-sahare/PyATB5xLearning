# write a program to find the frequency of each character in given string

string="automation"

char_count={}

for char in string:
    char_count[char]=char_count.get(char,0)+1

    print(char_count)
# find Vowels
input_string="hello, world!"

vowels="aeiou"

vowels_count=0

for char in input_string:
    if char in vowels:
        vowels_count=vowels_count+1

print(vowels_count)
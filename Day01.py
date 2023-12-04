import re

# Find digits written out
digit_words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_digits_written_out(line):
    for word, digit in digit_words.items():
        line = line.replace(word, word+digit+word)
    return line

total = 0

with open('Day01.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line2 = find_digits_written_out(line)
        match1 = re.search(r'\d', line2)
        first_digit = match1.group()
        reverse = line2[::-1]
        match2 = re.search(r'\d', reverse)
        last_digit = match2.group()
        number = first_digit + last_digit
        total += int(number)

print(f"The total is: {total}")






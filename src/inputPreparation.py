import sys
import random
import string

if len(sys.argv) != 3:
    print("Usage: python inputPreparation.py <k> <length>")
    sys.exit(1)
try:
    k = int(sys.argv[1])
    length = int(sys.argv[2])
except ValueError:
    print("Error: Both k and length must be integers.")
    sys.exit(1)
    
if not (1 <= k <= 26):
    print("Error: k must be between 1 and 26 (inclusive).")
    sys.exit(1)
if length <= 0:
    print("Error: length must be a positive integer.")
    sys.exit(1)
    
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(string.ascii_lowercase[:k])

# random.choices picks randomly from the alphabet with replacement
string_A = "".join(random.choices(alphabet, k=length))
string_B = "".join(random.choices(alphabet, k=length))

try:
    with open("input.txt", "w") as file:
        # Write K
        file.write(f"{k}\n")
        
        # Write characters and their random weights (1 to 10)
        for char in alphabet:
            weight = random.randint(1, 10)
            file.write(f"{char} {weight}\n")
            
        # Write the two strings
        file.write(f"{string_A}\n")
        file.write(f"{string_B}")
    
except IOError as e:
    print(f"Error writing to file: {e}")
    sys.exit(1)
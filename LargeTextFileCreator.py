import random
from string import ascii_letters
import time
import os

# Open the file
file = open("text.txt", "w", encoding="utf-8")  

num_repeats = int(input("How many groups of letters should be written? > "))
letters_per_group = 32767

current_write = 0

for _ in range(num_repeats):
    start_time = time.time()  

    random_letters = "".join(random.choices(ascii_letters, k=letters_per_group))

    file.write(random_letters)

    current_write += 1
   

    # Print information about the written group
    print(f"Successful writes: {current_write}/{num_repeats}")

# Close the file and calculate average writing time
file.close()

#

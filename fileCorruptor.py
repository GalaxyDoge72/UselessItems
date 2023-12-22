from tkinter import filedialog
import os

filetoCorrupt = filedialog.askopenfilename()  # Use askopenfilename to get the file path
file_size = os.path.getsize(filetoCorrupt)

if file_size == 0:
    print("Cannot corrupt an empty file.")
else:
    print(f"This file has {file_size} bytes that can be corrupted.")
    amount_to_corrupt = int(input("How many bytes should be corrupted? > "))

    # Generate random bytes
    random_bytes = os.urandom(amount_to_corrupt)

    amount_corrupted = 0

    with open(filetoCorrupt, 'rb+') as file:
        # Seek to a random position in the file
        if file_size > 0:
            file.seek(os.urandom(4)[0] % file_size)

            # Write the random bytes to the file
            file.write(random_bytes)

            amount_corrupted += len(random_bytes)
            print(f"Corrupted {amount_corrupted}/{amount_to_corrupt} bytes in {filetoCorrupt}")

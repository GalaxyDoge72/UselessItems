from tkinter import filedialog
import os

numFolder = int(input("How many folders should be made? (It is not recommended to select anything that there is already files in. [e.g. Desktop]) > "))
currentPath = filedialog.askdirectory()
foldersCreated = 0
for index in range(numFolder):
    foldersCreated += 1
    directory = str(foldersCreated)
    path = os.path.join(currentPath, directory)
    os.mkdir(path)
    print(f"Folders created: {foldersCreated}/{numFolder}")
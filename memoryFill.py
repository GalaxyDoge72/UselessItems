print("This will fill your computers memory. To free up the memory, close the window.")

def fill_memory():
    try:
        memory_list = []
        while True:
            # Append a large object to the list
            memory_list.append(" " * (1024 * 1024))  # Appending 1 MB of data
    except MemoryError:
        print("Memory exhausted.")

fill_memory()

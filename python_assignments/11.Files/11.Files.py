# 1. Read text file
def read_text_file():
    with open(r"C:/Users/Syed Kaif/OneDrive/Desktop/jala_academy/Python PDFS/python_assignments/11.Files/sample.txt", "r") as f:
        content = f.read()
    print("\n1. File Content:\n", content)
read_text_file()


# 2. Write text to .txt file using file write (Python doesn't use InputStream, but file handling)
def write_text_file():
    text = "Hello, this is a sample text."
    with open("sample_write.txt", "w") as f:
        f.write(text)
    print("\n2. Written to sample_write.txt")
write_text_file()

# 3. Read file stream (reading line by line)
def read_file_stream():
    print("\n3. Reading file line by line:")
    with open(r"C:/Users/Syed Kaif/OneDrive/Desktop/jala_academy/Python PDFS/python_assignments/11.Files/sample.txt", "r") as f:
        for line in f:
            print(line.strip())
read_file_stream()

# 4. Read file stream with random access using seek()
def read_file_random_access():
    with open(r"C:/Users/Syed Kaif/OneDrive/Desktop/jala_academy/Python PDFS/python_assignments/11.Files/sample.txt", "r") as f:
        f.seek(5)  # move to 5th byte
        content = f.read(10)  # read next 10 bytes
    print("\n4. Random Access Read:", content)
read_file_random_access()

# 5. Read file up to a particular index using seek()
def read_file_to_index(index=10):
    with open(r"C:/Users/Syed Kaif/OneDrive/Desktop/jala_academy/Python PDFS/python_assignments/11.Files/sample.txt", "r") as f:
        f.seek(0)
        content = f.read(index)
    print(f"\n5. Read up to index {index}:", content)
read_file_to_index(15)

# 6. Check read and write permissions on a file
import os

def check_file_permissions(filename="sample.txt"):
    can_read = os.access(filename, os.R_OK)
    can_write = os.access(filename, os.W_OK)
    print(f"\n6. Permissions for {filename} - Read:", can_read, ", Write:", can_write)
check_file_permissions("sample.txt")

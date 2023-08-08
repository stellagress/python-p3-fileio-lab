# def write_file(file_name, file_content):
#     with open(file_name, mode='w', encoding='utf-8') as file:
#         file.write(file_content)


def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as file:
        file_content = file.read()
    return file_content


# Lets practice! In the file file_io.py write a function called write_file that takes in the arguments file_name and file_content.

# The file_name can be a combined file path/name, you will need to add the .txt file extension to the file_name when opening a file.

# This function should use file_name included and file_content to write a .txt file.

# Write a append_to_file function that takes in the same parameters and appends to the .txt file.

# Write a read_file function that takes in a file name and returns the content of the .txt file.

# Example usage:

# # use write_file function. 
# write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
# append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

# read_file(file_name="logfile")
# # Log 1: 5 bananas added
# # Log 2: 3 bananas subtracted
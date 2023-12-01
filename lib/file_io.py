def write_file(file_name, file_content):
    file_path = f"{file_name}.txt"
    with open (file_path, "w") as file:
        file.write (file_content)

def append_file(file_name, append_content):  
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
    pass

def read_file(file_name):
    with open (f"{file_name}.txt") as f:
     return f.read ()
    pass

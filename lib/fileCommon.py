import os


def check_exits_file(file):
    if not os.path.exists(file):
        print(f"File {file} not found.")
        exit()
        
def is_pdf(file):
    file_art = file.split(".")[-1:]
    if (file_art[0] != 'pdf'): 
        print(f"File is not an PDF")
        exit()
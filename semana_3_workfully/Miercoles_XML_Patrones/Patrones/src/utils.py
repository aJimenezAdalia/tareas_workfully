

def choose_reader_object(file_path):
    extensions = ['csv', 'lsx', 'tsv']

    file_extension = file_path[-3:]

    if file_extension in extensions:
        return file_extension
    else:
        return "Extension not available."



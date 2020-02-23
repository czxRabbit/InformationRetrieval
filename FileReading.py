def Read_file(file_dir):
    file = open(file_dir, 'r')
    file_content = file.read()
    return file_content

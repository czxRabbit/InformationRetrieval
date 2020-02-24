def Read_file(file_dir):
    file = open(file_dir, 'rb')
    file_content = file.read().decode('utf-8')
    return file_content

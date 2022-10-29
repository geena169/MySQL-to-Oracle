# Ввод файла с помощью генератора
def get_line(file_name):

    with open(file_name, encoding="utf-8", errors='ignore') as f:
        for line in f:
            yield line

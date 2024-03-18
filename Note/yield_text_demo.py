def file_reader(file_path):
    with open(file_path) as f:
        for line in f:
            yield line


for line in file_reader("large_file.txt"):
    print(line, end="")


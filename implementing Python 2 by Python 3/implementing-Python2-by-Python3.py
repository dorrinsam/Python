import re


def convert_oiadsnfiasndonoifdndifnoidsanoidsafoidsan(text):
    file1 = text.replace("quit()", "exit()")
    file2 = ""

    for line in file1.split("\n"):
        regex = re.findall(r"print (.{0,})", line)

        for i in regex:
            line = line.replace(" " + i, "(" + i + ")")
        file2 += line + "\n"

    return file2


while True:
    exec(convert_oiadsnfiasndonoifdndifnoidsanoidsafoidsan(input()))

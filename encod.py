import sys
import os
import chardet
import subprocess
import webbrowser


def main():
    file_name = sys.argv[1]
    file_path = os.path.abspath(file_name)

    with open(file_path, 'rb') as first:
        dicts = chardet.detect(first.read())
        encod = dicts['encoding']

    if encod != 'UTF-8':
        with open(file_path, 'r', encoding=encod) as f:
            text = f.read()

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)

    subprocess.call(["open", "-a", "TextEdit", file_path])

    with open(file_path, 'r') as inf:
        inf_l = [i for j in inf for i in j.split(' ') if 'http' in i]
        for i in inf_l:
            webbrowser.open(i)


if __name__ == '__main__':
    main()

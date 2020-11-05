from typing import TextIO
from appJar import gui


def script_converter():
    i = 0
    file: TextIO
    with open("in.txt", "r", encoding="utf-8") as openfileobject, open("out.txt", "w", encoding="utf-8") as export:
        for stuff in openfileobject:
            line = stuff.rstrip()
            export.write('" {} "\n'.format(stuff))
            i += 1

def script_converter_file(file):
    i = 0
    file: TextIO
    with open(file, "r", encoding="utf-8") as openfileobject, open("out.txt", "w", encoding="utf-8") as export:
        for stuff in openfileobject:
            line = stuff.rstrip()
            export.write('" {} "\n'.format(stuff))
            i += 1

    print("process done total changed script number: " + str(i))


if __name__ == '__main__':
    app = gui()

    app.addLabel("title", "렌파이 스크립트 변환기 0.01 by 리미티드 팩토리")
    app.addTextArea("t1", script_converter())
    app.addFileEntry("f1")

    app.go()

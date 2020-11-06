from typing import TextIO
from appJar import gui
import sys


def script_loader():
    file: TextIO
    initialize: TextIO
    with open("in.txt", "w", encoding="utf-8") as initialize:
        # converting textbox into txt file
        texts = app.getTextArea("t1")
        initialize.write(texts)

        app.infoBox("info1", "Script Loaded (스크립트 로드 완료)", parent=None)


def script_converter():
    i = 0
    with open("in.txt", "r", encoding="utf-8") as openfileobject, open("out.txt", "w", encoding="utf-8") as export:
        for stuff in openfileobject:
            line = stuff.rstrip()
            export.write('" {} "\n'.format(stuff))
            i += 1

    #for the output in the t2 box

    with open("out.txt", "r", encoding="utf-8") as text_output:
        for stuff in text_output:
            app.setTextArea("t2", stuff, end=True, callFunction=True)

    info2idea = "total converted lines (변환된 라인 수): " + str(i)
    app.infoBox("info2", info2idea , parent=None)

#TODO with the file type support

# def script_converter_file(file=""):
#     i = 0
#     file: TextIO
#     with open(file, "r", encoding="utf-8") as openfileobject, open("out.txt", "w", encoding="utf-8") as export:
#         for stuff in openfileobject:
#             line = stuff.rstrip()
#             export.write('" {} "\n'.format(stuff))
#             i += 1
#
#     print("process done total changed script number: " + str(i))


#TODO Setting varliable support


if __name__ == '__main__':
    app = gui()

    app.addLabel("title", "Renpy Script Converter by Limited Factory V0.01")
    app.addScrolledTextArea("t1")
    app.addScrolledTextArea("t2")
    # app.addFileEntry("f1")
    app.addButton('load', script_loader)
    app.addButton('convert', script_converter)
    app.setFont(size=16, family="Arial", underline=False)

    app.go()
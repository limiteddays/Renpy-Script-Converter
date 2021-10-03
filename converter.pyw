from typing import TextIO
from appJar import gui
import sys


class converter():

    def __init__(self, rule, name):
        self.rule = ""
        self.name = {}

    def script_loader(self):
        file: TextIO
        initialize: TextIO
        with open("in.txt", "w", encoding="utf-8") as initialize:
            # converting textbox into txt file
            texts = app.getTextArea("t1")
            initialize.write(texts)

            app.infoBox("info1", "Script Loaded (스크립트 로드 완료)", parent=None)

    def script_converter(self):

        i = 0
        with open("in.txt", "r", encoding="utf-8") as openfileobject, open("out.txt", "w", encoding="utf-8") as export:
            for stuff in openfileobject:
                # changing the value

                line = stuff.rstrip()
                export.write('" {} "\n'.format(stuff))
                i += 1

        # for the output in the t2 box
        with open("out.txt", "r", encoding="utf-8") as text_output:
            for stuff in text_output:
                app.setTextArea("t2", stuff, end=True, callFunction=True)

        info2idea = "total converted lines (변환된 라인 수): " + str(i)

    # for setting the name
    def name_set(self):
        with open("name.txt", "r", encoding="utf-8") as name_out:
            for stuff in name_out:
                name_ini = stuff.split(":")

                name_get = str(name_ini[0])
                name_ini = str(name_ini[1])

                self.name[name_get] = name_ini
                print(self.name)

    # for setting the char_value
    def set_char_var(self):
        name = app.getEntry("char_var")
        ini = app.getEntry("char_ini")

        if name == "" or ini == "":
            app.infoBox("info4", "Some statements are missing (하나 이상의 변수가 빠졌습니다.)", parent=None)

        else:
            stuff = str(name) + ":" + str(ini) + "\n"

            with open("name.txt", "a", encoding="utf-8") as name_in:
                name_in.write(stuff)

            with open("name.txt", "r", encoding="utf-8") as name_out:
                app.clearTextArea("char_var_list", callFunction=True)
                for stuff in name_out:
                    app.setTextArea("char_var_list", stuff, end=True, callFunction=True)

            self.name_set()

            app.infoBox("info5", "Successfully added. (성공적으로 추가되었습니다.)", parent=None)

    def clear_name(self):
        app.clearTextArea("char_var_list", callFunction=True)
        with open("name.txt", "w", encoding="utf-8") as name_in:
            name_in.write("")

        app.infoBox("info6", "Successfully cleared. (성공적으로 삭제되었습니다.)", parent=None)

    def set_rule(self, rule):
        self.rule = rule

    def reset_rule(self):
        self.rule = ""

    def get_list(self):
        return self.chr_variable

    # TODO with the file type support

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


if __name__ == '__main__':
    app = gui("Notebook", useTtk=True)
    app.setTtkTheme("clam")
    app.startNotebook("Notebook")

    app.startNote("Introduction")
    app.setFont(size=30, family="Arial", underline=False)
    app.addLabel("l6", "V0.1.1")
    app.addLabel("l1", "Renpy Script Converter by Limited Factory ")
    app.stopNote()

    # Starting note 1
    app.startNote("Main page")
    app.addLabel("l20", "This is the main page to put your scripts in and convert it")
    app.addLabel("l21", "To rego the character variables, go to setting variables page up there")

    app.addScrolledTextArea("t1")
    app.addScrolledTextArea("t2")

    # app.addFileEntry("f1")
    app.addButton('load', converter.script_loader)
    app.addButton('convert', converter.script_converter)
    app.setFont(size=30, family="Arial", underline=False)

    app.stopNote()

    # starting note 2

    # TODO work on the setting variable page
    app.startNote("Setting variables")

    app.addLabel("l2", "This page is for setting up the character names (캐릭터 이름을 설정하는 페이지입니다)")
    app.addLabel("l3", "Ex) Hana:I am the god! (하나: 내가 신이다!)")
    app.addLabel("l4", "Output) Hana:'I am the god!' (h '내가 신이다!')")

    app.addEntry("char_var")
    app.addEntry("char_ini")
    app.addLabel("l5", "These are values that are in the name.txt right now (name.txt 파일에 있는 이름 변수들입니다.)")
    app.addScrolledTextArea("char_var_list", text=None)
    app.setEntryDefault("char_var", "put character name ex) Hana (캐릭터 이름을 설정해 주세요 예) 하나)")
    app.setEntryDefault("char_ini", "put character initial to use in renpy ex) h (캐릭터 이니셜을 설정해 주세요 예) h")

    app.addButton('Set character variable', converter.set_char_var)
    app.addButton('Clear Character Variable', converter.clear_name)

    app.stopNote()

    app.stopNotebook()
    app.go()

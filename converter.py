i = 0
with open("in3.txt", "r", encoding="utf-8") as f, open("out3.txt", "w", encoding="utf-8") as export:
    while True:
        line = f.readline()
        line = line.rstrip()
        # if line == '':
        #     i += 1
        #     continue
        #
        # if line == '#':
        #     i += 1
        #     continue
        #
        # if line == "s":
        #     i += 1
        #     continue
        #
        # if line == "j":
        #     i += 1
        #     continue
        #
        # if line == "e":
        #     i += 1
        #     continue

        export.write('" {} "\n'.format(line))
        # else:
        #




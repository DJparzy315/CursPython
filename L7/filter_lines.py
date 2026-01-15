def filter_lines(input_file, output_file, keyword):
    with open(input_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(output_file, "w", encoding="utf-8") as fout:
        for line in lines:
            if keyword in line:
                fout.write(line)


# test
filter_lines("input.txt", "filtered.txt", "Python")

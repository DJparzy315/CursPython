def reverse_lines(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(output_file, "w", encoding="utf-8") as fout:
        for line in lines:
            # eliminam newline, inversam linia si o scriem inapoi
            fout.write(line.rstrip()[::-1] + "\n")


# test
reverse_lines("input.txt", "output.txt")

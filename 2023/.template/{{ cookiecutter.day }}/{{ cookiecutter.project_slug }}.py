def {{ cookiecutter.main_method }}(lines):
    pass

if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print({{ cookiecutter.main_method }}(lines))

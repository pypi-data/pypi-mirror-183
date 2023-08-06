def read_file(path_to_file: str) -> str:
    with open(path_to_file) as fin:
        return fin.read()


def write_file(path_to_file: str, new_contents: str) -> None:
    with open(path_to_file, 'w') as fout:
        fout.write(new_contents)

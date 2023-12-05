import os


def read_input(script_path: str, part: int = 0) -> str:
    py_filename = os.path.basename(script_path)
    basename, _ = os.path.splitext(py_filename)

    filename = f"input/{basename}.txt" if not part else f"input/{basename}-{part}.txt"

    with open(filename) as f:
        content = f.read()
    return content

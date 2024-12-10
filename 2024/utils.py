import os


def read_input(script_path: str, part: int = None, remove_suffix: bool = True) -> str:
    py_filename = os.path.basename(script_path)
    basename, _ = os.path.splitext(py_filename)

    basename = basename.split("_")[0] if remove_suffix else basename
    filename = f"input/{basename}.txt" if not part else f"input/{basename}-{part}.txt"

    with open(filename) as f:
        content = f.read()
    return content

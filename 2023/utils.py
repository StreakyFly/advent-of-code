def read_input(file_name: str) -> str:
    with open(f"input/{file_name}") as f:
        content = f.read()
    return content

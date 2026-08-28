from importlib import resources

def read_template(file_name: str):
    target_file = resources.files(__package__).joinpath("templates", file_name)

    return target_file.read_text(encoding="UTF-8")
def pull_text(file_name: str) -> str:
    file = open(file_name, "r")
    text = str(file.read())
    file.close()
    return text

def write_summary_to_file(file_name: str, text: str):
    file_prefix = file_name.split(".")[0]
    file = open(file_prefix + "summary.txt", "a")
    file.write(text)
    file.close()

def log_message(level: str, message: str):
    print("[{}]: {}".format(level, message))

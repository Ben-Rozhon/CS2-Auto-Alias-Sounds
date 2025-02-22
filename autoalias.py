import re
import requests

def process_line(line, line_num):
    # Check if the line contains the "play" command followed by any non-whitespace path
    if not re.match(r'^play\s+\S+', line):
        print(f"Line {line_num} is invalid: {line.strip()}")
        return None

    # Extract the path from the "play" command
    parts = line.strip().split(maxsplit=1)
    if len(parts) != 2:
        print(f"Line {line_num} is invalid: {line.strip()}")
        return None
    command, path = parts

    # Extract only the file name from the path (after the last slash)
    file_name = path.split('/')[-1]

    # Capitalize the first letter after each underscore in the file name
    sub_parts = file_name.split('_')
    alias_name = "SOUND" + sub_parts[0] + ''.join(word.capitalize() for word in sub_parts[1:])

    # Create the alias command
    alias_command = f'alias {alias_name} "{command} {path}"'
    return alias_command

def main():
    url = "https://raw.githubusercontent.com/armync/ArminC-CS2-Cvars/refs/heads/main/sounds/sounds_cvar.txt"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the file from the URL.")
        return

    lines = response.text.splitlines()

    with open('output.txt', 'w', encoding='utf-8') as outfile:
        for line_num, line in enumerate(lines, start=1):
            result = process_line(line, line_num)
            if result:
                outfile.write(result + '\n')
    print("Output written to 'output.txt'")

if __name__ == "__main__":
    main()

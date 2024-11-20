import re

def process_line(line, line_num):
    # Check if the line contains the "play" command followed by a file path
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

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_num, line in enumerate(infile, start=1):
            result = process_line(line, line_num)
            if result:
                outfile.write(result + '\n')

def main():
    input_file = 'input.txt'  # Change this to your input file name
    output_file = 'output.txt'  # Change this to your output file name
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()

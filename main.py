import sys

# Command dictionary
command_dict = {
  # your command here
  # "hello_world": "print('Hello, world!')"
}

def command_parser(line):
    mod_line = line
    for command in command_dict:
        if command in line:
            mod_line=mod_line.replace(command, command_dict[command])
    exec(mod_line)

if __name__ == '__main__':
    if len(sys.argv) != 2: 
        print("Your usage here.") # Your usage here
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        command_parser(file.read())

import os

cmd = input()

while cmd != 'End':

    cmd = cmd.split('-')
    command, file_name = cmd[0], cmd[1]

    if command == 'Create':
        open(file_name, 'w').close()

    elif command == 'Add':
        content = cmd[2]

        with open(file_name, 'a') as file:
            file.write(content)
            file.write('\n')

    elif command == 'Replace':
        old_string = cmd[2]
        new_string = cmd[3]
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                file_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(file_content)
        else:
            print("An error occurred")

    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    cmd = input()

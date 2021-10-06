import os

def traverse_folder(current_root, f_dict):
    for el in os.listdir(current_root):
        full_path = os.path.join(current_root, el)
        if os.path.isfile(full_path):
            ext = el.split('.')[-1]
            if ext not in f_dict:
                f_dict[ext] = []
            f_dict[ext].append(el)
        elif os.path.isdir(full_path):
            traverse_folder(full_path, f_dict)



files_dict = {}
traverse_folder(os.getcwd(), files_dict)

sorted_files_dict = {key: val for key, val in sorted(files_dict.items())}


with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\output.txt'), 'w') as output:
    for key, val in sorted_files_dict.items():
        output.write(f".{key}")
        output.write("\n")
        for file in sorted(val):
            output.write(f"- - - {file}")
            output.write("\n")

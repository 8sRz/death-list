import os

folder_path = "./formats"

with open(os.path.join(folder_path, 'base.txt'), 'r') as file:
    lines = file.readlines()

with open(os.path.join(folder_path, 'ABP.txt'), 'w') as file:
    file.writelines([f"||{line.strip()}^\n" for line in lines])

with open(os.path.join(folder_path, 'personalDNSfilter.txt'), 'w') as file:
    file.writelines([f"*.{line}" for line in lines])

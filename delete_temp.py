import os

file_to_delete = r"d:\eskoolwork\rename_files.py"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"Deleted {file_to_delete}")
else:
    print(f"File {file_to_delete} not found.")

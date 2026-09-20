import os
file_path = "first.exe"
if os.path.exists(file_path):
    print(f"the file path exists in the location {file_path} ")
else:
    print("the file path doesnt exists")

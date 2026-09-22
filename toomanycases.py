import os
file_path = "C:\\Users\\nukeg\\OneDrive\\Desktop\\wtf.txt"
if os.path.exists(file_path):
    print(f"the file path exists in the location {file_path} ")
    if os.path.isfile(file_path):
        print("That is a file")
    else:
        print("That is not a file")
else:
    print("the file path doesnt exists")

import pathlib
import os

# path1 = pathlib.Path.home() /"my_folder"
# path2 = pathlib.Path("C:/Users/OLAITAN BLESSING/my_folder")/"image"
# path2.mkdir(exist_ok=True)
path1 = pathlib.Path("C:/Users/OLAITAN BLESSING/my_folder")
path2 = pathlib.Path("C:/Users/OLAITAN BLESSING/my_folder/image")
# files_path = [
#     path1 / "file1.txt",
#     path1 / "file2.txt",
#     path1 / "image1.pmg",
# ]
# for path in files_path:
#     path.touch()
#     print(path1)

# source = path1.parent/"my_folder" / "image1.pmg"
# print(source.exists())
# destination = path1 / "image" / "image1.pmg"
# print(destination.exists())
# source.replace(destination)

# path3 = pathlib.Path("C:/Users/OLAITAN BLESSING/my_folder/file1.txt")
# path3.unlink()
path4 = pathlib.Path("C:/Users/OLAITAN BLESSING/my_folder")
path4.rmdir()

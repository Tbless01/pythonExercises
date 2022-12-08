import pathlib

path = pathlib.Path("C:/Users/OLAITAN BLESSING/my_folder/image")

files_path = [
    path / "image1.png",
    path / "image2.gif",
    path / "image3.png",
    path / "image4.jpg",
]
for path in files_path:
    path.touch()
    
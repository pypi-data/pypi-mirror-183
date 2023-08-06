# Makes it easier to access Documents/Pictures/Desktop/Music/Videos/Downloads

```python

from winuserfolder import *

print(get_desktop_folder_path())
print(get_documents_folder_path())
print(get_downloads_folder_path())
print(get_music_folder_path())
print(get_pictures_folder_path())
print(get_videos_folder_path())
a = create_folder_in_documents_folder("00testestest")
b = create_folder_in_pictures_folder("00testestest")
c = create_folder_in_desktop_folder("00testestest")
d = create_folder_in_music_folder("00testestest")
e = create_folder_in_videos_folder("00testestest")
f = create_folder_in_downloads_folder("00testestest")
a1 = touch_file_in_documents_folder(relative_path="00testestest\\xxx\\myfile.txt")
b1 = touch_file_in_pictures_folder(relative_path="00testestest\\xxx\\myfile.txt")
c1 = touch_file_in_desktop_folder(relative_path="00testestest\\xxx\\myfile.txt")
d1 = touch_file_in_music_folder(relative_path="00testestest\\xxx\\myfile.txt")
e1 = touch_file_in_videos_folder(relative_path="00testestest\\xxx\\myfile.txt")
f1 = touch_file_in_downloads_folder(relative_path="00testestest\\xxx\\myfile.txt")

    
```





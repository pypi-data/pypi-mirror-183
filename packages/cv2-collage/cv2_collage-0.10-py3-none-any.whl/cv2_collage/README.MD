<h2>Create a collage from images with OpenCV </h2>


```python

from cv2_collage import create_collage

lst = [
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/2022-12-27%2003_40_27-.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/2022-12-27%2003_49_27-.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/2022-12-27%2004_01_57-.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/2022-12-27%2004_02_09-.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/colorfind1.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/colorfind2.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/colorfind3.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/colorfind4.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/zoompics_0000006.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/zoompics_0000007.png",
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/zoompics_0000008.png",
]


from numpy_choices import get_random_items_from_list

coldone = create_collage(
    lst=get_random_items_from_list(lst, 16),
    width=1000,
    background=(0, 0, 0),
    save_path=r"F:\cv2mergepics\m\tetete.png",
)




```

<img src="https://github.com/hansalemaos/screenshots/raw/main/collage.png"/>



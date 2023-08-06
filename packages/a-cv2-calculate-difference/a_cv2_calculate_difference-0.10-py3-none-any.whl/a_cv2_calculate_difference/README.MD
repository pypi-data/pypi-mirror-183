<h2>Calculates the difference between 2 images</h2>


```python
from a_cv2_calculate_difference import check_before_after
rect = check_before_after(
    "https://github.com/hansalemaos/screenshots/raw/main/colorfind3.png",
    r"https://github.com/hansalemaos/screenshots/raw/main/colorfind1.png",
    show_results=False,
    return_image=True,
    color=(255, 0, 0),
)

print(rect[0])
[(93, 150, 39, 18), (100, 137, 26, 13), (150, 117, 15, 15), (100, 100, 50, 32)]


```


<img src="https://github.com/hansalemaos/screenshots/raw/main/colorfind3.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/colorfind1.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/imagediffsquare.png"/>



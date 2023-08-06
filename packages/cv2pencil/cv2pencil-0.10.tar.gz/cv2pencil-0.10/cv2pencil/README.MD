<h2>Converts images to pencil sketches</h2>


```python

$pip install cv2pencil

from cv2pencil import get_pencil_drawing
# Allowed image formats: url/path/buffer/base64/PIL/np
# save_diff / save_norm are optional
a, b = get_pencil_drawing(
    r"https://raw.githubusercontent.com/hansalemaos/screenshots/main/merg1.png",
    dilate=(9, 9),
    blur=7,
    save_diff="f:\\pencildrawing\\diff.png",
    save_norm="f:\\pencildrawing\\norm.png",
)


```

<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/merg1.png"/>


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/diff.png"/>


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/norm.png"/>
<h2>Stacks 2 images (horizontal/vertical)</h2>


```python

$pip install cv2-stack-images
from cv2_stack_images import concat2images

# Allowed image formats: url/path/buffer/base64/PIL/np
# You must pass either width or height, but not both!
# save_path is optional

b1 = concat2images(
    img1=r"https://github.com/hansalemaos/screenshots/raw/main/colorfind3.png",
    img2=r"https://github.com/hansalemaos/screenshots/raw/main/pic4.png",
    width=300,
    save_path="f:\\concatimg\\vertical.png",
)
b2 = concat2images(
    img1=r"https://github.com/hansalemaos/screenshots/raw/main/colorfind3.png",
    img2=r"https://github.com/hansalemaos/screenshots/raw/main/pic4.png",
    height=300,
    save_path="f:\\concatimg\\horizontal.png",
)

```

<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/vertical.png"/>


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/horizontal.png"/>

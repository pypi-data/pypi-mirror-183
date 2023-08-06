# Creates new/empty cv2 images/numpy arrays 

```python
$pip create-empty-image

from create_empty_image import create_new_image, create_new_image_same_size

a = create_new_image_same_size(
    openimage=r"https://github.com/hansalemaos/screenshots/raw/main/papag_00000003.png",
    color=(255, 255, 0),  # rgb
)

b = create_new_image(width=200, height=300, color=(0, 0, 120, 255))  # rgba
c = create_new_image(width=200, height=300, color=(120,))  # gray

```





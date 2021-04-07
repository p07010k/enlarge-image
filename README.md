# enlarge-image
This script enlarges an image without smoothing its pixels. This is useful when creating pixel art.
Made by p07010k in August 2020.

## Requirements
Python Imaging Library is needed. Install from pip:
```
pip install Pillow
```

## Usage
```
>enlarge_image.py path_to_the_image scaling_coefficient
```
For example, we have a pixel-art picture, like this:
![p07010k.bmp](examples/p07010k.bmp)
And we want to enlarge it by the scaling factor of 8:
```
>enlarge_image.py p07010k.bmp 8
Enlarged image saved as p07010k.bmp_out.png
```
The picture we get:
![p07010k.bmp_out.png](examples/p07010k.bmp_out.png)


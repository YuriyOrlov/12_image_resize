# Image Resizer

This program changes the size of your image and/or its format. You need to pass the path to the file, and then specify the settings of necessary changes. Moreover, you can increase or decrease the image size by multiplying it by the desired number or you can do this by indicating percent. You can specify the required height or width of the image separately or you can also pass both parameters together. However, if the aspect ratio of the image is wrong, the program will warn you about it. The program works with two file formats PNG and JPEG. By default a file will be saved in JPEG. 

Example of program run.

```#!bash
$ python image_resize.py 2017.jpg
File created.

```
If you specify keys, which cannot work together, for example `-scale` and `-width` script will return you an error:

```#!bash
$ python image_resize.py 2017.jpg -scale 2 -width 1555
Traceback (most recent call last):
  File "image_resize.py", line 41, in <module>
    args.enlarge_scale, args.reduce_scale)
  File "image_resize.py", line 33, in get_type_of_resize
    raise ValueError('Too many keys. Please, remove some keys from the row.')
ValueError: Too many keys. Please, remove some keys from the row.

```

In this case just remove some unneeded keys and rerun program.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

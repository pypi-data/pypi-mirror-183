# Write/read from memory instead of files when open() is called 

## @read_decorator fakes the existence of a file and provides the file content when open(mode='r'/mode='rb') from the builtins is called. 
## @write_decorator captures the output when open(mode='w'/mode='wb') from the builtins is called. 

#### The decorators don't work with functions/methods that don't use the open() function (for example: cv2.imread / cv2.imwrite)

### Some examples 
```python
import pandas as pd
import cv2
from PIL import Image
import numpy as np
import os.path
from fake_read_write_files import read_decorator, write_decorator

@read_decorator
def readutf8(filename, _file_data):
    with open(filename, mode="r", encoding="utf-8") as f:
        data = f.read()
    return data


@write_decorator
def write_pil_image(pilpic, filepath):
    pilpic.save(filepath)
    # don't use "return" here, the function will return a dict


@read_decorator
def read_bin_file(filename, _file_data):
    with open(filename, mode="rb") as f:
        data = f.read()
    return data


@read_decorator
def pandasread(filename, _file_data):
    return pd.read_csv(filename)


@write_decorator
def pandaswrite(df, filename):
    df.to_csv(filename)
    # don't use "return" here, the function will return a dict


# the read decorator always checks for the kwarg "_file_data"
# It must be passed as a kwarg
e = readutf8(
    filename="f:\\txtdoesnotexist.txt", _file_data="I am fake\nDid you know that?"
)
print(e)

# real file
bi = Image.open(r"C:\Users\Gamer\anaconda3\envs\dfdir\xxxxxxxxxx.png")

# writing to a fake file, returns a dict with all written files in the function,
# even if there is no return value declared
o = write_pil_image(bi, filepath="i_am_a_fake_image.png")
print(
    cv2.imdecode(np.frombuffer(o["i_am_a_fake_image.png"], np.uint8), cv2.IMREAD_COLOR)
)


binaryfile = read_bin_file(
    filename="i_am_a_fake_image.png", _file_data=o["i_am_a_fake_image.png"]
)


df = pandasread(filename="test.csv", _file_data="john,1\nmaria,2\ncarlos,3")
print(df)

pdcsv = pandaswrite(df, filename="test.csv")
print(pdcsv)


# output 
I am fake
Did you know that?
[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [254 255 255]
  [253 255 255]]
 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [254 255 255]
  [253 255 255]]
 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [254 255 255]
  [253 255 255]]
 ...
 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 254]
  [255 255 254]
  [255 255 254]]
 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 254]
  [255 255 254]
  [255 255 254]]
 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 254]
  [255 255 254]
  [255 255 254]]]
     john  1
0   maria  2
1  carlos  3
{'test.csv': ',john,1\r\n0,maria,2\r\n1,carlos,3\r\n'}


```




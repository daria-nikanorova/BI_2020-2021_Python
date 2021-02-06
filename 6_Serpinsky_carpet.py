import numpy as np
from PIL import Image

repeat = 6
image_size = 3**repeat

# image a black square
square = np.empty([image_size, image_size, 3], dtype=np.uint8)

for i in range(0, repeat + 1):
    step = 3**(repeat - i)
    for x in range(0, 3**i):
        if x % 3 == 1:
            for y in range(0, 3**i):
                if y % 3 == 1:
                    square[y * step:(y + 1)*step, x * step:(x + 1)*step].fill(50*i)

save_file = "6_Serpinsky_carpet.png"
Image.fromarray(square).save(save_file)


import math
import numpy as np
import fourier_transform as ft
from PIL import Image

def __sampling_image(img, n_x, n_y):
    h, w = img.shape
    result = []

    for x in range(0, h, n_x):
        for y in range(0, w, n_y):
            block = []
            for x_b in range(n_x):
                for y_b in range(n_y):
                    block.append(img[x + x_b][y + y_b])
            result.append(block)
    return np.array(result).reshape(h//n_x, w//n_y, n_x*n_y)


def __merge_blocks(blocks):
    h_b, w_b, block_area = blocks.shape
    block_size =int(math.sqrt(block_area))
    h = h_b * block_size
    w = h_b * block_size
    blocks = blocks.reshape(h_b * w_b, block_area)
    blocks = __sampling_image(blocks, h_b, block_size)
    return blocks.reshape(h, w)


def __transform_image(image, block_size):
    blocks = __sampling_image(image, block_size, block_size)
    result = []
    for row in blocks:
        transformed_row = []
        for col in row:
            transformed_row.append(ft.transform(col))
        result.append(transformed_row)
    return result


def __inverse_image(blocks):
    result = []
    for row in blocks:
        transformed_row = []
        for col in row:
            transformed_row.append(ft.inverse(col))
        result.append(transformed_row)
    return __merge_blocks(np.asarray(result, dtype=np.uint8))

def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.array(img, dtype='int32')
    return data

def save_image(datas, outfilename):
    img = Image.fromarray(np.asarray(np.clip(datas, 0, 255), dtype='uint8'), 'L')
    img.save(outfilename)
    pass


a = load_image('images/input/1.gif')
a = __transform_image(a, 2)
a = __inverse_image(a)
save_image(a, 'images/output/3.gif')

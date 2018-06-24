import math
import numpy as np
import fourier_transform as ft

from complex_number import Complex
from PIL import Image


def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.array(img, dtype='int32')
    return data


def save_image(datas, outfilename):
    img = Image.fromarray(np.asarray(np.clip(datas, 0, 255), dtype='uint8'), 'L')
    img.save(outfilename)
    pass


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


def zipper(fourier_blocks):
    result = []
    for row in fourier_blocks:
        zipped_row = []
        for block in row:
            zipped_block = []
            for i in range(len(block)//2 + 1):
                zipped_block.append(block[i].real)
            for i in range(1, len(block)//2, 1):
                zipped_block.append(block[i].imaginer)
            zipped_row.append(zipped_block)
        result.append(zipped_row)
    return result


def __flipdown_and_conjugate(block):
    result = []
    m = len(block)//2
    real_a, real_b, real_c, imaginer = np.split(block, [1, m, m + 1])
    result.append(Complex(real_a[0]))
    result.extend([Complex(real, i) for real, i in zip(real_b, imaginer)])
    result.append(Complex(real_c[0]))
    result.extend([Complex(real, -i) for real, i in reversed(zip(real_b, imaginer))])
    return result


def inverse_zipper(zipper_blocks):
    result = []
    for row in zipper_blocks:
        inversed_row = []
        for block in row:
            inversed_row.append(__flipdown_and_conjugate(block))
        result.append(inversed_row)
    return result


img = load_image('images/input/3.tif')
a = __transform_image(img, 64)
a = zipper(a)
a = inverse_zipper(a)
a = __inverse_image(a)
save_image(a, 'images/output/3.gif')

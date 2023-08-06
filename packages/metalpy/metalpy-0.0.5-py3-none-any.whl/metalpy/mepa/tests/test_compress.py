import blosc2
import numpy as np
import pympler.asizeof

from metalpy.mepa import DaskExecutor
from metalpy.utils.time import Timer


def generate_randoms(shape):
    return np.ones(shape)


def generate_compressibles(shape):
    return np.random.random(shape)


def task(content):
    content **= 2

    return content


def compressed_task(content):
    content **= 2

    return blosc2.pack_array2(content)


def _test_compress():
    executor = DaskExecutor('localhost:8786')

    shape = (5000, 1000)
    repeated = 10
    timer = Timer()

    with timer:
        for i in range(repeated):
            arg = generate_randoms(shape)
            output = executor.submit(task, arg)
            output, = executor.gather([output])

    print(f'{repeated}x Non-Compressed: {timer}')

    with timer:
        for i in range(repeated):
            compressed_arg = generate_randoms(shape)
            compressed_arg = blosc2.pack_array2(compressed_arg)
            arg = executor.submit(blosc2.unpack_array2, compressed_arg)
            compressed_output = executor.submit(compressed_task, arg)
            compressed_output, = executor.gather([compressed_output])
            output = blosc2.unpack_array2(compressed_output)

    print(f'{repeated}x Compressed: {timer}')

    compress_rate = 0
    for i in range(repeated):
        arg = generate_randoms(shape)
        compressed_arg = blosc2.pack_array2(arg)

        compress_rate += pympler.asizeof.asizeof(compressed_arg) / pympler.asizeof.asizeof(arg)

    print(f'Average Compressed rate: {compress_rate / repeated}')

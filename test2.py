#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy
import gzip
import os

def _read32(bytestream):
    # 采用大尾端存储
    dt = numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)

# 提取图片到四维uint8数组
def extract_images(filename):
    """Extract the images into a 4D uint8 numpy array [index, y, x, depth]."""
    print('Extracting', filename)
    with gzip.open(filename) as bytestream:
        print('bytestream:', bytestream)
        magic = _read32(bytestream)
        print('magic:', magic)
        if magic != 2051:
            raise ValueError(
                'Invalid magic number %d in MNIST image file: %s' %
                (magic, filename))
        num_images = _read32(bytestream)
        print('num_images:', num_images)
        rows = _read32(bytestream)
        print('rows:', rows)
        cols = _read32(bytestream)
        print('cols:', cols)
        buf = bytestream.read(rows * cols * num_images)
        data = numpy.frombuffer(buf, dtype=numpy.uint8)
        data = data.reshape(num_images, rows, cols, 1)
        return data

idata = extract_images('E://t10k-images-idx3-ubyte.gz')
print(idata)
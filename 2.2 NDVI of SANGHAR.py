from rasterio.plot import show
import geos
import tensorflow
import rasterio
import geotiff
import tifffile
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing.image import load_img
from keras import src
from keras.preprocessing.image import img_to_array
from keras import src
import cv2
from PIL import Image
# Open the GeoTIFF image
r_band= rasterio.open(r"D:\image processing\myenv\lab 2 data\B4.TIF")
ir_band = rasterio.open(r"D:\image processing\myenv\lab 2 data\B5.TIF")
red=r_band.read(1).astype(float)
ir=ir_band.read(1).astype(float)
"For error handling for 0 in divisor"
ndvi=(ir-red)/(ir+red)
"close the dataset"
r_band.close()
ir_band.close()
plt.title("sanghar's NDVI.")
plt.imshow(ndvi, cmap='viridis')
plt.colorbar()
plt.show()
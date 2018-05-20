#coding:utf-8
import glob
import os
from PIL import Image

outPath = './resize'

def changePictureSize (imgFile, outPath):
  img = Image.open(imgFile)
  (width, height) = img.size
  newImg = img.resize((int(width / 2), int(height / 2)), Image.BILINEAR)
  newImg.save(os.path.join(outPath, os.path.basename(imgFile)))

for imgFile in glob.glob("./rgb/*.png"):
  if not os.path.exists(outPath):
    os.makedirs(outPath)
  changePictureSize(imgFile, outPath)
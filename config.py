# -*- coding: utf-8 -*-
"""config.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m_b7nMmAmUx_SMQVfpXfV2uJDxxWPcad
"""

TELEGRAM_TOKEN = "5722080247:AAEIMlNJ9I7K9yVBjgCHL4KL82VL3iH2Pfk" # from config import *
files_dict = {'audios': ['.mp3'], 'videos': ['.mp4'], 'imagenes': ['.jpg','.png','.bmp']}
files_nodocs = []
for fd in files_dict.keys():
  files_nodocs.extend(files_dict[fd])
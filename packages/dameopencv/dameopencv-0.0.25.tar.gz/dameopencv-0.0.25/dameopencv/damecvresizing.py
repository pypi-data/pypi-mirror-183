#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  Copyright (C) 2022 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com> 
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with DameOpenCV; see the file LICENSE.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image = cv2.imread("files/img/girl1.jpg", 1)
# Loading the image
 
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))
 
stretch_near = cv2.resize(image, (780, 540),
               interpolation = cv2.INTER_NEAREST)
 
 
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4
 
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
 
plt.show()

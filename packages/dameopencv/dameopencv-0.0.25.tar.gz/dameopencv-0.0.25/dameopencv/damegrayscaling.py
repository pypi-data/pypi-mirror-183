#!/bin/bash
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

# importing opencv 
import cv2 
  
# Load our input image 
image = cv2.imread('files/img/tomatoes.png') 
cv2.imshow('Original', image) 
#cv2.waitKey() 
  
# We use cvtColor, to convert to grayscale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0)   
  
# window shown waits for any key pressing event 
cv2.destroyAllWindows() 

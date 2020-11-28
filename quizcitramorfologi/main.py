# import cv2
#
# image = cv2.imread('image1.JPG')
# cv2.imshow("Original", image)
#
# # erosion
# for i in range(0, 3):
#     eroded = cv2.erode(image.copy(), None, iterations = i + 1)
#     cv2.imshow(f"Erosi {i+1} kali", eroded)
#     cv2.waitKey(0)
#
# # dilation
# for i in range(0, 3):
#     dilated = cv2.dilate(image.copy(), None, iterations = i + 1)
#     cv2.imshow(f"Dilasi {i+1} kali", dilated)
#     cv2.waitKey(0)
#
# kernelSizes = [(3,3), (5,5), (7,7)]
# # Opening
# for kernelSize in kernelSizes:
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
#     opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#     cv2.imshow(f"Opening : ({kernelSize[0]}, {kernelSize[1]}", opening)
#     cv2.waitKey(0)
#
# # Closing
# for kernelSize in kernelSizes:
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
#     opening = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#     cv2.imshow(f"Closing : ({kernelSize[0]}, {kernelSize[1]}", opening)
#     cv2.waitKey(0)


from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

src = None
erosion_size = 0
max_elem = 2
max_kernel_size = 21
title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
title_erosion_window = 'Erosion'
title_dilation_window = 'Dilation'


def main(image):
    global src
    src = cv.imread("image2.JPG")
    if src is None:
        print('Could not open or find the image: ', image)
        exit(0)
    cv.namedWindow(title_erosion_window)
    cv.createTrackbar(title_trackbar_element_shape, title_erosion_window, 0, max_elem, erosion)
    cv.createTrackbar(title_trackbar_kernel_size, title_erosion_window, 0, max_kernel_size, erosion)
    cv.namedWindow(title_dilation_window)
    cv.createTrackbar(title_trackbar_element_shape, title_dilation_window, 0, max_elem, dilatation)
    cv.createTrackbar(title_trackbar_kernel_size, title_dilation_window, 0, max_kernel_size, dilatation)
    erosion(0)
    dilatation(0)
    opening()
    closing()
    cv.waitKey()


# optional mapping of values with morphological shapes
def morph_shape(val):
    if val == 0:
        return cv.MORPH_RECT
    elif val == 1:
        return cv.MORPH_CROSS
    elif val == 2:
        return cv.MORPH_ELLIPSE


def erosion(val):
    erosion_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_erosion_window)
    erosion_shape = morph_shape(cv.getTrackbarPos(title_trackbar_element_shape, title_erosion_window))

    element = cv.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                       (erosion_size, erosion_size))

    erosion_dst = cv.erode(src, element)
    cv.imshow(title_erosion_window, erosion_dst)


def dilatation(val):
    dilatation_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_dilation_window)
    dilation_shape = morph_shape(cv.getTrackbarPos(title_trackbar_element_shape, title_dilation_window))
    element = cv.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    dilatation_dst = cv.dilate(src, element)
    cv.imshow(title_dilation_window, dilatation_dst)


kernelSizes = [(3,3)]
def opening():
    for kernelSize in kernelSizes:
        kernel = cv.getStructuringElement(cv.MORPH_RECT, kernelSize)
        opening = cv.morphologyEx(src, cv.MORPH_OPEN, kernel)
        cv.imshow(f"Opening : ({kernelSize[0]}", opening)
        cv.waitKey(20)

def closing():
    for kernelSize in kernelSizes:
        kernel = cv.getStructuringElement(cv.MORPH_RECT, kernelSize)
        opening = cv.morphologyEx(src, cv.MORPH_CLOSE, kernel)
        cv.imshow(f"Closing : ({kernelSize[0]}", opening)
        cv.waitKey(20)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()
    main(args.input)


# import cv2 as cv
# import numpy as np
#
# img = cv.imread('image1.JPG', 0)
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv.erode(img, kernel, iterations=1)
# dilation = cv.dilate(img, kernel, iterations=1)
# opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#
# cv.imshow('erosion', erosion)
# cv.imshow('dilation', dilation)
# cv.imshow('opening', opening)
# cv.imshow('closing', closing)
# cv.waitKey(0)
from __future__ import print_function

import glob
import numpy as np
import cv2

def downsample(img):
    return cv2.resize(img, (320, 180))

def crop(img):
    assert (180, 320) == img.shape[:2], 'the size of the image should be 320 * 180 after downsampling'
    return img[60:180][:]
    

def birdeye(img):
    """
    Apply perspective transform to input frame to get the bird's eye view.
    :param img: input color frame
    :param verbose: if True, show the transformation result
    :return: warped image, and both forward and backward transformation matrices
    """
    h, w = img.shape[:2]

    src = np.float32([[w, h-10],    # br
                      [0, h-10],    # bl
                      [132, 45],   # tl
                      [188, 45]])  # tr
    dst = np.float32([[w, h],       # br
                      [0, h],       # bl
                      [0, 0],       # tl
                      [w, 0]])      # tr

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)
    warped = cv2.warpPerspective(img, M, (w, h), flags=cv2.INTER_LINEAR)

    return warped, M, Minv

def main():
    # show result on test images
    for test_img in glob.glob('_out/demo-1/*.jpg'):

        img = cv2.imread(test_img)

        img = downsample(img)
        cropped_img = crop(img)

        img_birdeye, M, Minv = birdeye(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
        cv2.imshow('test1', img)
        cv2.imshow('test2', cropped_img)
        cv2.imshow('test3', img_birdeye)
        cv2.waitKey()


if __name__ == '__main__':
    main()

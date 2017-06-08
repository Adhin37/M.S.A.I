# -*- coding: utf-8 -*-
"""
This script detect knife in video.
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
# queryImage
IMG1 = cv2.imread('IMG1.png', 0)
# trainImage
IMG2 = cv2.imread('IMG2.png', 0)

# Initiate SIFT detector
SIFT = cv2.KAZE_create()

# find the keypoints and descriptors with SIFT
KP1, DES1 = SIFT.detectAndCompute(IMG1, None)
KP2, DES2 = SIFT.detectAndCompute(IMG2, None)


FLANN_INDEX_KDTREE = 0
INDEX_PARAMS = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
SEARCH_PARAMS = dict(checks=50)

FLANN = cv2.FlannBasedMatcher(INDEX_PARAMS, SEARCH_PARAMS)

MATCHES = FLANN.knnMatch(DES1, DES2, k=2)

# store all the GOOD matches as per Lowe's ratio test.
GOOD = []
for m, n in MATCHES:
    if m.distance < 0.7 * n.distance:
        GOOD.append(m)

if len(GOOD) > MIN_MATCH_COUNT:
    SRC_PTS = np.float32([KP1[m.queryIdx].pt for m in GOOD]).reshape(-1, 1, 2)
    DTS_PTS = np.float32([KP2[m.trainIdx].pt for m in GOOD]).reshape(-1, 1, 2)

    M, MASK = cv2.findHomography(SRC_PTS, DTS_PTS, cv2.RANSAC, 5.0)
    MATCHES_MASK = MASK.ravel().tolist()

    h, w = IMG1.shape
    PTS = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1],
                      [w - 1, 0]]).reshape(-1, 1, 2)
    DTS = cv2.perspectiveTransform(PTS, M)

    IMG2 = cv2.polylines(IMG2, [np.int32(DTS)], True, 255, 3, cv2.LINE_AA)
else:
    print("Not enough matches are found - %d/%d" %
          (len(GOOD), MIN_MATCH_COUNT))
    MATCHES_MASK = None

DRAW_PARAMS = dict(matchColor=(0, 255, 0),      # draw matches in green color
                   singlePointColor=None,
                   matchesMask=MATCHES_MASK,    # draw only inliers
                   flags=2)

IMG3 = cv2.drawMatches(IMG1, KP1, IMG2, KP2, GOOD, None, **DRAW_PARAMS)

plt.imshow(IMG3, 'gray'), plt.show()
#raw_input()

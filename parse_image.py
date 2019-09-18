import cv2
import numpy as np
from matplotlib import pyplot as plt
champs = ['morde', 'eve']

for champ in champs:
    img_post = cv2.imread('tft_test.png')
    img_post_gray = cv2.cvtColor(img_champ, cv2.COLOR_BGR2GRAY)
    champ_template = cv2.imread('{0}.png'.format(champ))
    w,h = template.shape[::-1]

    res = cv2.matchTemplate(img_post_gray, template, cv2.TM_COEFF_NORMED)
    threshhold = 0.6
    loc = np.where(res >= threshhold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_post, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)
    cv2.imwrite('res{0}.png'.format(champ), img_post)


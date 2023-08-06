import cv2
import pandas as pd
import numpy as np
from math import ceil
from a_cv_imwrite_imread_plus import open_image_in_cv


def img2ascii(img, width=100, letters=r'rqdx.,:ilwWQ@";', filler="X", printimg=True):
    letters = filler + letters
    img = open_image_in_cv(img, channels_in_output=2)

    ratio = img.shape[0] / img.shape[1]

    height = width * ratio
    dim = (int(width), int(height))

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    df = pd.DataFrame(img)
    letters = list(reversed(letters))
    256 / len(letters)
    df2 = df.copy()
    df2.columns += 0.5
    df = pd.concat([df, df2], axis=1)
    df = df.filter(sorted(df.columns))
    df.columns = range(len(df.columns))

    farblimit = 0
    allconditions = []
    allreplacements = []
    for _ in [(x, ceil(256 / len(letters))) for x in enumerate(list(letters))]:
        allsigns = _[0][1]
        farbold = farblimit
        farbnew = farblimit + _[-1]
        allconditions.append(((df >= farbold) & (df < farbnew)))
        allreplacements.append(allsigns)
        farblimit = farbnew
    np.select(allconditions, allreplacements, letters[0])
    df = pd.DataFrame(np.select(allconditions, allreplacements, letters[0]))
    tostr = df.to_string(col_space=1, header=False, index=False).replace(" ", "")
    if printimg:
        print(tostr)
    return tostr


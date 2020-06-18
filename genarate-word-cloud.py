# -*- coding: UTF-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


if __name__ == "__main__":
    with open('jenkins-plugins.txt') as f:
        text = f.read()

        # mask
        mask = np.array(Image.open("jenkins-horizontal-color.png"))

        # generate word cloud
        wc = WordCloud(mask=mask, scale=1.5, mode='RGBA', background_color="white", max_words=2000).generate(text=text)

        # show word cloud
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()

        # save to file
        wc.to_file('word-cloud.png')
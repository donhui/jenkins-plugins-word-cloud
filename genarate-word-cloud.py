# -*- coding: UTF-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate_word_cloud_image(background_image):
    # mask
    mask = np.array(Image.open(background_image))

    # generate word cloud
    wc = WordCloud(mask=mask, scale=1.5, mode='RGBA', background_color="white", max_words=2000).generate(text=text)

    # show word cloud
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # save to file
    wc.to_file(image_name.replace(".png", "-") + 'word-cloud.png')


if __name__ == "__main__":
    with open('jenkins-plugins.txt') as f:
        text = f.read()

        for image_name in ["kongfu.png", "jenkins-logo.png"]:
            generate_word_cloud_image(background_image=image_name)

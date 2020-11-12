"""Python Image Enhancement Using Sharpening

@2020 Created by Vihang Garud
"""

# Importing required libraries
import imageio
import matplotlib.pyplot as plt
import numpy as np


def sharpen(original_image):
    """
    Applying sharpening on the provided image

    :param original_image:
    :return: parser: sharpened image
    """

    # Creating a parser (piece of the image) for the operation
    parser = np.copy(original_image)
    size = parser.shape

    # Generating sharpened image
    for x in range(1, size[0] - 1):

        for y in range(1, size[1] - 1):

            #   0	  -1	  0
            #  -1	   5     -1
            #   0	  -1      0

            parser[x][y] = 5 * original_image[x][y] - (
                        original_image[x - 1][y] + original_image[x][y - 1] + original_image[x][y + 1] +
                        original_image[x + 1][y])

    # Returning the operated image
    return parser


if __name__ == '__main__':

    # Reading the image
    image = imageio.imread('blurry-moon.tif')
    image = image.astype('int32')

    # Applying Sharpening
    sharpened_image = sharpen(image)

    # Outputting the image
    plt.imshow(sharpened_image, cmap='gray')
    plt.show()

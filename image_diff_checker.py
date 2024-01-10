# from PIL import Image, ImageChops
#
# image_one = Image.open('/Users/sviatoslavkovalchuk/Repo/FirstTask/Image_jpeg_sample.jpeg')
# image_two = Image.open('/Users/sviatoslavkovalchuk/Repo/FirstTask/Image_jpeg_sample.jpeg')
#
#
# def img_checker(img_one, img_two):
#     diff_checker = ImageChops.difference(img_one, img_two)
#     print(diff_checker)
#     return diff_checker
#
#
#
# img_checker(image_one, image_two)

from PIL import Image
import imagehash


def diff_chec():
    hash0 = imagehash.average_hash(Image.open('/Users/sviatoslavkovalchuk/Repo/FirstTask/Image_jpeg_sample.jpeg'))
    hash1 = imagehash.average_hash(Image.open('/Users/sviatoslavkovalchuk/Repo/FirstTask/Image_jpeg_sample.jpeg'))
    cutoff = 5  # maximum bits that could be different between the hashes.

    if hash0 - hash1 < cutoff:
        print('images are similar')
    else:
        print('images are not similar')

diff_chec()
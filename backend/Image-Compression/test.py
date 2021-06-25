import os
import numpy as np
from PIL import Image


def read_img(img_path, output):
    image = Image.open(img_path)
    np_image = np.asarray(image)
    np_image = np_image.astype('float32')
    np_image /= 255.0
    img = Image.fromarray(np_image)
    img.save(
        f"{os.path.join(output, os.path.splitext(os.path.basename(img_path))[0])}_test.jpeg")
    return np_image


def main():
    image_name = "wolves.jpg"
    cwd = os.getcwd()
    images_dir = os.path.join(cwd, "images")
    image_path = os.path.join(images_dir, image_name)
    read_img(image_path, images_dir)


if __name__ == "__main__":
    main()

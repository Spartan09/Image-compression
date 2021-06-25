import numpy as np
import os
from PIL import Image
import sys


def img_read(img_path):
    image = Image.open(img_path)
    np_image = np.asarray(image)
    np_image = np_image.astype('float32')
    np_image /= 255.0
    return np_image


def compress(image_path, output_path):
    img = img_read(image_path)
    # print(f"image is with dims: {img.shape}")
    dims = len(img.shape)

    if dims == 2:
        img = np.mean(img, -1)
        U, S, VT = np.linalg.svd(img, full_matrices=False)
        S = np.diag(S)

        # This section to be modified heavily !!!!! ---------------
        # r_max = pass
        # print(f"r_max: {r_max}")
        r_values = (1000, 2000)
        # ---------------------------------------------------------
        for r in r_values:
            Xapprox = []

            Xapproxs = U[:, :r] @ S[0:r, :r] @ VT[:r, :]
            Xapprox.append(Xapproxs)

            Xapprox = np.array(Xapprox)
            Xapprox = np.moveaxis(Xapprox, 0, -1)
            img = Image.fromarray(np.uint8(Xapprox * 255))
            img.save(
                f"{os.path.join(output_path, os.path.splitext(os.path.basename(image_path))[0])}_r={r}.png"
            )

    if dims == 3:
        h, w, c = img.shape[0], img.shape[1], img.shape[2]
        U, S, VT = [], [], []

        for i in range(c):
            Us, Ss, VTs = np.linalg.svd(img[:, :, i], full_matrices=False)
            Ss = np.diag(Ss)
            U.append(Us)
            S.append(Ss)
            VT.append(VTs)

        # This section to be modified heavily !!!!! ---------------
        # r_max = pass
        # print(f"r_max: {r_max}")
        r_values = (250, 500)
        # ---------------------------------------------------------
        for r in r_values:
            Xapprox = []
            for i in range(c):
                Xapproxs = U[i][:, :r] @ S[i][0:r, :r] @ VT[i][:r, :]
                Xapprox.append(Xapproxs)

            Xapprox = np.array(Xapprox)
            Xapprox = np.moveaxis(Xapprox, 0, -1)
            img = Image.fromarray(np.uint8(Xapprox * 255))
            img.save(
                f"{os.path.join(output_path, os.path.splitext(os.path.basename(image_path))[0])}_r={r}.jpeg"
            )


def main():
    image_name = sys.argv[1]
    # image_name = "5757a638e34c2a7004226b915e92224f"
    cwd = os.getcwd()
    images_dir = os.path.join(cwd, "images")
    image_path = os.path.join(images_dir, image_name)
    compress(image_path, images_dir)
    print(image_path)


if __name__ == "__main__":
    main()

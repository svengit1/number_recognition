from PIL import Image

im = Image.open("./archive/CompleteImages/All data (Compressed)/0/0_2_2.png")
im = im.convert("L")


def create_matirx(image):
    image = image.convert("L")
    pix = image.load()
    image_size = image.size
    image_matrix = []
    print(image_size)
    for i in range(image_size[0]):
        row = []
        for j in range(image_size[1]):
            if pix[j, i] == 255:
                row.append(1)
            else:
                row.append(0)
        image_matrix.append(row)
    return image_matrix


matrix = create_matirx(im)

for row in matrix:
    print(row)




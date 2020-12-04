from PIL import Image, ImageFont, ImageDraw


def editor(image):
    my_image = Image.open(image)

    title_font = ImageFont.truetype('arial.ttf', 200)
    title_text = "The Nature"

    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((15, 15), title_text, (237, 230, 211), font=title_font)

    result = my_image.save("result.jpg")

    return Image.open(result)

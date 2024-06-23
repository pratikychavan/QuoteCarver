from PIL import Image, ImageDraw, ImageFont

def create_images_from_quotes(quote, image_location=None, font="cream_cake.otf", font_size=150, font_colour="white", font_alignment="left"):
    width, height = 1920, 1080
    try:
        font = ImageFont.truetype(font=font, size=font_size)
    except IOError as e:
        font = ImageFont.load_default()

    if image_location is not None:
        img = Image.open(image_location)
    else:
        img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)

    parts = quote.strip().split(',')
    y_offset = (img.height - sum(draw.textsize(part, font=font)[1] for part in parts)) // 2

    for part in parts:
        text_width, text_height = draw.textsize(part, font=font)
        x = (img.width - text_width) // 2
        draw.text((x, y_offset), part, font=font, fill=font_colour)
        y_offset += text_height

    img.save(f'outputs/quote_image.png')

create_images_from_quotes("abra ka dabra", "/home/user/Desktop/Personal/QuoteMaker/outputs/quote_image_4.png")
from PIL import Image, ImageDraw, ImageFont
def add_text_to_image(image_path, text, output_path):

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arialbd.ttf", 50)  # Замените путь к шрифту на свой
    except IOError:
        print("Шрифт не найден. Пожалуйста, убедитесь, что файл arialbd.ttf доступен.")
        return

    width, height = image.size

    # Получаем размеры текста
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_x = (width - text_width) // 2
    text_y = height - text_height - 80  # Отступ от нижней границы

    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 0))

    image.save(output_path)
    print(f"Открытка сохранена как {output_path}")

# Основная программа
if __name__ == "__main__":
    name = input("Введите имя того, кого вы хотите поздравить: ")
    message = f"{name}, поздравляю!"

    image_path = "пустая_открытка.png"
    output_path = "поздравления.png"
    add_text_to_image(image_path, message, output_path)

    output_image = Image.open(output_path)
    output_image.show()


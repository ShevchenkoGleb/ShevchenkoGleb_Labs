'''import os
from PIL import Image

def add_watermark(input_folder, output_folder, watermark_path, opacity=0.2):
    # Создаем выходную папку если не существует
    os.makedirs(output_folder, exist_ok=True)

    # Загружаем водяной знак один раз перед циклом
    watermark = Image.open(watermark_path).convert("RGBA")
    alpha = watermark.split()[3].point(lambda p: p * opacity)
    watermark.putalpha(alpha)

    # Обрабатываем только JPG файлы
    for filename in [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path).convert("RGBA") as img:
                # Масштабируем водяной знак под размер изображения
                wm_resized = watermark.resize(img.size, Image.LANCZOS)

                # Создаем композицию
                watermarked = Image.alpha_composite(img, wm_resized)

                # Сохраняем в исходном формате
                watermarked.convert("RGB").save(output_path, "JPEG", quality=85)

        except Exception as e:
            print(f"Ошибка обработки {filename}: {str(e)}")


# Пример использования
add_watermark(
    input_folder='D:/АиП/Лабы/ЛР_8 Обработка изображений/9-4 без знака',
    output_folder='D:/АиП/Лабы/ЛР_8 Обработка изображений/9-4 водяной знак',
    watermark_path='watermark.png',
    opacity=0.2
'''



from PIL import Image, ImageDraw, ImageFont
import os

input_folder = "D:/АиП/Лабы/ЛР_8 Обработка изображений/9-4 без знака2"  # Папка с исходными изображениями
output_folder = "D:/АиП/Лабы/ЛР_8 Обработка изображений/9-4 водяной знак2"  # Папка для сохранения результатов
watermark_text = "водяной знак"  # Текст водяного знака
font_size = 40  # Размер шрифта
opacity = 0.8  # Прозрачность (от 0.0 до 1.0)


def add_watermark():

    # Получаем список PNG-файлов
    images = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    # Обрабатываем каждое изображение
    for filename in images:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Открываем изображение
        with Image.open(input_path).convert("RGBA") as img:
            # Создаем слой для текста
            txt_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))

            # Настраиваем шрифт
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            # Рисуем текст
            draw = ImageDraw.Draw(txt_layer)
            text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            # Позиция в правом нижнем углу с отступом 20px
            x = (img.width - text_width) // 2
            y = (img.height - text_height) // 2

            # Добавляем текст с прозрачностью
            draw.text(
                (x, y),
                watermark_text,
                font=font,
                fill=(255, 255, 255, int(255 * opacity))
            )

            # Объединяем слои
            watermarked = Image.alpha_composite(img, txt_layer)

            # Сохраняем результат
            watermarked.save(output_path)


if __name__ == "__main__":
    add_watermark()
    print(f"Обработано {len(os.listdir(input_folder))} изображений!")

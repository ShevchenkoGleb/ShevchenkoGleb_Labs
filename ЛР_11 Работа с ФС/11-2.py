from pathlib import Path
from PIL import Image

input_folder = Path('D:/Projects_1_MD_8/ЛР_11 Работа с ФС/11-2')
output_folder = Path('D:/Projects_1_MD_8/ЛР_11 Работа с ФС/11-2 Обработка')

for img_path in input_folder.iterdir():
    if img_path.suffix.lower() == '.jpg': #проверка на расширение
        img = Image.open(img_path)

        bw_img = img.convert('L')
        output_path = output_folder / img_path.name
        bw_img.save(output_path)
print("Обработанные файлы сохранены в:", output_folder)

'''import os
from PIL import Image

input_folder = 'D:/АиП/Лабы/ЛР_10 Работа с ФС/11-1'
output_folder = 'D:/АиП/Лабы/ЛР_10 Работа с ФС/11-1 Обработка'

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img = img.resize((800, 600))

        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print("Обработка завершена.")
'''

from pathlib import Path
from PIL import Image

input_folder = Path('D:/Projects_1_MD_8/ЛР_11 Работа с ФС/11-1')
output_folder = Path('D:/Projects_1_MD_8/ЛР_11 Работа с ФС/11-1 Обработка')

for img_path in input_folder.glob('*.jpg'): # .glob поиск всех файлов, соответствующих определенному шаблону(jpg)
    img = Image.open(img_path)
    img = img.resize((600, 600))

    output_path = output_folder / img_path.name #объединение путей
    img.save(output_path)
print("Обработка завершена.")

'''from PIL import Image
import os #для выполнения операций с ФС

input_folder = 'D:\АиП\Лабы\ЛР_8 Обработка изображений'
output_folder = 'D:\АиП\Лабы\ЛР_8 Обработка изображений\9-3 Обработка'

for i in range(1, 6):
    input_file = os.path.join(input_folder, f'{i}.jpg')
    img = Image.open(input_file)
    bw_img = img.convert('L')  # 'L' - режим для градаций серого
    output_file = os.path.join(output_folder, f'ЧБ_{i}.jpg')
    bw_img.save(output_file)
'''

from pathlib import Path # Path - для представления путей к файлам и директориям pathlib - предоставляет объектно-ориентированный интерфейс для работы с ФС.
from PIL import Image

input_folder = Path('D:/Projects_1_MD_8/ЛР_9 Обработка изображений')
output_folder = Path('D:/Projects_1_MD_8/ЛР_9 Обработка изображений/9-3 Обработка')

for i in range(1, 6):
    img = Image.open(input_folder / f'{i}.jpg').convert('L') # 'L' - режим для градаций серого
    img.save(output_folder / f'ЧБ_{i}.jpg')

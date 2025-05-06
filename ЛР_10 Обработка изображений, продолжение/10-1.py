from PIL import Image

input_folder = "D:/АиП/Лабы/ЛР_9 Обработка изображений, продолжение/10-1/открытка.png"
image=Image.open(input_folder)
#image.show()
print(f"Размер: {image.width} * {image.height}")
cut=(270, 50, 670, 200)
cut_image=image.crop(cut)
cut_image.save('D:/АиП/Лабы/ЛР_9 Обработка изображений, продолжение/10-1/cut.png')
cut_image.show()
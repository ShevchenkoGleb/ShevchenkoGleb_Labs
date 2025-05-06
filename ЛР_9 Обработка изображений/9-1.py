from PIL import Image
img=Image.open('welcome.png')
img.show()
print(f"Размер: {img.width} * {img.height}")
print(f"Формат: {img.format}")
print(f'Цветовая модель: {img.mode}')
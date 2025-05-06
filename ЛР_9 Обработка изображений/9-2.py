from PIL import Image
img=Image.open('welcome.png')
img.show()

reduce_img=img.reduce(3)
reduce_img.show()
reduce_img.save('welcome_reduced.png')

horizontal_img=img.transpose(Image.FLIP_LEFT_RIGHT) #зеркальное горизонтальное
horizontal_img.show()
horizontal_img.save('welcome_horizontal.png')

vertical_img=img.transpose(Image.FLIP_TOP_BOTTOM) #зеркальное вертикальное
vertical_img.show()
vertical_img.save('welcome_vertical.png')
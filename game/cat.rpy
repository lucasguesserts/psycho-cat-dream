init python:
    cat_name = "Bartolomeu"

define cat = Character(cat_name, image = "cat")

image cat normal = "images/cat.png"
image side cat normal = im.Scale("images/catPicture.png", 250, 250)

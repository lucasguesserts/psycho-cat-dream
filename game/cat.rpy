init python:
    cat_name = "Bartolomeu"

define cat = Character(cat_name, image = "cat", color="#ededed")

image cat normal = "images/cat.png"
image side cat normal = im.Scale("images/catPicture.png", 250, 250)

image cat happy = "images/catHappy.png"
image side cat happy = im.Scale("images/catPicture.png", 250, 250)

image cat evil = "images/evilCat.png"

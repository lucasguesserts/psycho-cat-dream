# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

python

define e = Character("Elaine")
image elaineNormal = "images/elaineNormal.png"
image bedRoomBlack = "images/bedRoomBlack.jpg" 

# The game starts here.

label start:
    e "Begin Game"

    scene bedRoomBlack at center:
        zoom 0.5
    with zoomin


    show elaineNormal
    with pixellate

    # These display lines of dialogue.

    e "Hello, my name is Elaine"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    jump kitchen

    "Fim de Jogo"

    # This ends the game.

    return


label kitchen:
    e "oi"
    return

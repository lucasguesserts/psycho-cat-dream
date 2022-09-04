define audio.backgroundEvening = "<loop 0.0>audio/eveningBackground.mp3"
define audio.doorOpeningEvening = "audio/doorOpeningEvening.mp3"
define audio.doorOpeningMorning = "audio/doorOpeningMorning.mp3"
define audio.staticTV = "audio/staticTVEvening.mp3"

label audioOpenDoorMorning:
    play sound doorOpeningMorning
    return

label audioOpenDoorEvening:
    play sound doorOpeningEvening
    return

label audioBackgroundEvening:
    play music backgroundEvening fadein 1.0
    return

label audioStaticTV:
    play sound staticTV volume 0.1
    return
define audio.backgroundEvening = "<loop 0.0>audio/eveningBackground.mp3"
define audio.doorOpeningEvening = "audio/doorOpeningEvening.mp3"

label audioOpenDoorEvening:
    play sound doorOpeningEvening
    return

label audioBackgroundEvening:
    play music backgroundEvening
    return
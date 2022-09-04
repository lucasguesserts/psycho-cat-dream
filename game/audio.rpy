define audio.backgroundEvening = "<loop 0.0>audio/eveningBackground.mp3"
define audio.doorOpeningEvening = "audio/doorOpeningEvening.mp3"
define audio.audioNightmare = "audio/terror.mp3"

label audioOpenDoorEvening:
    play sound doorOpeningEvening
    return

label audioBackgroundEvening:
    play music backgroundEvening
    return

label audioNightmare:
    play sound audioNightmare
    return
define audio.backgroundEvening = "<loop 0.0>audio/eveningBackground.mp3"
define audio.doorOpeningEvening = "audio/doorOpeningEvening.mp3"
define audio.doorOpeningMorning = "audio/doorOpeningMorning.mp3"
define audio.staticTV = "audio/staticTVEvening.mp3"
define audio.audioNightmare = "audio/terror.mp3"
define audio.purr = "audio/catPurr.mp3"

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

label audioNightmare:
    play sound audioNightmare
    return

label audioPurr:
    play sound purr
    return
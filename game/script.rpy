label initVariables:
    $ wake_up = True
    $ visited_bathroom = False
    $ visited_kitchen = False
    $ visited_parents_bedroom = False
    $ visited_livingroom = False
    $ vase_is_broken = False
    $ has_watched_tv_in_the_evening = False
    $ is_watching_tv_in_the_evening = False

    # courage mechanics
    $ has_eaten_the_apple_in_the_kitchen_in_the_morning = False
    $ has_eaten_cookies = False
    $ has_checked_her_weight_after_getting_heavier = False
    $ has_checked_her_weight_in_the_evening = False
    $ has_seen_herself_on_the_mirror_in_the_evening = False
    $ has_watched_all_channels_in_the_evening = False
    $ is_courageus_enough = False

    return

label start:

    call initVariables

    call morning
    
    call evening

    "End Game"
    return

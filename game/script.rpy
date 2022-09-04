label initVariables:
    $ wake_up = True
    $ visited_bathroom = False
    $ visited_kitchen = False
    $ visited_parents_bedroom = False
    $ visited_livingroom = False
    $ vase_is_broken = False
    $ has_watched_tv_in_the_evening = False
    $ is_watching_tv_in_the_evening = False
    $ is_sink_open = False
    $ closed_sink = False
    $ player_weight = 30
    $ cookies_eaten = 0
    $ first_time_in_corridor_evening = True
    $ see_gamuto = False
    $ see_unsynced = False
    $ channel_watched = [False for i in range(8)]
    $ running_at_corridor = False
    $ running_at_corridor_second_time = False
    $ tried_to_steal_cookie = False

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

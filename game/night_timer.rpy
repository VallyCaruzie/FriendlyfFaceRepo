transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

init:

    $ day_no = 1


    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0


    $ timer2_range = 0
    $ timer2_jump = 0
    $ time2 = 0

    $ timer_leon_range = 0
    $ timer_leon_jump = 0
    $ time_leon = 0

    $ timer_winniefred_range = 0
    $ timer_winniefred_jump = 0
    $ time_winniefred = 0

    $ timer_sancho_range = 0
    $ timer_sancho_jump = 0
    $ time_sancho = 0

init 1:
    if day_no == 1:
        if time == 400:
            jump couch





screen countdown:
    frame:
        xalign 0.1 ypos 1000
        xsize 500 ysize 50
        timer 0.01 repeat True action If(time > 0, true=SetVariable("time", time - 0.01), false=[Hide("countdown"), Jump(timer_jump)])

        bar value time range timer_range xalign 0.5 yalign 0.6 xmaximum 600 ymaximum 400 at alpha_dissolve
label night_timer:
    $ timer_flag["dayTimer"] == True
    $ time = 420 #7 Minutes
    $ timer_range = 420 #7 Minutes
    $ timer_jump = "day_end"
    show screen countdown




##############################
######### LEON TIMER #########
##############################
screen countdown_leon:
    frame:
        xalign 0.4 ypos 900
        xsize 500 ysize 50
        timer 0.01 repeat True action If(time_leon > 0, true=SetVariable("time_leon", time_leon - 0.01), false=[Hide("countdown_leon"), Jump(timer_jump_leon)])

        bar value time_leon range timer_range_leon xalign 0.5 yalign 0.6 xmaximum 600 ymaximum 400 at alpha_dissolve
            
label night_start_timer_leon:
#    $ timer_flag["day_Timer"] == True
    $ time_leon = 180 #7 Minutes
    $ timer_range_leon = 180 #7 Minutes
    $ timer_jump_leon = "day_end"
    show screen countdown_leon



####################################
######### WINNIEFRED TIMER #########
####################################
#winniefred TIMER
screen countdown_winniefred:
    frame:
        xalign 0.4 ypos 800
        xsize 500 ysize 50
        timer 0.01 repeat True action If(time_winniefred > 0, true=SetVariable("time_winniefred", time_winniefred - 0.01), false=[Hide("countdown_winniefred"), Jump(timer_jump_winniefred)])

        bar value time_winniefred range timer_range_winniefred xalign 0.5 yalign 0.6 xmaximum 600 ymaximum 400 at alpha_dissolve
            
label night_start_timer_winniefred:
#    $ timer_flag["night_Timer_winniefred"] == True
    $ time_winniefred = 5 
    $ timer_range_winniefred = 5
    if obj_flag.get("player_open_door") == False:
        $ timer_jump_winniefred = "death"
    else:
        $ timer_jump_winniefred = "knock_timer_winniefred"
    show screen countdown_winniefred
    jump wc_loop


    #jump wc_loop
label knock_timer_winniefred:  
#    $ timer_flag["night_Timer_winniefred"] == True
    $ time_winniefred = 5 
    $ timer_range_winniefred = 5
    if obj_flag.get("player_open_door") == False:
        $ timer_jump_winniefred = "death"
    else:
        $ timer_jump_winniefred = "cozy_timer_winniefred"
    show screen countdown_winniefred
    "Someone's knocking at the door! Get to the door!"
    show winniefred as winniefred_front_door:
            subpixel True pos (0.50, 1.5)zpos 3600.0 
    jump wc_loop
label cozy_timer_winniefred:
#    $ timer_flag["day_Timer"] == True
    $ time_winniefred = 5 #7 Minutes
    $ timer_range_winniefred = 5 #7 Minutes
    $ timer_jump_winniefred = "lets_roll_timer_winniefred"
    show screen countdown_winniefred
    "After Winniefred is done getting cozy, she will roll"
    jump wc_loop


label lets_roll_timer_winniefred:
#    $ timer_flag["day_Timer"] == True
    "Here Winnie will roll for location"
    $ time_winniefred = 5 
    $ timer_range_winniefred = 5
    $ timer_jump_winniefred = "lets_hold_timer_winniefred"
    show screen countdown_winniefred
    "winniefred is ready to roll for location, perhaps again"
    jump wc_loop

label lets_hold_timer_winniefred:
#    $ timer_flag["day_Timer"] == True
    "Here Winnie will stay where she rolled to, condition met"
    $ time_winniefred = 5 
    $ timer_range_winniefred = 5
    $ timer_jump_winniefred = "lets_roll_timer_winniefred"
    show screen countdown_winniefred
    jump wc_loop

################################
######### SANCHO TIMER #########
################################
#sancho TIMER
screen countdown_sancho:
    frame:
        xalign 1.2 ypos 700
        xsize 900 ysize 30
        timer 0.01 repeat True action If(time2 > 0, true=SetVariable("time_sancho", time - 0.01), false=[Hide("countdown_sancho"), Jump(timer_jump_sancho)])

        bar value time_sancho range timer_range_sancho xalign 0.5 yalign 0.6 xmaximum 600 ymaximum 400 at alpha_dissolve
            
label night_timer_sancho:
#    $ timer_flag["day_Timer"] == True
    $ time_sancho = 420 #7 Minutes
    $ timer_range_sancho = 420 #7 Minutes
    $ timer_jump_sancho = "day_end"
    show screen countdown_sancho
    "sancho Shiggy Shiggy"







    jump day_timer

label day2:
    show beer
    "Day 2"
    jump wc_loop




label time_checker:
    if time == 405:
        "Lets see if this worked at all"
    if time <= 350:
        "Second Test Passed"
    else:
        "test??"
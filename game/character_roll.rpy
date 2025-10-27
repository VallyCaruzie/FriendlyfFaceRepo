# each character has a roll and percentages

#how many spots we got??? how long is a night??
# i just need the variables to work on tbh it should be easy asf after that


#so this is where the gotta make the guts that put the organs together. 
#im thinking we'll need like a fuckton of timers, and thats like it tbh. once a timer goes off itll just do something on its own.

#it should be completely possible to add time to the actual timer. this should be exactly as we picture below. add all sorts of additions and subtractions should ne fine. lets test 2 variations.

label leon_enter_timer:
"Leon Waiting at door."
$ time = 20
$ timer_range = 20
$ timer_jump = "leon_getting_comfortable"
show screen countdown
"add time, 20 sec"
$ time += 20       #add time
"subtract time, 20 seconds"
$ time = 20       #minus time
show screen countdown
l "Hello there! Thank you for letting me in. My name is Leon. Nice to be here. 1"
jump wc_loop

label leon_getting_comfortable:
$ time = 25
$ timer_range = 25
$ timer_jump = "leon_movement_roll"
show screen countdown
l "How nice, I've gotten comfortable... hmm, where should I move on to next? (stay or leave) 2"
show steak as steak1 zorder 99:
    subpixel True pos (1.60, 0.6) zpos -6642.0 yrotate(189) matrixtransform ScaleMatrix(10, 10, 10)
show steak as steak1 zorder 99:
    ease 5 subpixel True pos (100.60, 0.6) zpos -6642.0 yrotate(189) matrixtransform ScaleMatrix(10, 10, 10)

label leon_movement_roll:
$ time = 2
$ timer_range = 2
$ timer_jump = "leon_roll"
show screen countdown
l "Ah! I have decided... I will 3"

label leon_roll:
    $ leon_roll = random.randint(0, 10)
    if leon_roll <= 0:
        l "stay here right now."
        jump wc_loop
    if leon_roll <= 5: 
        l "Go straight to bed!!!!"
        jump leon_in_bed

label leon_in_bed:
    pass
l "It landed on bed"
jump wc_loop



label leon_timer:
    show beer as leon:
        subpixel True pos (1.60, 0.6) zpos 6642.0 yrotate(189)
"You have chosen TEST2."
$ time = 2
$ timer_range = 2
$ timer_jump = "test2_fast"
show screen countdown
"What happened? 4"
jump wc_loop



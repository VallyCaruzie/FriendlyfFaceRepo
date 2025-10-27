#TODO: So we gotta put the buttons for the map here, likely shrink everything until it fits. not too bad tbh

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    frame:
        xalign 0.4 ypos 800
        xsize 600 ysize 200
        timer 0.01 repeat True action If(time > 0, true=SetVariable("time", time - 0.01), false=[Hide("countdown"), Jump(timer_jump)])

        bar value time range timer_range xalign 0.5 yalign 0.6 xmaximum 600 ymaximum 400 at alpha_dissolve
            
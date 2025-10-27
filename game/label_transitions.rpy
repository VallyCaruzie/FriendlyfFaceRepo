label inside1b_to_dining:

    show kitchen_doorframe zorder 5
    show wondow2 behind kitchen_doorframe:
        subpixel True pos (5274, -0.5) zpos 513.0 
        yrotate 90.0

    show wall1 as wall1f_kitchen behind cupboard_c1osed:
        subpixel True pos (4200, -540) zpos -567.0 

    show wall2 as wall2h_kitchen behind doorframe_y_wondow:
        subpixel True pos (3123, -0.5) zpos 513.0 
        yrotate 90.0

    window hide
    camera:
        subpixel True 
        parallel:
            xpos -654 
            ease 3.07 xpos 1683 
            ease 0.23 xpos 2789 
        parallel:
            zpos 513.0 
            ease 1.39 zpos 1125.0 
            ease 1.12 zpos 2018.97 
            ease 0.23 zpos 1787.94 
        parallel:
            xrotate 0.0 
            ease 0.4 xrotate 0.0 
        parallel:
            yrotate -137.0 
            ease 1.39 yrotate -125.12 
            ease 0.56 yrotate -83.54 
    with Pause(3.40)
    camera:
        xpos 2789 zpos 1787.94 xrotate 0.0 yrotate -83.54 
    window show



    
    window hide
    camera:
        subpixel True 
        parallel:
            xpos 15 zpos 2115.0 
            ease 1.48 xpos 2904 zpos 1287.0 
            ease 0.19 xpos 3381 zpos 1566.0 
            ease 1.08 xpos 3327 zpos -333.0 
            ease 0.12 xpos 3390 zpos -400.0 
        parallel:
            yrotate -81.0 
            ease 1.67 yrotate -27.0 
            ease 1.08 yrotate -83.61 
            ease 0.12 yrotate -90 
            ease 0.2 zpos 1130.0 yrotate -90.0 
    with Pause(2.97)


    window show

    jump dining




label kitchen_a_to_dining:
    
    camera:
        subpixel True 
        ease 0.2 zpos 890
        ease 0.1  xpos 3390 zpos 1130.0 xrotate 0 yrotate -90
    with Pause(0.3)


    jump dining

label living_room_to_inside1b:

    window hide
    camera:
        subpixel True 
        parallel:
            xpos 3012 
            ease_cubic 0.99 xpos 357 
        parallel:
            ypos -171 
            ease_cubic 0.49 ypos -90 
        parallel:
            zpos 1130.0 
            ease_cubic 0.27 zpos 1580.9 
            ease_cubic 0.22 zpos 1897.34 
        parallel:
            yrotate 100.0 
            ease_cubic 0.27 yrotate 90.0 
            ease_cubic 0.72 yrotate 41.49 
    with Pause(1.09)
    camera:
        pos (357, -90) zpos 1897.34 yrotate 41.49 
    window show
    jump inside1b


label wondow_from_inside1b:       #### IS INSIDE ####
    camera:
        subpixel True 
        ease 0.3 pos (1904, -395) zpos 2209
        ease 0.59 pos (1904, -395) yrotate -171.0 
        ease 0.13 pos (1976, -395) zpos 1531 yrotate -171.0 
    with Pause(0.74)
    jump wondow

label wondow_from_dining:       #### IS INSIDE ####
    camera:
        subpixel True 
        ease 0.3 pos (1904, -395) zpos 2209
        ease 0.59 pos (1904, -395) yrotate 189.0 
    with Pause(0.69)
    camera:
        pos (1976, -395) zpos 1531 yrotate 189.0 
    jump wondow

    jump inside1b







label generator_to_kitchen_b:
    "You unlock the sliding glass door. This is the Generator"







label generator_to_kitchen_a: # GENERATOR TO KITCHEN A
    #make outside wall where cupboard is
    window hide
    show outside_sliding_glass_doorframe zorder 10: 
        subpixel True pos (3123, -0.5) zpos 513.0 xzoom 1.01 
        yrotate 90.0
    "HOW ABOUT THIS"
    with Pause(5)
    camera:
        subpixel True 
        ease 0.5 yrotate -180.0 
    with Pause(0.5)
    camera:
        subpixel True 
        parallel:
            zpos -8000.0 
            ease 1.5 zpos -1500.0 
            ease 0.6 zpos -159.0 
        parallel:
            ease 1.5 yrotate -130.0 
    with Pause(1.5)
    hide outside_wall1_b
    camera:
        subpixel True 
        ease .6 zpos -159 yrotate -90.0 
    with Pause(0.6)
    camera:
        zpos -159.0 yrotate -90.0 
    window show

    hide outside_wall1_b
    hide outside_wall1_c
    hide outside_wall1_d

    camera:
        subpixel True 
        ease 0.2 xpos 3300 zpos -150.0 xrotate 0.0 
    with Pause(0.2)

    hide outside_sliding_glass_doorframe
    "UNTIL HERE"
    with Pause(5)

    jump kitchen_a



label zoomout_house:
#### ZOOM OUT OF HOUSE ####
    window hide
    camera:
        subpixel True ypos -171 yrotate 0
        ease 1 xpos 1000 zpos 16000 
        ease 2.19 xpos 15 zpos 4833.0 
    with Pause(3.29)
    camera:
        xpos 15 zpos 4833.0 
    window show
    jump wc_loop
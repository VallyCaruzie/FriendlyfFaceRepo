init -3:
    default current_room = None # This variable controls what list to get buttons from
    define obj_flag = {} #Holds all flags for the objects collected
    define use_flag = {} #Holds all flags for objects that are used
    #use and obj are diff because some objects are a one time pick up and if using an object sets it to false, a shine can go back an pick it up again
    #One time pick up objects are perma True after pickup while replenishable items are only True when in inventory
    #use flag always has to be paired w an obj flag to avoid being able to use objects that aren't picked up
    define convers_flag = {} #Holds flags for conditional dialogue based on previous dialogue
    define timer_flag = {}
    define friends_flag = {}
# WC = WORLD CHECK #THIS CONTROLS ALL THE POINT AND CLICK BUTTONS #PART OF A PLUGIN - DO NOT MESS W/




screen wc_screen(room="door"):
    style_prefix "wc"
    for i in eval(f"{room}_buttons"):
        if (i[3] is None) or (eval(i[3])):
            imagebutton auto "images/" + str(i[0]) + "_%s.png" pos i[1] action Return(i[2])
style wc_image_button:
    anchor (0.5, 0.5)

define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause

# This label handles showing the screen to the player.
label wc_loop:
    $ quick_menu = False
    window hide diss
    call screen wc_screen(current_room)
    window show diss
    $ quick_menu = True
    jump expression _return






screen entity_check_loop(room="door"):
    style_prefix "entity_check"
    for i in eval(f"{room}_buttons"):           # SO this checks and loads the room
        if (i[3] is None) or (eval(i[3])):      # WHAT THE FUCK DOES THIS LINE OF CODE DO
            imagebutton auto "images/" + str(i[0]) + "_%s.png" pos i[1] action Return(i[2])
style wc_image_button:
    anchor (0.5, 0.5)

label entity_check_loop:
    $ quick_menu = False
    window hide diss
    call screen entity_check_screen(current_room)            #OK so this seems to be the flag area we can use to flag spawn items in.
    window show diss
    $ quick_menu = True
    jump expression _return



# The game starts here.


label start:
    $ timer_flag["dayTimer"] = False


    #Put all the object flags here for the inventory
    $ obj_flag["has_milk"] = False
    $ obj_flag["has_apple"] = False
    $ obj_flag["has_tart"] = False
    $ obj_flag["has_cereal"] = False
    $ obj_flag["has_key"] = False
    $ obj_flag["has_steak"] = False
    $ obj_flag["has_veggie"] = False
    $ obj_flag["has_mangobean_flower"] = False
    $ obj_flag["has_remote"] = False
    $ obj_flag["has_veggie"] = False

















    screen health_display:      #∑
        frame:
            background "transparent.png"
            xpos 230 ypos 490       #origionally 250, 490
            xsize 330 ysize 70      #origionally 350, 70
            hbox:
                    bar value AnimatedValue(health, 100, 0.001) xpos 60 ypos 395 xsize 120 ysize 20
            text "[health]%":
                    xpos 80 ypos 415        #origionally 80, 415
                    size 20         #origionally 20
                    color "#000000"
    #∑


    screen inventory_display_toggle:
        zorder 92
        frame:
            imagebutton auto "inv_%s.png" action ToggleScreen("inventory_item_description")
            xalign 0.8    #originally 0.037
            yalign 0.9   #originally 0.6

    #    frame:
     #       background "transparent.png"
      #      xalign 0.048        #origionally 0.048
       #     yalign 0.1         #origionally 0.09
    #TEXT FOR INV BUTTON
     #       text "inv":
      #          xpos 10 ypos -35      #origionally 7, 8
       #         size 60             #I believe og was 68
        #        color "#000000"

        on "hide" action Hide("inventory_item_description")

                #   INVENTORY LISTING SYSTEM

    default item_descriptions = { 
        "milk" : "The best drink after a long day", 
        "key" : "To get back into your home", 
    "steak" : "It's nice and crisp after being in the fridge :-)", 
    "veggie" : "Remember to eat something like this!", 
    "tart": "'Funky Bran with Raisin Chunks and Cinnamen'", 
    "special cereal": "An old family recipe with strange effects.", 
            #   WEAPONS / TOOLS
    "lighter": "A fun way to pass the time",
    }

    #THIS IS DATA FOR ACTUAL ITEM TABS IN THE INVENTORY
    style inv_button is frame:
        xsize 100
        ysize 100

    #style inv_button_text:
        xalign 0.7
        yalign 0.9


    screen inventory_item_description:
        # use this based on your preference
        
        modal True
        window:
            background "inv_desc.png"
            xsize 1290
            ysize 600
            xalign 1.52
            yalign 0.9
            text item_description:
                size 40
                xfill True
                yfill True
                xoffset 60
                yoffset 50
                xsize 470
                ysize 200
                

        window:
        #THIS IS THE FRAME FOR THE bACKgROUND of the inventory system
            #Add in the Eat/Drop function
            background "inv_frame.png"
            xsize 600
            ysize 150
            xalign 0.29
            yalign 0.08
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 90
                yoffset 60
                #xalign 0.5
                #yalign 0.5
                style_prefix "inv"
                for item in inventory_items:
                    textbutton item:
                        action SetVariable("item_description", item_descriptions.get(item)) #Add... set variable for the images?
                        selected False


        on "hide" action SetVariable("item_description", "")










    label door: # Player starting point
        window hide diss        #Dissapear, not dissolve
        camera:
            perspective True
            subpixel True xpos 15 zpos 8700.0 yrotate 0.0



    show screen inventory_display_toggle
    show screen health_display


    $ current_room = "door"
    define door_buttons = [
        (("room"), (200, 550), "front_door", None),
        (("room"), (200, 500), "zoomout_house", None),
        (("room"), (200, 900), "leon_enter_timer", None),

    ]
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
#########################
##### WORLD SPRITES #####                   # TOP of loading area for sprites #
#########################

    show black as loading_screen zorder 999:
        subpixel True pos (360, 0) zpos 8000 matrixtransform ScaleMatrix(3, 2, 1.0)

    show black
    show black as black2
    show black:
        subpixel True pos (0.46, -0.46) zpos -3400.0 matrixtransform ScaleMatrix(10.87, 10.82, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show black as black2:
        subpixel True pos (0.46, -0.46) zpos 7300.0 matrixtransform ScaleMatrix(10.87, 10.82, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show black as black3:
        subpixel True xpos -2000 ypos -4320 xzoom 2.45 yzoom 17.81 yrotate 90.0 
    show black as black4:
        subpixel True xpos 4500 ypos -4320 xzoom 2.45 yzoom 17.81 yrotate 90.0 

    # Rar right wall of door
    show kitchen_doorframe behind doorframe_y_wondow:
        subpixel True pos (3123, -0.5) zpos 2673.0 
        yrotate 90.0

    show curtain_half_open as curtain2 zorder 2:
        subpixel True pos (5274, -0.5) zpos 513.0 
        yrotate 90.0
        
    show wondow2 behind curtain2:
        subpixel True pos (5274, -0.5) zpos 513.0 
        yrotate 90.0

    show wall1 as wall1j behind cupboard_closed:
        subpixel True pos (4200, -540) zpos -567.0 

    show winniefred behind wondow2:
        subpixel True pos (8000, -1.02) zpos -540.0 
        yrotate 90.0

    show tv_stand zorder 4:
        subpixel True pos (-0.62, 0.39) zpos 2673.0 
        yrotate 90.0
    with Pause(19)

#######################
###### GREENERY #######

    show pretty_bush as pretty_bush1 zorder 100:
        subpixel True pos (-0.83, 0.02) zpos 4806.0 

    show pretty_bush as pretty_bush2 behind wondow2:
        subpixel True pos (4.84, 0.19) zpos 4806.0 

    show flowers_floor_sprite
    show flowers_floor_sprite:
        subpixel True ypos 19560 zpos 5319.0 zoom 4.0 xrotate 90

    ################################################
    ######## HIDES ITEMS THAT MUST BE RESET ########
    hide winniefred_bedroom
    hide cupboard_door1
    hide cupboard_door1_right
    hide cupboard_door2
    hide cupboard_door2_right
    hide cupboard_door3
    hide cupboard_door3_right
    hide cupboard_door4
    hide cupboard_door4_right
    show inside_door zorder 3:
        subpixel True 
        ease (1) pos (2170, -387) zpos 1595.0 yrotate 0


# DOORFRAME 1
    show doorframe_y_wondow
    show doorframe_y_wondow:
        subpixel True pos (1.07, 1.0)zpos 3744.0 
    #####################
    #### IS OUTSIDE ####
    hide pedestal

###################
## WALLS OF ROOM ##
###################

# ACross OF door
    show stairway_y_indoor_doorframe zorder 3:
        subpixel True pos (-0.06, -0.5) zpos 1595.0 
    # LEFT of door
    show wall2 as wall1a behind stairway:
        subpixel True pos (-0.62, -0.5) zpos 2673.0 
        yrotate 90.0
    #FaAR Doorframe
    show black as black2
    show black as black2 behind carpet:
        subpixel True xpos 1.22 zpos 1359.0 xrotate 0.0 yrotate 0.0 zrotate 90.0 

##### DECORATIONS #####
    show shroud_of_turin
    show shroud_of_turin zorder 3:
        subpixel True pos (3619, -72) zpos 1595.0 xzoom 1.0 zoom 0.15 


    show shoe as shoe zorder 3:
        subpixel True pos (1.63, 0.62) zpos 1594
    show shoe as shoe2 zorder 3:
        subpixel True pos (1.87, 0.62) zpos 1594


    ##########################
    #### CARPET AND TILES ####
    show door zorder 50
    show carpet behind doorframe_y_wondow:
        subpixel True crop_relative True pos (-747, -1791) zpos 2862.0 rotate 90.0 crop (-0.28, 0.0, 1.0, 1.0) xrotate 90.0 
    show carpet as carpet2 behind doorframe_y_wondow:
        subpixel True crop_relative True pos (-747, -1791) zpos 2862.0 rotate 90.0 crop (-0.28, 0.0, 1.0, 1.0) xrotate 90.0 
    show carpet as carpet2:
        subpixel True crop_relative True xpos 477 crop (position(absolute=0.0, relative=-0.28), position(absolute=837.0, relative=0.0), position(absolute=0.0, relative=1.0), position(absolute=0.0, relative=1.0)) 

    show kitchen_tiles
    show kitchen_tiles behind carpet:
        subpixel True pos (2.72, 3.11) zpos 1621.36 xrotate 90

        ########################################
        ######## WINDOW FRAME+ Curtains ########
        ########################################             #curtain: stage1=closed, stage2=1/2 open, stage3=open
    #RIGHT of door


    
    show outside_front zorder 15:
        subpixel True pos (-157, -540) zpos 3744.0 
    
    #show curtain
    show curtain_open as curtain1 zorder 3:
        subpixel True pos (2040, -540) zpos 3744.0 

    #show curtain_open




    show doormat zorder 160:
        subpixel True pos (0.17, 731) zpos 3900.0 zoom 3.7  xrotate 90.0
    show door zorder 16:
        subpixel True xanchor 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 3744.0)
        xpos 0.5 yrotate 0.0
    show inside_door behind stairway_y_indoor_doorframe:
        subpixel True pos (2170, -387) zpos 1595.0 yrotate 0
    window auto show

    show wall1 as wall1c_ behind doorframe_y_wondow:
        subpixel True pos (4200, -540) zpos 3744.0 

        # Rar right wall of door
    show wall2 as wall1d_kitchen behind stairway_y_indoor_doorframe:
        subpixel True pos (5274, -0.5) zpos 2673.0 
        yrotate 90.0

    #Kitchen furniture:
    show cupboard_closed
    show cupboard_closed behind stairway_y_indoor_doorframe:
            subpixel True xpos 5289 ypos 1034 zpos -567.0

########################
##### END OF OUTSIDE WALLS #####
########################


        ##########################
        ##### ROOF / CEILING #####
        ##########################

    show roof_front
    show roof_front zorder 99:
        subpixel True xpos 1.62 ypos -0.32 zpos 3935.0 around (0.0, 0.0) xrotate 36.0

    show ceiling as ceiling1
    show ceiling as ceiling1 behind doorframe_y_wondow:
        subpixel True pos (1.63, 1.73) zpos 1760.78 matrixtransform ScaleMatrix(1.05, 1.0, 1.0) xrotate 90.0 

# DINING FURNITURE
    show table
    show table_legs
    show kitchen_chair_blue
    show kitchen_chair_red
    show kitchen_chair_green
    show table zorder 4:
        subpixel True pos (3.29, 1.14) zpos 2179.0 xzoom 1.39 xrotate 0.0 yrotate 90.0 zrotate 0.0 
    show table_legs zorder 2:
        subpixel True pos (3.29, 1.14) zpos 2179.0 xrotate 0.0 yrotate 90.0 zrotate 0.0 
    show kitchen_chair_blue zorder 3:
        subpixel True pos (3.29, 1.14) zpos 2921.0 xrotate 0.0 yrotate -90.0 zrotate 0.0 
    show kitchen_chair_red zorder 3:
        subpixel True pos (3.29, 1.14) zpos 1965.0 xrotate 0.0 yrotate 90.0 zrotate 0.0 
    show kitchen_chair_green zorder 3:
        subpixel True pos (3.29, 1.14) zpos 2400.0 xrotate 0.0 yrotate 90.0 zrotate 0.0 

    hide loading_screen with Fade(0.01, .5, 0.4)

    ######## END OF LOADING SCREENS ########

##########################################################################
############## ALL OF THE ABOVE IS JUST THE RooM LAYOUT ##################
##########################################################################
label front_door:

    show outside_front zorder 15:
        subpixel True pos (-157, -540) zpos 3744.0 
    show curtain_half_open as curtain1 zorder 4
    hide sofa_front_45
    window hide
    camera:
        subpixel True  
        xpos 15 ypos -171 zpos 4833.0 yrotate 0
    window show
    $ current_room = "front_door"
    define front_door_buttons = [
        (("room"), (200, 550), "open_door", None),
        (("room"), (200, 500), "zoomout_house", None),
        (("room"), (200, 900), "leon_enter_timer", None),
    ]
    jump wc_loop

###################################
####### Door Open Animation #######


    label open_door:
    
        show sofa_front_45 zorder 5:
            subpixel True pos (0.5, 0.21) zpos 1876.0 zoom 1.0 xzoom 1.30 yrotate -50.0 
            
        show door zorder 20:
            subpixel True 
            parallel:
                xanchor 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 3744.0)
                xpos 0.5 yrotate 0.0 
                ease_bounce 1.0 xpos 0.05 yrotate -144.0 
        show sofa_front_45:
            parallel:
                subpixel True 
                ease 1.5 pos (0.5, 0.26) zpos 1876.0 zoom 1.0 xzoom 1.30 yrotate -50.0 
        with Pause(0.5)
    #Push forward


    camera:
        subpixel True 
        parallel:
            xpos 15 ypos -171 zpos 4833.0 
            ease 0.6  ypos -261 zpos 2115.0 
        parallel:
            xrotate 0.0 
            ease 1.00 xpos 2 ypos -171 xrotate 0.0 
    hide wall1j
    hide wondow2

    "..."


    ##################################################################
    ########### HIDES OUTSIDE WALLS + KITCHEN WALLS + ROOF ###########
    ##################################################################

    hide outside_front
    hide wall1j
    hide pretty_bush2
    show kitchen_doorframe zorder 4:
        subpixel True pos (3123, -0.5) zpos 2673.0 
        yrotate 90.0
    hide roof_front
    show door zorder 1


    ###############################################
    ######### INSIDE LIVING ROOM SHIFTING #########
    ###############################################
    show door behind doorframe_y_wondow
    show curtain_half_open as curtain1 zorder 6

    show wondow2 as wall1e_kitchen behind cupboard_closed:
            subpixel True pos (5274, -0.5) zpos 513.0 yrotate 90.0


##########################
##### SHOW PEDEDSTAL #####
    show pedestal
    show pedestal zorder 6:
        subpixel True pos (2.17, 1.16) zpos 3483.0 xzoom 1.0 yzoom 0.61
    show pedestal as pedestal2
    show pedestal as pedestal2 zorder 6:
        subpixel True pos (2.17, 1.16) zpos 3483.0 xzoom 1.0 yzoom 0.61 yrotate 90







####### TIMERS START??? ######
    label day_timer:
        
        if timer_flag.get("dayTimer") == False:
            "ready?"
            $ timer_flag["dayTimer"] = True
            call night_timer
        else:
            $ renpy.notify("Working timer Day")


#lets try to add this for winnie here too

  #  if day_no == 1:
  #      call day_timer_winniefred
  #      call day_timer_leon

    label day_timer_winniefred:
        if timer_flag.get("winniefred_at_door") == False:
            "Hello?"
            $ timer_flag["winniefred_at_door"] == True
            call night_start_timer_winniefred
        else:
            "It should have worked"
            $ renpy.notify("Working timer Winniefred")


    label day_timer_leon:
        if timer_flag.get("leon_at_door") == False:
            "ready?"
            $ timer_flag["leon_at_door"] == True
            call night_start_timer_leon
        else:
            "It should have worked"
            $ renpy.notify("Working timer Leon")
            jump inside1a


    label inside1a:

    $ current_room = "inside1a"
    define inside1a_buttons = [
        (("room"), (1550, 500), "bedroom", None),
        (("room"), (50, 400), "inside1b", None),
        (("room"), (1150, 1000), "couch", None),
        (("room"), (350, 500), "stairway", None),
        (("room"), (150, 1000), "front_door", None),
]

    show sofa_front_45 zorder 6:
        subpixel True 
        ease 0.3 pos (0.5, 0.31) zpos 1876.0 zoom 1.0 xzoom 1.28 yrotate -50.0 
    with Pause(0.3)
    show sofa_front_45 zorder 5:
        subpixel True pos (0.5, 0.31) zpos 1876.0 zoom 1.0 xzoom 1.28 yrotate -50.0     
    show door zorder 1:
        subpixel True 
        parallel:
            ease 0.5 xpos 0.5 
            ease 0.44 yrotate 0.0
    camera:
        subpixel True 
        parallel:
            ease 0.64 xpos -654 zpos 2315 yrotate -56.0
            ease 0.40 yrotate -24.57 
        ease 0.3 xpos -654 zpos 2495 yrotate -24.57 
    with Pause(2)


    camera:
        subpixel True 
        xpos -654 zpos 2495 yrotate -24.57 
    window auto show

    "inside1a"

    jump wc_loop

    label inside1b:

    $ current_room = "inside1b"
    define inside1b_buttons = [
        (("room"), (1250, 500), "front_from_inside", None),
        (("room"), (1850, 600), "inside1a", None),
        (("room"), (750, 400), "wondow_from_inside1b", None),
        (("room"), (450, 550), "pedestal", None),
        (("room"), (150, 500), "inside1b_to_dining", None),
]

##### CLOSING DOOR ANIMATION
    show door behind doorframe_y_wondow:
        subpixel True 
        parallel:
            ease 1.4 xpos 0.5 
            ease 1.4 yrotate 0.0
    camera:
        subpixel True 
        parallel:
            ease 0.2 xpos -654 xrotate 0 yrotate -64 zrotate 0
            ease 0.3 zpos 513.0 yrotate -137
    with Pause(0.5)

    camera:
        subpixel True 
        xpos -654 ypos -171 zpos 513.0 xrotate 0 yrotate -137 zrotate 0

    "inside1b"

    jump wc_loop


label dining:

    $ current_room = "dining"
    define dining_buttons = [
        (("room"), (200, 300), "living_room", None),
        (("room"), (200, 250), "kitchen_a", None),
        (("room"), (200, 200), "kitchen_b", None),
        (("room"), (200, 150), "kitchen_c", None),
    ]

    hide outside_front
    hide wondow2
    hide roof_front


    show inside_door:
        ease (1) yrotate 0
    "This is the dining"
##########################
#### WALLS OF KITCHEN ####
##########################
    show kitchen_doorframe zorder 5
    show wondow2 behind kitchen_doorframe:
        subpixel True pos (5274, -0.5) zpos 513.0 
        yrotate 90.0

    show wall1 as wall1f_kitchen behind cupboard_closed:
        subpixel True pos (4200, -540) zpos -567.0 

    show wall2 as wall2h_kitchen behind doorframe_y_wondow:
        subpixel True pos (3123, -0.5) zpos 513.0 
        yrotate 90.0

    camera:
        subpixel True 
        xpos 3390 zpos 1130.0 xrotate 0 yrotate -90



    jump wc_loop


    
label generator:
    ####################
    #### IS OUTSIDE ####
    hide pedestal
    #show outside_wondow as bedroom_window_only_visible_from_generator:
    #        subpixel True pos (2040, -540) zpos -576.0

    $ current_room = "generator"
    define generator_buttons = [
        (("room"), (200, 300), "generator_to_kitchen_a", None),   #THIS WILL LEAD INTO KITCHEN B, only exists for animation
        (("room"), (200, 250), "touch_generator", None),
        (("room"), (200, 200), "kitchen_b", None),

    ]

    "You unlock the sliding glass door. This is the Generator"

    
    window hide
    show sliding_glass_door as sliding_glass_door1:
        subpixel True 
        zpos 842.0 
        ease 1.2 zpos 264.2 
    with Pause(1.26)
    show sliding_glass_door as sliding_glass_door1:
        zpos 264.2 
    window show

    window hide
    camera:
        subpixel True 
        parallel:
            ease 1 xpos 4235 zpos -150
            ease 1 xpos 1742 yrotate 0
    with Pause(2)
    camera:
        subpixel True
        parallel:
            ease 1 zpos -8000.0 yrotate 40.0 
            ease 1 yrotate 0.0 
    with Pause(2)
    camera:
        xpos 1742 zpos -8000.0 yrotate 0.0 
    window show

    show outside_wall1 as outside_wall1_b zorder 16:
        subpixel True pos (4200, -540) zpos -567.0 
    jump wc_loop
    show outside_wall1 as outside_wall1_c zorder 16:
        subpixel True pos (-0.06, -0.5) zpos 1595.0 
    show outside_wall1 as outside_wall1_d zorder 16:
        subpixel True pos (2044, -540) zpos 1595.0 
    "THIS DID WHAT"
    jump generator_to_kitchen_a

    label touch_generator:
        pass


label wondow:
    ###########################################################
    ########### HIDES OUTSIDE WALLS + KITCHEN WALLS ###########
    ###########################################################
    
    hide outside_front
    hide wondow2
    show kitchen_doorframe zorder 4:
        subpixel True pos (3123, -0.5) zpos 2673.0 
        yrotate 90.0
    hide roof_front
    ###########################################################
    "press the button to start the timer"
    $ current_room = "wondow"
    define wondow_buttons = [
        (("room"), (200, 300), "front_door", None),
        (("room"), (200, 250), "window_test", None),
        (("room"), (200, 200), "pull_curtain", None),

    ]
    jump wc_loop


    label pull_curtain:
    if curtain1_x == 1:
        $ curtain1_x += 1
        show curtain_closed as curtain1 zorder 6:
            subpixel True pos (2040, -540) zpos 3744.0 
    elif curtain1_x == 2:
        $ curtain1_x += 1
        show curtain_half_open as curtain1 zorder 6:
            subpixel True pos (2040, -540) zpos 3744.0 
    elif curtain1_x == 3:
        $ curtain1_x += 1
        show curtain_open as curtain1 zorder 6:
            subpixel True pos (2040, -540) zpos 3744.0     
    elif curtain1_x == 4:
        $ curtain1_x += 1
        show curtain_half_open as curtain1 zorder 6:
            subpixel True pos (2040, -540) zpos 3744.0 
    else:
        $ curtain1_x -= 3
        show curtain_closed as curtain1 zorder 6:
            subpixel True pos (2040, -540) zpos 3744.0 

    jump wondow


    label window_test:
        show beer as villain2:
            subpixel True pos (1.60, 0.6) zpos 6642.0 yrotate(189)
    "You have chosen window_test."
    $ time = 5
    $ timer_range = 5
    $ timer_jump = "window_test_fast"
    show screen countdown
    "What happened?"
    jump wc_loop

    label window_test_fast:
        "Timer2 ended"
        $ test_entity += 3

    show ghosty_base_body
    "Jumpscare test"

    window hide
    show ghosty_base_body:
        subpixel True 
        pos (1.4, 1.46) zpos 7704.0 
    "now lets test this"
    if test_entity == 6:
        "Test_entity is 6"    
        show curtain_open as curtain1 zorder 6:
            subpixel True pos (2040, -540) zpos 3744.0 
        with dissolve
    else:
        pass
    jump wc_loop



    label pedestal:
        
    $ current_room = "pedestal"
    define pedestal_buttons = [
        (("room"), (200, 300), "inside1b", None),
        (("room"), (200, 250), "living_room", None),
    ]
    show pedestal as pedestal2 zorder 6
    show pedestal zorder 6
    "pedestal"
    camera:
        subpixel True 
        ease (1) xpos 2409 zpos 2115 xrotate -60.0 yrotate -125.0 zrotate -60.0 

    jump wc_loop





label kitchen_a:

    $ current_room = "kitchen_a"
    define kitchen_a_buttons = [
        (("room"), (200, 500), "cupboard_door1_open", None),
        (("room"), (350, 500), "cupboard_door2_open", None),
        (("room"), (200, 400), "cupboard_door3_open", None),
        (("room"), (350, 400), "cupboard_door4_open", None),
        (("room"), (100, 400), "kitchen_a_to_dining", None),
        (("room"), (200, 200), "kitchen_b", None),
        (("room"), (200, 150), "kitchen_c", None),
    ]
    
    "You Unlock The Door. --This is kitchen_a"

    show cupboard_open
    show cupboard_open:
        subpixel True xpos 5289 ypos 1034 zpos -567.0
    hide winniefred_bedroom

    show cupboard_doors_closed as cupboard_doors_closed1:
        subpixel True xpos 4339 ypos 532 zpos -567.0
    show cupboard_doors_closed as cupboard_doors_closed2:
        subpixel True xpos 5537 ypos 532 zpos -567.0
    show cupboard_doors_closed as cupboard_doors_closed3:
        subpixel True xpos 4339 ypos -0.48 zpos -567.0
    show cupboard_doors_closed as cupboard_doors_closed4:
        subpixel True xpos 5537 ypos -0.48 zpos -567.0
    hide cupboard_closed


    show apple behind cupboard_doors_closed1:
        subpixel True pos (4475, 710) zpos -567.0 zoom 0.25
    show apple as apple2 behind cupboard_doors_closed1:
        subpixel True pos (4620, 710) zpos -567.0 zoom 0.25 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(-103.41) 
    show veggie behind cupboard_doors_closed1:
        subpixel True pos (4475, 210) zpos -567.0 zoom 0.25
    show steak behind cupboard_doors_closed1:
        subpixel True pos (4620, 210) zpos -567.0 zoom 0.25 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)



    window hide
    camera:
        subpixel True 
        ease 0.9 xpos 4335 zpos -4.0 xrotate 0.0 yrotate 0.0 
    with Pause(0.9)
    window show
    jump wc_loop


    label cupboard_door1_open:
        hide cupboard_doors_closed1
    show cupboard_door as cupboard_door1:
        subpixel True xpos 4339 ypos 532 zpos -567.0
    show cupboard_door_right as cupboard_door1_right:
        subpixel True xpos 4663 ypos 533 zpos -567.0 



    window hide
    show cupboard_door as cupboard_door1:
        subpixel True 
        pos (4339, 532) yrotate 0.0 
        ease_bounce 1.02 pos (4031, 564) yrotate -135.0 
    show cupboard_door_right as cupboard_door1_right:
        subpixel True 
        pos (4663, 533) yrotate 0.0 
        ease_bounce 1.02 pos (4925, 546) yrotate 162.0 
    with Pause(1.02)
    show cupboard_door as cupboard_door1:
        pos (4031, 564) yrotate -135.0 
    show cupboard_door_right as cupboard_door1_right:
        pos (4925, 546) yrotate 162.0 
    window show

    jump wc_loop

    label cupboard_door2_open:
        hide cupboard_doors_closed2

    show cupboard_door as cupboard_door2:
        subpixel True xpos 5537 ypos 532 zpos -567.0 
    show cupboard_door_right as cupboard_door2_right:
        subpixel True xpos 5861 ypos 532 zpos -567.0


    show cupboard_door as cupboard_door2:
        subpixel True 
        pos (5537, 532) yrotate 0.0 
        ease_bounce 1.02 pos (5268, 549) yrotate -160.0 
    show cupboard_door_right as cupboard_door2_right:
        subpixel True 
        pos (5861, 532) orientation (0.0, 0.0, 0.0) 
        ease_bounce 1.02 pos (6166, 546) orientation (0.0, 160.0, 0.0) 
    with Pause(1.02)
    show cupboard_door as cupboard_door2:
        pos (5268, 549) yrotate -160.0 
    show cupboard_door_right as cupboard_door2_right:
        pos (6166, 546) orientation (0.0, 160.0, 0.0) 
    window show

    jump wc_loop

    label cupboard_door3_open:
        hide cupboard_doors_closed3
        
        show cupboard_door as cupboard_door3:
            subpixel True xpos 4339 ypos -519 zpos -567.0
        show cupboard_door_right as cupboard_door3_right:
            subpixel True pos (4663, -519) zpos -567.0

    show cupboard_door as cupboard_door3:
        subpixel True 
        pos (4339, -519) yrotate 0.0 
        ease_bounce 1.02 pos (4031, -530) yrotate -135.0 
    show cupboard_door_right as cupboard_door3_right:
        subpixel True 
        pos (4663, -519) yrotate 0.0 
        ease_bounce 1.02 pos (4925, -530) yrotate 162.0 
    with Pause(1.02)
    show cupboard_door as cupboard_door3:
        pos (4036, -530) yrotate -135.0 
    show cupboard_door_right as cupboard_door3_right:
        pos (4930, -530) yrotate 162.0 








    jump wc_loop


    label cupboard_door4_open:

        hide cupboard_doors_closed4
        
        show cupboard_door as cupboard_door4:
            subpixel True xpos 5537 ypos -519 zpos -567.0

        show cupboard_door_right as cupboard_door4_right:
            subpixel True pos (5861, -519) zpos -567.0

    window hide
    show cupboard_door as cupboard_door4:
        subpixel True 
        pos (5537, -519) yrotate 0.0 
        ease_bounce 1.02 pos (5299, -530) yrotate -135.0 
    show cupboard_door_right as cupboard_door4_right:
        subpixel True 
        pos (5861, -519) yrotate 0.0 
        ease_bounce 1.02 pos (6172, -530) yrotate 162.0 
    with Pause(1.02)
    show cupboard_door as cupboard_door4:
        pos (5299, -530) yrotate -135.0 
    show cupboard_door_right as cupboard_door4_right:
        pos (6176, -530) yrotate 162.0 
    jump wc_loop



    label kitchen_b:
    $ current_room = "kitchen_b"
    define kitchen_b_buttons = [
        (("room"), (200, 300), "dining", None),
        (("room"), (200, 250), "kitchen_a", None),
        (("room"), (200, 150), "kitchen_c", None),
        (("room"), (200, 150), "pull_curtain2", None),

    ]


    camera:
        subpixel True 
        ease 1.47 xpos 4035 zpos -1100.0 xrotate 0.0 yrotate -90.0 
    with Pause(1.57)

    "THis is kitchen_b"


    label pull_curtain2:
    if curtain2_x == 1:
        $ curtain2_x += 1
        show curtain_closed as curtain2 zorder 2:
            subpixel True pos (5274, -0.5) zpos 513.0 yrotate 90
        with dissolve

    elif curtain2_x == 2:
        $ curtain2_x += 1
        show curtain_half_open as curtain2 zorder 2:
            subpixel True pos (5274, -0.5) zpos 513.0 yrotate 90
        with dissolve
    elif curtain2_x == 3:
        $ curtain2_x += 1
        show curtain_open as curtain2 zorder 2:
            subpixel True pos (5274, -0.5) zpos 513.0 yrotate 90
        with dissolve
    elif curtain2_x == 4:
        $ curtain2_x += 1
        show curtain_half_open as curtain2 zorder 2:
            subpixel True pos (5274, -0.5) zpos 513.0 yrotate 90
        with dissolve
    else:
        $ curtain2_x -= 3
        show curtain_closed as curtain2 zorder 2:
            subpixel True pos (5274, -0.5) zpos 513.0 yrotate 90
        with dissolve







    jump wc_loop

    label kitchen_c:
    $ current_room = "kitchen_c"
    define kitchen_c_buttons = [
        (("room"), (200, 300), "dining", None),
        (("room"), (200, 250), "kitchen_a", None),
        (("room"), (200, 150), "kitchen_b", None),
        (("room"), (600, 150), "generator", None),
    ]
    
    hide sofa_front_45
    show outside_wall1 as backyard_wall1 zorder 6:
        subpixel True pos (2044, -540) zpos 1595.0 
    show outside_wall1 as backyard_wall2 zorder 6:
        subpixel True pos (-0.06, -0.5) zpos 1595.0 
    show support_beam_backyard zorder 6:
        subpixel True pos (-233, -0.3) zpos -722.0 matrixtransform ScaleMatrix(1.0, 1.64, 0.84)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yrotate 90.0 

    hide wall2h_kitchen with Fade(0.08, 0.0, 0.12)
    show sliding_glass_doorframe zorder 10:
        subpixel True pos (3123, -0.5) zpos 513.0 xzoom 1.01 
        yrotate 90.0

    show sliding_glass_door as sliding_glass_door1 zorder 11:
        subpixel True pos (3844, -0.29) zpos 842.0 
        yrotate 90.0
    show sliding_glass_door as sliding_glass_door2 zorder 11:
        subpixel True pos (3844, -0.29) zpos 125.0 
        yrotate 90.0
    hide pretty_bush1
    hide pretty_bush2
    hide pretty_bush

    camera:
        subpixel True 
        ease 1.47 xpos 5000 zpos -840.0 xrotate 0.0 yrotate 90.0 
    with Pause(1.57)

    "This is kitchen_c"

    jump wc_loop



    label bedroom:
        $ current_room = "bedroom"
        define bedroom_buttons = [
            (("room"), (1550, 500), "living_room", None),
            (("room"), (350, 400), "inside1b", None),
            (("room"), (150, 400), "inside1a", None),
            (("room"), (150, 500), "dining", None),
        ]

        
        show carpet as bedroom_carpet
        show carpet as bedroom_carpet behind stairway_y_indoor_doorframe:
            subpixel True pos (1.73, 2.25) zpos 505.8 xrotate 90.0 yrotate 90.0 
        show winniefred as winniefred_bedroom behind stairway_y_indoor_doorframe:
            subpixel True pos (2350, -950) zpos 357.0 
        show winniefred_eyes behind stairway_y_indoor_doorframe:
            subpixel True pos (2350, -950) zpos 357.0 alpha 0.30 
        show inside_door zorder 5
        
        window hide
        show sofa_front_45 zorder 6:
            ease (0.3) subpixel True pos (-2, 0.31) zpos 1876.0 zoom 1.30 yrotate -50.0 
        camera:
            subpixel True 
            ease 0.5 pos (1650, -261) zpos 2115.0 yrotate -23.0 
            ease 0.5 pos (1671, -144) zpos 1836.0 yrotate 0.0 
        with Pause(1.1)
        camera:
            pos (1671, -144) zpos 1836.0 yrotate 0.0 

        show black as black_bedroom behind stairway_y_indoor_doorframe:
            subpixel True pos (2170, -227) zpos 1595.0 matrixtransform ScaleMatrix(1.0, 1.1, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 0.75 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend 'normal' 

        "Let's open the door."

        show inside_door zorder 4:
            subpixel True 
            ease (1.2) xpos 2053 zpos 1316.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yrotate 45.0 



        "Winniefred is inside!"

    jump wc_loop


    label living_room:
        $ current_room = "living_room"
        define living_room_buttons = [
            (("room"), (1550, 500), "bedroom", None),
            (("room"), (350, 400), "living_room_to_inside1b", None),
            (("room"), (150, 400), "inside1a", None),
            (("room"), (150, 500), "dining", None),
        ]
        show tv_stand zorder 4:
            subpixel True pos (-0.41, 0.39) zpos 2673.0 
            yrotate 90.0
        show sofa_front_45 zorder 4:
            subpixel True pos (0.41, 0.39) zpos 2673.0 
            yrotate 90.0
        hide pretty_bush1
        window hide
        
        hide sofa_front_45
        show sofa_back zorder 5:
            subpixel True pos (-0.35, 0.39) zpos 2673.0 
            yrotate 90.0

        camera:
            subpixel True 
            ease 0.2 xrotate 0 yrotate -90.0 zrotate 0
            ease 0.5 xpos 3530 zpos 1130 yrotate 100.0 
        with Pause(0.7)
        camera:
            yrotate 100.0 
        window show

    jump wc_loop



    label couch:
        "You look toward the couch"

    jump wc_loop


    label stairway:
        "You look toward the stairwell. Maybe we should put a tray that takes items away"

    jump wc_loop 

return
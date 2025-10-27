label front_from_inside:

    $ current_room = "front_from_inside"
    define inside1b_buttons = [
        (("room"), (150, 500), "front_from_inside", None),
        (("room"), (250, 600), "open_door_from_inside", None),
        (("room"), (150, 550), "pedestal", None),
        (("room"), (250, 500), "inside1b_to_dining", None),
]

    camera:
        subpixel True 
        ease 0.2 pos (-213, -135) zpos 539.82 yrotate -175.0 
    with Pause(0.2)

    camera:
        subpixel True pos (-213, -135) zpos 539.82 yrotate 185.0 
    jump wc_loop



    label open_door_from_inside:
    show door zorder 1:
        subpixel True 
        parallel:
            xanchor 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 3744.0)
            xpos 0.5 yrotate 0.0 
            ease_bounce 1.0 xpos 0.05 yrotate -144.0 


label death:
    if condition_door_answered_winniefred == False:
        "Condition unmet"


                #$ timer_flag["leon_at_door"] == True
                #TBH maybe its an object flag, and object flags cover everything from grabbing items to door opening

                # LIKe, a button that is triggered with a label brought up by timer_jump_winniefred. that screen gets hidden after pressed. 
                        #it can probably override the regular open door button

                    #make it a different color, like gold to see if it worked





                    # MAGIC MAN WILL KILL YOU IF YOU LEAVE THE DOOR OPEN
                    # OPEN DOOR AND LEAVE, SO LIKE HOW BUTTONS
                    # HIDE OBJECT BEHIND BUSH




label get_item_x:

    "You check to find..."
    
    #Object cannot be picked up after being picked up or used
    if obj_flag.get("has_item_x") == True or use_flag.get("used_item_x") == True:

        show player right frown
        "Nothing."
        show player forward smile
        jump wc_loop

    else:

        show item_x:
            zoom 5
            xpos 600
            ypos 130

        show player closedlid high vsmile large
        "Item name!"
        $ renpy.notify("In hand: item_name")
        show player halflid low smile small
        #Adds key to inventory and queues flag for having the key.
        $ inventory_items.append("item_x")
        $ obj_flag["has_item_x"] = True
        hide item_x
        jump wc_loop



# hmm how do we do appearing items? dio we do it based on like a seed?? tbh it sounds like the easiest way
# or like... this relies upon other frames being able to do something

# random rols for spots, 



#if len(inventory_items) >= 10: #len(): length of an array. Turns array into variable to work w/. No need to type limit when defining array  
    #Check if less than or equal to 10
    #"Your bag is full..."
    #"Why so many keys?"
    #jump bed 
#else:
    #$ inventory_items.append("key")

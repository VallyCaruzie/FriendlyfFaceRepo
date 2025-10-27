############################################
## THIS IS WHERE DEFINES OF ENTITIES GOES ##
## going over limit will trigger death    ##
## sequence                               ##
############################################

init python:
    import random

    

default day_no = 1
default health = 100
default inventory_items = []
default item_description = ""



default curtain1_x = 1    
default curtain2_x = 1    


#HUFFY METER
default winniefred = 0
default leon = 0
default sancho = 0
default ladyinredmourning = 0
default normaleeapperson = 0
default bin_bin = 0
default magic_man = 0
default test_entity = 0






define lw = Character(None, image="lucy", kind=bubble)   # Lucy


define n = Character("[name]")
define narrator = Character(what_italic=True)
define u = Character("???")
define w = Character("Winniefred")
define l = Character("Leon", who_color="#b97832ff", image="beer", kind=bubble)
define s = Character("Sancho")
define lrm = Character("Lady In Red Mourning")
define bb = Character("Bin-Bin")
define mm = Character("Magic-Man")
define te = Character("Test_Entity")



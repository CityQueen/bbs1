##### Mit hilfe von Flo #####

Moved_Up_stop1 = True
Moved_Down_stop1 = True
Moved_Left_stop1 = True
Moved_Right_stop1 = True

def Move_Up_stop(player_y, display_height):
    global Moved_Up_stop1
    Moved_Up_stop1 = True
    if player_y < (display_height-80) and player_y > (display_height-160):
        return(player_y-5)
    elif player_y < (display_height-160) and player_y > (display_height-240):
        return(player_y-5)
    elif player_y < (display_height-240) and player_y > (display_height-320):
        return(player_y-5)
    elif player_y < (display_height-320) and player_y > (display_height-400):
        return(player_y-5)
    elif player_y < (display_height-400) and player_y > (display_height-480):
        return(player_y-5)
    elif player_y < (display_height-480) and player_y > (display_height-560):
        return(player_y-5)
    elif player_y < (display_height-560) and player_y > (display_height-640):
        return(player_y-5)
    elif player_y < (display_height-640) and player_y > (display_height-720):
        return(player_y-5)
    else:
        Moved_Up_stop1 = False
        return(player_y)

def Moved_Up_stop():
    global Moved_Up_stop1
    return(Moved_Up_stop1)

def Move_Down_stop(player_y, display_height):
    global Moved_Down_stop1
    Moved_Down_stop1 = True
    if player_y < (display_height-80) and player_y > (display_height-160):
        return(player_y+5)
    elif player_y < (display_height-160) and player_y > (display_height-240):
        return(player_y+5)
    elif player_y < (display_height-240) and player_y > (display_height-320):
        return(player_y+5)
    elif player_y < (display_height-320) and player_y > (display_height-400):
        return(player_y+5)
    elif player_y < (display_height-400) and player_y > (display_height-480):
        return(player_y+5)
    elif player_y < (display_height-480) and player_y > (display_height-560):
        return(player_y+5)
    elif player_y < (display_height-560) and player_y > (display_height-640):
        return(player_y+5)
    elif player_y < (display_height-640) and player_y > (display_height-720):
        return(player_y+5)
    else:
        Moved_Down_stop1 = False
        return(player_y)

def Moved_Down_stop():
    global Moved_Down_stop1
    return(Moved_Down_stop1)

def Move_Left_stop(player_x, display_width):
    global Moved_Left_stop1
    Moved_Left_stop1 = True
    if player_x < (display_width-80) and player_x > (display_width-160):
        return(player_x-5)
    elif player_x < (display_width-160) and player_x > (display_width-240):
        return(player_x-5)
    elif player_x < (display_width-240) and player_x > (display_width-320):
        return(player_x-5)
    elif player_x < (display_width-320) and player_x > (display_width-400):
        return(player_x-5)
    elif player_x < (display_width-400) and player_x > (display_width-480):
        return(player_x-5)
    elif player_x < (display_width-480) and player_x > (display_width-560):
        return(player_x-5)
    elif player_x < (display_width-560) and player_x > (display_width-640):
        return(player_x-5)
    elif player_x < (display_width-640) and player_x > (display_width-720):
        return(player_x-5)
    elif player_x < (display_width-720) and player_x > (display_width-800):
        return(player_x-5)
    elif player_x < (display_width-800) and player_x > (display_width-880):
        return(player_x-5)
    elif player_x < (display_width-880) and player_x > (display_width-960):
        return(player_x-5)
    elif player_x < (display_width-960) and player_x > (display_width-1040):
        return(player_x-5)
    elif player_x < (display_width-1040) and player_x > (display_width-1120):
        return(player_x-5)
    elif player_x < (display_width-1120) and player_x > (display_width-1200):
        return(player_x-5)
    elif player_x < (display_width-1200) and player_x > (display_width-1280):
        return(player_x-5)
    else:
        Moved_Left_stop1 = False
        return(player_x)

def Moved_Left_stop():
    global Moved_Left_stop1
    return(Moved_Left_stop1)

def Move_Right_stop(player_x, display_width):
    global Moved_Right_stop1
    Moved_Right_stop1 = True
    if player_x < (display_width-80) and player_x > (display_width-160):
        return(player_x+5)
    elif player_x < (display_width-160) and player_x > (display_width-240):
        return(player_x+5)
    elif player_x < (display_width-240) and player_x > (display_width-320):
        return(player_x+5)
    elif player_x < (display_width-320) and player_x > (display_width-400):
        return(player_x+5)
    elif player_x < (display_width-400) and player_x > (display_width-480):
        return(player_x+5)
    elif player_x < (display_width-480) and player_x > (display_width-560):
        return(player_x+5)
    elif player_x < (display_width-560) and player_x > (display_width-640):
        return(player_x+5)
    elif player_x < (display_width-640) and player_x > (display_width-720):
        return(player_x+5)
    elif player_x < (display_width-720) and player_x > (display_width-800):
        return(player_x+5)
    elif player_x < (display_width-800) and player_x > (display_width-880):
        return(player_x+5)
    elif player_x < (display_width-880) and player_x > (display_width-960):
        return(player_x+5)
    elif player_x < (display_width-960) and player_x > (display_width-1040):
        return(player_x+5)
    elif player_x < (display_width-1040) and player_x > (display_width-1120):
        return(player_x+5)
    elif player_x < (display_width-1120) and player_x > (display_width-1200):
        return(player_x+5)
    elif player_x < (display_width-1200) and player_x > (display_width-1280):
        return(player_x+5)
    else:
        Moved_Right_stop1 = False
        return(player_x)

def Moved_Right_stop():
    global Moved_Right_stop1
    return(Moved_Right_stop1)
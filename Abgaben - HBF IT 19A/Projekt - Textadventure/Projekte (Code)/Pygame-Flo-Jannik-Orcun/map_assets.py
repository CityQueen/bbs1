def Map_asset(game_map,gameDisplay):
    gameDisplay.blit(game_map,(0,0))
    
def Player_character(player_square,player_x,player_y,gameDisplay):
    gameDisplay.blit(player_square,(player_x,player_y))
    
def Fog_asset(player_x,player_y,Fog,gameDisplay):
    gameDisplay.blit(Fog,(player_x,player_y))
    
def hidden_asset(hidden_x,hidden_y,black_square,gameDisplay):
    gameDisplay.blit(black_square,(hidden_x,hidden_y))
    
def goal_asset(goal_x,goal_y,goal_square,gameDisplay):
    gameDisplay.blit(goal_square,(goal_x,goal_y))
    
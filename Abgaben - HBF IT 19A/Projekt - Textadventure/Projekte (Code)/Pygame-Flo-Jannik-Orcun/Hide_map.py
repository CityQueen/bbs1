from map_assets import *

##### Mit hilfe von Flo #####
def list_clear():
    del Liste[:]

Liste = []
def Hide_map(black_square,gameDisplay,Hardmode,Fog,player_x,player_y,black):
    global Liste
    if Hardmode == 1:
        if player_y >= 160 or player_x >= 160:
            if Liste.count('1') == 0:
                hidden_asset(80*0,80*0,black_square,gameDisplay)
        else:
            if Liste.count('1') == 0:
                Liste += '1'
        if player_y >= 160 or player_x >= 240:
            if Liste.count('2') == 0:
                hidden_asset(80*1,80*0,black_square,gameDisplay)
        else:
            if Liste.count('2') == 0:
                Liste += '2'
        if player_y >= 160 or player_x >= 320 or player_x <= 0:
            if Liste.count('3') == 0:
                hidden_asset(80*2,80*0,black_square,gameDisplay)
        else:
            if Liste.count('3') == 0:
                Liste += '3'
        if player_y >= 160 or player_x >= 400 or player_x <= 80:
            if Liste.count('4') == 0:
                hidden_asset(80*3,80*0,black_square,gameDisplay)
        else:
            if Liste.count('4') == 0:
                Liste += '4'
        if player_y >= 160 or player_x >= 480 or player_x <= 160:
            if Liste.count('5') == 0:
                hidden_asset(80*4,80*0,black_square,gameDisplay)
        else:
            if Liste.count('5') == 0:
                Liste += '5'
        if player_y >= 160 or player_x >= 560 or player_x <= 240:
            if Liste.count('6') == 0:
                hidden_asset(80*5,80*0,black_square,gameDisplay)
        else:
            if Liste.count('6') == 0:
                Liste += '6'
        if player_y >= 160 or player_x >= 640 or player_x <= 320:
            if Liste.count('7') == 0:
                hidden_asset(80*6,80*0,black_square,gameDisplay)
        else:
            if Liste.count('7') == 0:
                Liste += '7'
        if player_y >= 160 or player_x >= 720 or player_x <= 400:
            if Liste.count('8') == 0:
                hidden_asset(80*7,80*0,black_square,gameDisplay)
        else:
            if Liste.count('8') == 0:
                Liste += '8'
        if player_y >= 160 or player_x >= 800 or player_x <= 480:
            if Liste.count('9') == 0:
                hidden_asset(80*8,80*0,black_square,gameDisplay)
        else:
            if Liste.count('9') == 0:
                Liste += '9'
        if player_y >= 160 or player_x >= 880 or player_x <= 560:
            if Liste.count('10') == 0:
                hidden_asset(80*9,80*0,black_square,gameDisplay)
        else:
            if Liste.count('10') == 0:
                Liste.append('10')
        if player_y >= 160 or player_x >= 960 or player_x <= 640:
            if Liste.count('11') == 0:
                hidden_asset(80*10,80*0,black_square,gameDisplay)
        else:
            if Liste.count('11') == 0:
                Liste.append('11')
        if player_y >= 160 or player_x >= 1040 or player_x <= 720:
            if Liste.count('12') == 0:
                hidden_asset(80*11,80*0,black_square,gameDisplay)
        else:
            if Liste.count('12') == 0:
                Liste.append('12')
        if player_y >= 160 or player_x >= 1120 or player_x <= 800:
            if Liste.count('13') == 0:
                hidden_asset(80*12,80*0,black_square,gameDisplay)
        else:
            if Liste.count('13') == 0:
                Liste.append('13')
        if player_y >= 160 or player_x >= 1200 or player_x <= 880:
            if Liste.count('14') == 0:
                hidden_asset(80*13,80*0,black_square,gameDisplay)
        else:
            if Liste.count('14') == 0:
                Liste.append('14')
        if player_y >= 160 or player_x <= 960:
            if Liste.count('15') == 0:
                hidden_asset(80*14,80*0,black_square,gameDisplay)
        else:
            if Liste.count('15') == 0:
                Liste.append('15')
        if player_y >= 160 or player_x <= 1040:
            if Liste.count('16') == 0:
                hidden_asset(80*15,80*0,black_square,gameDisplay)
        else:
            if Liste.count('16') == 0:
                Liste.append('16')
        if player_y >= 240 or player_x >= 160:
            if Liste.count('17') == 0:
                hidden_asset(80*0,80*1,black_square,gameDisplay)
        else:
            if Liste.count('17') == 0:
                Liste.append('17')
        if player_y >= 240 or player_x >= 240:
            if Liste.count('18') == 0:
                hidden_asset(80*1,80*1,black_square,gameDisplay)
        else:
            if Liste.count('18') == 0:
                Liste.append('18')
        if player_y >= 240 or player_x <= 0 or player_x >= 320:
            if Liste.count('19') == 0:
                hidden_asset(80*2,80*1,black_square,gameDisplay)
        else:
            if Liste.count('19') == 0:
                Liste.append('19')
        if player_y >= 240 or player_x <= 80 or player_x >= 400:
            if Liste.count('20') == 0:
                hidden_asset(80*3,80*1,black_square,gameDisplay)
        else:
            if Liste.count('20') == 0:
                Liste.append('20')
        if player_y >= 240 or player_x <= 160 or player_x >= 480:
            if Liste.count('21') == 0:
                hidden_asset(80*4,80*1,black_square,gameDisplay)
        else:
            if Liste.count('21') == 0:
                Liste.append('21')
        if player_y >= 240 or player_x <= 240 or player_x >= 560:
            if Liste.count('22') == 0:
                hidden_asset(80*5,80*1,black_square,gameDisplay)
        else:
            if Liste.count('22') == 0:
                Liste.append('22')
        if player_y >= 240 or player_x <= 320 or player_x >= 640:
            if Liste.count('23') == 0:
                hidden_asset(80*6,80*1,black_square,gameDisplay)
        else:
            if Liste.count('23') == 0:
                Liste.append('23')
        if player_y >= 240 or player_x <= 400 or player_x >= 720:
            if Liste.count('24') == 0:
                hidden_asset(80*7,80*1,black_square,gameDisplay)
        else:
            if Liste.count('24') == 0:
                Liste.append('24')
        if player_y >= 240 or player_x <= 480 or player_x >= 800:
            if Liste.count('25') == 0:
                hidden_asset(80*8,80*1,black_square,gameDisplay)
        else:
            if Liste.count('25') == 0:
                Liste.append('25')
        if player_y >= 240 or player_x <= 560 or player_x >= 880:
            if Liste.count('26') == 0:
                hidden_asset(80*9,80*1,black_square,gameDisplay)
        else:
            if Liste.count('26') == 0:
                Liste.append('26')
        if player_y >= 240 or player_x <= 640 or player_x >= 960:
            if Liste.count('27') == 0:
                hidden_asset(80*10,80*1,black_square,gameDisplay)
        else:
            if Liste.count('27') == 0:
                Liste.append('27')
        if player_y >= 240 or player_x <= 720 or player_x >= 1040:
            if Liste.count('28') == 0:
                hidden_asset(80*11,80*1,black_square,gameDisplay)
        else:
            if Liste.count('28') == 0:
                Liste.append('28')
        if player_y >= 240 or player_x <= 800 or player_x >= 1120:
            if Liste.count('29') == 0:
                hidden_asset(80*12,80*1,black_square,gameDisplay)
        else:
            if Liste.count('29') == 0:
                Liste.append('29')
        if player_y >= 240 or player_x <= 880 or player_x >= 1200:
            if Liste.count('30') == 0:
                hidden_asset(80*13,80*1,black_square,gameDisplay)
        else:
            if Liste.count('30') == 0:
                Liste.append('30')
        if player_y >= 240 or player_x <= 960 or player_x >= 1280:
            if Liste.count('31') == 0:
                hidden_asset(80*14,80*1,black_square,gameDisplay)
        else:
            if Liste.count('31') == 0:
                Liste.append('31')
        if player_y >= 240 or player_x <= 1040:
            if Liste.count('32') == 0:
                hidden_asset(80*15,80*1,black_square,gameDisplay)
        else:
            if Liste.count('32') == 0:
                Liste.append('32')
        if player_y <= 0 or player_y >= 320 or player_x >= 160:
            if Liste.count('33') == 0:
                hidden_asset(80*0,80*2,black_square,gameDisplay)
        else:
            if Liste.count('33') == 0:
                Liste.append('33')
        if player_y <= 0 or player_y >= 320 or player_x >= 240:
            if Liste.count('34') == 0:
                hidden_asset(80*1,80*2,black_square,gameDisplay)
        else:
            if Liste.count('34') == 0:
                Liste.append('34')
        if player_y <= 0 or player_y >= 320 or player_x >= 320 or player_x <= 0:
            if Liste.count('35') == 0:
                hidden_asset(80*2,80*2,black_square,gameDisplay)
        else:
            if Liste.count('35') == 0:
                Liste.append('35')
        if player_y <= 0 or player_y >= 320 or player_x >= 400 or player_x <= 80:
            if Liste.count('36') == 0:
                hidden_asset(80*3,80*2,black_square,gameDisplay)
        else:
            if Liste.count('36') == 0:
                Liste.append('36')
        if player_y <= 0 or player_y >= 320 or player_x >= 480 or player_x <= 160:
            if Liste.count('37') == 0:
                hidden_asset(80*4,80*2,black_square,gameDisplay)
        else:
            if Liste.count('37') == 0:
                Liste.append('37')
        if player_y <= 0 or player_y >= 320 or player_x >= 560 or player_x <= 240:
            if Liste.count('38') == 0:
                hidden_asset(80*5,80*2,black_square,gameDisplay)
        else:
            if Liste.count('38') == 0:
                Liste.append('38')
        if player_y <= 0 or player_y >= 320 or player_x >= 640 or player_x <= 320:
            if Liste.count('39') == 0:
                hidden_asset(80*6,80*2,black_square,gameDisplay)
        else:
            if Liste.count('39') == 0:
                Liste.append('39')
        if player_y <= 0 or player_y >= 320 or player_x >= 720 or player_x <= 400:
            if Liste.count('40') == 0:
                hidden_asset(80*7,80*2,black_square,gameDisplay)
        else:
            if Liste.count('40') == 0:
                Liste.append('40')
        if player_y <= 0 or player_y >= 320 or player_x >= 800 or player_x <= 480:
            if Liste.count('41') == 0:
                hidden_asset(80*8,80*2,black_square,gameDisplay)
        else:
            if Liste.count('41') == 0:
                Liste.append('41')
        if player_y <= 0 or player_y >= 320 or player_x >= 880 or player_x <= 560:
            if Liste.count('42') == 0:
                hidden_asset(80*9,80*2,black_square,gameDisplay)
        else:
            if Liste.count('42') == 0:
                Liste.append('42')
        if player_y <= 0 or player_y >= 320 or player_x >= 960 or player_x <= 640:
            if Liste.count('43') == 0:
                hidden_asset(80*10,80*2,black_square,gameDisplay)
        else:
            if Liste.count('43') == 0:
                Liste.append('43')
        if player_y <= 0 or player_y >= 320 or player_x >= 1040 or player_x <= 720:
            if Liste.count('44') == 0:
                hidden_asset(80*11,80*2,black_square,gameDisplay)
        else:
            if Liste.count('44') == 0:
                Liste.append('44')
        if player_y <= 0 or player_y >= 320 or player_x >= 1120 or player_x <= 800:
            if Liste.count('45') == 0:
                hidden_asset(80*12,80*2,black_square,gameDisplay)
        else:
            if Liste.count('45') == 0:
                Liste.append('45')
        if player_y <= 0 or player_y >= 320 or player_x >= 1200 or player_x <= 880:
            if Liste.count('46') == 0:
                hidden_asset(80*13,80*2,black_square,gameDisplay)
        else:
            if Liste.count('46') == 0:
                Liste.append('46')
        if player_y <= 0 or player_y >= 320 or player_x >= 1280 or player_x <= 960:
            if Liste.count('47') == 0:
                hidden_asset(80*14,80*2,black_square,gameDisplay)
        else:
            if Liste.count('47') == 0:
                Liste.append('47')
        if player_y <= 0 or player_y >= 320 or player_x <= 1040:
            if Liste.count('48') == 0:
                hidden_asset(80*15,80*2,black_square,gameDisplay)
        else:
            if Liste.count('48') == 0:
                Liste.append('48')
        if player_y <= 80 or player_y >= 400 or player_x >= 160:
            if Liste.count('49') == 0:
                hidden_asset(80*0,80*3,black_square,gameDisplay)
        else:
            if Liste.count('49') == 0:
                Liste.append('49')
        if player_y <= 80 or player_y >= 400 or player_x >= 240:
            if Liste.count('50') == 0:
                hidden_asset(80*1,80*3,black_square,gameDisplay)
        else:
            if Liste.count('50') == 0:
                Liste.append('50')
        if player_y <= 80 or player_y >= 400 or player_x >= 320 or player_x <= 0:
            if Liste.count('51') == 0:
                hidden_asset(80*2,80*3,black_square,gameDisplay)
        else:
            if Liste.count('51') == 0:
                Liste.append('51')
        if player_y <= 80 or player_y >= 400 or player_x >= 400 or player_x <= 80:
            if Liste.count('52') == 0:
                hidden_asset(80*3,80*3,black_square,gameDisplay)
        else:
            if Liste.count('52') == 0:
                Liste.append('52')
        if player_y <= 80 or player_y >= 400 or player_x >= 480 or player_x <= 160:
            if Liste.count('53') == 0:
                hidden_asset(80*4,80*3,black_square,gameDisplay)
        else:
            if Liste.count('53') == 0:
                Liste.append('53')
        if player_y <= 80 or player_y >= 400 or player_x >= 560 or player_x <= 240:
            if Liste.count('54') == 0:
                hidden_asset(80*5,80*3,black_square,gameDisplay)
        else:
            if Liste.count('54') == 0:
                Liste.append('54')
        if player_y <= 80 or player_y >= 400 or player_x >= 640 or player_x <= 320:
            if Liste.count('55') == 0:
                hidden_asset(80*6,80*3,black_square,gameDisplay)
        else:
            if Liste.count('55') == 0:
                Liste.append('55')
        if player_y <= 80 or player_y >= 400 or player_x >= 720 or player_x <= 400:
            if Liste.count('56') == 0:
                hidden_asset(80*7,80*3,black_square,gameDisplay)
        else:
            if Liste.count('56') == 0:
                Liste.append('56')
        if player_y <= 80 or player_y >= 400 or player_x >= 800 or player_x <= 480:
            if Liste.count('57') == 0:
                hidden_asset(80*8,80*3,black_square,gameDisplay)
        else:
            if Liste.count('57') == 0:
                Liste.append('57')
        if player_y <= 80 or player_y >= 400 or player_x >= 880 or player_x <= 560:
            if Liste.count('58') == 0:
                hidden_asset(80*9,80*3,black_square,gameDisplay)
        else:
            if Liste.count('58') == 0:
                Liste.append('58')
        if player_y <= 80 or player_y >= 400 or player_x >= 960 or player_x <= 640:
            if Liste.count('59') == 0:
                hidden_asset(80*10,80*3,black_square,gameDisplay)
        else:
            if Liste.count('59') == 0:
                Liste.append('59')
        if player_y <= 80 or player_y >= 400 or player_x >= 1040 or player_x <= 720:
            if Liste.count('60') == 0:
                hidden_asset(80*11,80*3,black_square,gameDisplay)
        else:
            if Liste.count('60') == 0:
                Liste.append('60')
        if player_y <= 80 or player_y >= 400 or player_x >= 1120 or player_x <= 800:
            if Liste.count('61') == 0:
                hidden_asset(80*12,80*3,black_square,gameDisplay)
        else:
            if Liste.count('61') == 0:
                Liste.append('61')
        if player_y <= 80 or player_y >= 400 or player_x >= 1200 or player_x <= 880:
            if Liste.count('62') == 0:
                hidden_asset(80*13,80*3,black_square,gameDisplay)
        else:
            if Liste.count('62') == 0:
                Liste.append('62')
        if player_y <= 80 or player_y >= 400 or player_x >= 1280 or player_x <= 960:
            if Liste.count('63') == 0:
                hidden_asset(80*14,80*3,black_square,gameDisplay)
        else:
            if Liste.count('63') == 0:
                Liste.append('63')
        if player_y <= 80 or player_y >= 400 or player_x <= 1040:
            if Liste.count('64') == 0:
                hidden_asset(80*15,80*3,black_square,gameDisplay)
        else:
            if Liste.count('64') == 0:
                Liste.append('64')
        if player_y <= 160 or player_y >= 480 or player_x >= 160:
            if Liste.count('65') == 0:
                hidden_asset(80*0,80*4,black_square,gameDisplay)
        else:
            if Liste.count('65') == 0:
                Liste.append('65')
        if player_y <= 160 or player_y >= 480 or player_x >= 240:
            if Liste.count('66') == 0:
                hidden_asset(80*1,80*4,black_square,gameDisplay)
        else:
            if Liste.count('66') == 0:
                Liste.append('66')
        if player_y <= 160 or player_y >= 480 or player_x >= 320 or player_x <= 0:
            if Liste.count('67') == 0:
                hidden_asset(80*2,80*4,black_square,gameDisplay)
        else:
            if Liste.count('67') == 0:
                Liste.append('67')
        if player_y <= 160 or player_y >= 480 or player_x >= 400 or player_x <= 80:
            if Liste.count('68') == 0:
                hidden_asset(80*3,80*4,black_square,gameDisplay)
        else:
            if Liste.count('68') == 0:
                Liste.append('68')
        if player_y <= 160 or player_y >= 480 or player_x >= 480 or player_x <= 160:
            if Liste.count('69') == 0:
                hidden_asset(80*4,80*4,black_square,gameDisplay)
        else:
            if Liste.count('69') == 0:
                Liste.append('69')
        if player_y <= 160 or player_y >= 480 or player_x >= 560 or player_x <= 240:
            if Liste.count('70') == 0:
                hidden_asset(80*5,80*4,black_square,gameDisplay)
        else:
            if Liste.count('70') == 0:
                Liste.append('70')
        if player_y <= 160 or player_y >= 480 or player_x >= 640 or player_x <= 320:
            if Liste.count('71') == 0:
                hidden_asset(80*6,80*4,black_square,gameDisplay)
        else:
            if Liste.count('71') == 0:
                Liste.append('71')
        if player_y <= 160 or player_y >= 480 or player_x >= 720 or player_x <= 400:
            if Liste.count('72') == 0:
                hidden_asset(80*7,80*4,black_square,gameDisplay)
        else:
            if Liste.count('72') == 0:
                Liste.append('72')
        if player_y <= 160 or player_y >= 480 or player_x >= 800 or player_x <= 480:
            if Liste.count('73') == 0:
                hidden_asset(80*8,80*4,black_square,gameDisplay)
        else:
            if Liste.count('73') == 0:
                Liste.append('73')
        if player_y <= 160 or player_y >= 480 or player_x >= 880 or player_x <= 560:
            if Liste.count('74') == 0:
                hidden_asset(80*9,80*4,black_square,gameDisplay)
        else:
            if Liste.count('74') == 0:
                Liste.append('74')
        if player_y <= 160 or player_y >= 480 or player_x >= 960 or player_x <= 640:
            if Liste.count('75') == 0:
                hidden_asset(80*10,80*4,black_square,gameDisplay)
        else:
            if Liste.count('75') == 0:
                Liste.append('75')
        if player_y <= 160 or player_y >= 480 or player_x >= 1040 or player_x <= 720:
            if Liste.count('76') == 0:
                hidden_asset(80*11,80*4,black_square,gameDisplay)
        else:
            if Liste.count('76') == 0:
                Liste.append('76')
        if player_y <= 160 or player_y >= 480 or player_x >= 1120 or player_x <= 800:
            if Liste.count('77') == 0:
                hidden_asset(80*12,80*4,black_square,gameDisplay)
        else:
            if Liste.count('77') == 0:
                Liste.append('77')
        if player_y <= 160 or player_y >= 480 or player_x >= 1200 or player_x <= 880:
            if Liste.count('78') == 0:
                hidden_asset(80*13,80*4,black_square,gameDisplay)
        else:
            if Liste.count('78') == 0:
                Liste.append('78')
        if player_y <= 160 or player_y >= 480 or player_x >= 1280 or player_x <= 960:
            if Liste.count('79') == 0:
                hidden_asset(80*14,80*4,black_square,gameDisplay)
        else:
            if Liste.count('79') == 0:
                Liste.append('79')
        if player_y <= 160 or player_y >= 480 or player_x <= 1040:
            if Liste.count('80') == 0:
                hidden_asset(80*15,80*4,black_square,gameDisplay)
        else:
            if Liste.count('80') == 0:
                Liste.append('80')
        if player_y <= 240 or player_y >= 560 or player_x >= 160:
            if Liste.count('81') == 0:
                hidden_asset(80*0,80*5,black_square,gameDisplay)
        else:
            if Liste.count('81') == 0:
                Liste.append('81')
        if player_y <= 240 or player_y >= 560 or player_x >= 240:
            if Liste.count('82') == 0:
                hidden_asset(80*1,80*5,black_square,gameDisplay)
        else:
            if Liste.count('82') == 0:
                Liste.append('82')
        if player_y <= 240 or player_y >= 560 or player_x >= 320 or player_x <= 0:
            if Liste.count('83') == 0:
                hidden_asset(80*2,80*5,black_square,gameDisplay)
        else:
            if Liste.count('83') == 0:
                Liste.append('83')
        if player_y <= 240 or player_y >= 560 or player_x >= 400 or player_x <= 80:
            if Liste.count('84') == 0:
                hidden_asset(80*3,80*5,black_square,gameDisplay)
        else:
            if Liste.count('84') == 0:
                Liste.append('84')
        if player_y <= 240 or player_y >= 560 or player_x >= 480 or player_x <= 160:
            if Liste.count('85') == 0:
                hidden_asset(80*4,80*5,black_square,gameDisplay)
        else:
            if Liste.count('85') == 0:
                Liste.append('85')
        if player_y <= 240 or player_y >= 560 or player_x >= 560 or player_x <= 240:
            if Liste.count('86') == 0:
                hidden_asset(80*5,80*5,black_square,gameDisplay)
        else:
            if Liste.count('86') == 0:
                Liste.append('86')
        if player_y <= 240 or player_y >= 560 or player_x >= 640 or player_x <= 320:
            if Liste.count('87') == 0:
                hidden_asset(80*6,80*5,black_square,gameDisplay)
        else:
            if Liste.count('87') == 0:
                Liste.append('87')
        if player_y <= 240 or player_y >= 560 or player_x >= 720 or player_x <= 400:
            if Liste.count('88') == 0:
                hidden_asset(80*7,80*5,black_square,gameDisplay)
        else:
            if Liste.count('88') == 0:
                Liste.append('88')
        if player_y <= 240 or player_y >= 560 or player_x >= 800 or player_x <= 480:
            if Liste.count('89') == 0:
                hidden_asset(80*8,80*5,black_square,gameDisplay)
        else:
            if Liste.count('89') == 0:
                Liste.append('89')
        if player_y <= 240 or player_y >= 560 or player_x >= 880 or player_x <= 560:
            if Liste.count('90') == 0:
                hidden_asset(80*9,80*5,black_square,gameDisplay)
        else:
            if Liste.count('90') == 0:
                Liste.append('90')
        if player_y <= 240 or player_y >= 560 or player_x >= 960 or player_x <= 640:
            if Liste.count('91') == 0:
                hidden_asset(80*10,80*5,black_square,gameDisplay)
        else:
            if Liste.count('91') == 0:
                Liste.append('91')
        if player_y <= 240 or player_y >= 560 or player_x >= 1040 or player_x <= 720:
            if Liste.count('92') == 0:
                hidden_asset(80*11,80*5,black_square,gameDisplay)
        else:
            if Liste.count('92') == 0:
                Liste.append('92')
        if player_y <= 240 or player_y >= 560 or player_x >= 1120 or player_x <= 800:
            if Liste.count('93') == 0:
                hidden_asset(80*12,80*5,black_square,gameDisplay)
        else:
            if Liste.count('93') == 0:
                Liste.append('93')
        if player_y <= 240 or player_y >= 560 or player_x >= 1200 or player_x <= 880:
            if Liste.count('94') == 0:
                hidden_asset(80*13,80*5,black_square,gameDisplay)
        else:
            if Liste.count('94') == 0:
                Liste.append('94')
        if player_y <= 240 or player_y >= 560 or player_x >= 1280 or player_x <= 960:
            if Liste.count('95') == 0:
                hidden_asset(80*14,80*5,black_square,gameDisplay)
        else:
            if Liste.count('95') == 0:
                Liste.append('95')
        if player_y <= 240 or player_y >= 560 or player_x <= 1040:
            if Liste.count('96') == 0:
                hidden_asset(80*15,80*5,black_square,gameDisplay)
        else:
            if Liste.count('96') == 0:
                Liste.append('96')
        if player_y <= 320 or player_y >= 640 or player_x >= 160:
            if Liste.count('97') == 0:
                hidden_asset(80*0,80*6,black_square,gameDisplay)
        else:
            if Liste.count('97') == 0:
                Liste.append('97')
        if player_y <= 320 or player_y >= 640 or player_x >= 240:
            if Liste.count('98') == 0:
                hidden_asset(80*1,80*6,black_square,gameDisplay)
        else:
            if Liste.count('98') == 0:
                Liste.append('98')
        if player_y <= 320 or player_y >= 640 or player_x >= 320 or player_x <= 0:
            if Liste.count('99') == 0:
                hidden_asset(80*2,80*6,black_square,gameDisplay)
        else:
            if Liste.count('99') == 0:
                Liste.append('99')
        if player_y <= 320 or player_y >= 640 or player_x >= 400 or player_x <= 80:
            if Liste.count('100') == 0:
                hidden_asset(80*3,80*6,black_square,gameDisplay)
        else:
            if Liste.count('100') == 0:
                Liste.append('100')
        if player_y <= 320 or player_y >= 640 or player_x >= 480 or player_x <= 160:
            if Liste.count('101') == 0:
                hidden_asset(80*4,80*6,black_square,gameDisplay)
        else:
            if Liste.count('101') == 0:
                Liste.append('101')
        if player_y <= 320 or player_y >= 640 or player_x >= 560 or player_x <= 240:
            if Liste.count('102') == 0:
                hidden_asset(80*5,80*6,black_square,gameDisplay)
        else:
            if Liste.count('102') == 0:
                Liste.append('102')
        if player_y <= 320 or player_y >= 640 or player_x >= 640 or player_x <= 320:
            if Liste.count('103') == 0:
                hidden_asset(80*6,80*6,black_square,gameDisplay)
        else:
            if Liste.count('103') == 0:
                Liste.append('103')
        if player_y <= 320 or player_y >= 640 or player_x >= 720 or player_x <= 400:
            if Liste.count('104') == 0:
                hidden_asset(80*7,80*6,black_square,gameDisplay)
        else:
            if Liste.count('104') == 0:
                Liste.append('104')
        if player_y <= 320 or player_y >= 640 or player_x >= 800 or player_x <= 480:
            if Liste.count('105') == 0:
                hidden_asset(80*8,80*6,black_square,gameDisplay)
        else:
            if Liste.count('105') == 0:
                Liste.append('105')
        if player_y <= 320 or player_y >= 640 or player_x >= 880 or player_x <= 560:
            if Liste.count('106') == 0:
                hidden_asset(80*9,80*6,black_square,gameDisplay)
        else:
            if Liste.count('106') == 0:
                Liste.append('106')
        if player_y <= 320 or player_y >= 640 or player_x >= 960 or player_x <= 640:
            if Liste.count('107') == 0:
                hidden_asset(80*10,80*6,black_square,gameDisplay)
        else:
            if Liste.count('107') == 0:
                Liste.append('107')
        if player_y <= 320 or player_y >= 640 or player_x >= 1040 or player_x <= 720:
            if Liste.count('108') == 0:
                hidden_asset(80*11,80*6,black_square,gameDisplay)
        else:
            if Liste.count('108') == 0:
                Liste.append('108')
        if player_y <= 320 or player_y >= 640 or player_x >= 1120 or player_x <= 800:
            if Liste.count('109') == 0:
                hidden_asset(80*12,80*6,black_square,gameDisplay)
        else:
            if Liste.count('109') == 0:
                Liste.append('109')
        if player_y <= 320 or player_y >= 640 or player_x >= 1200 or player_x <= 880:
            if Liste.count('110') == 0:
                hidden_asset(80*13,80*6,black_square,gameDisplay)
        else:
            if Liste.count('110') == 0:
                Liste.append('110')
        if player_y <= 320 or player_y >= 640 or player_x >= 1280 or player_x <= 960:
            if Liste.count('111') == 0:
                hidden_asset(80*14,80*6,black_square,gameDisplay)
        else:
            if Liste.count('111') == 0:
                Liste.append('111')
        if player_y <= 320 or player_y >= 640 or player_x <= 1040:
            if Liste.count('112') == 0:
                hidden_asset(80*15,80*6,black_square,gameDisplay)
        else:
            if Liste.count('112') == 0:
                Liste.append('112')
        if player_y <= 400 or player_y >= 720 or player_x >= 160:
            if Liste.count('113') == 0:
                hidden_asset(80*0,80*7,black_square,gameDisplay)
        else:
            if Liste.count('113') == 0:
                Liste.append('113')
        if player_y <= 400 or player_y >= 720 or player_x >= 240:
            if Liste.count('114') == 0:
                hidden_asset(80*1,80*7,black_square,gameDisplay)
        else:
            if Liste.count('114') == 0:
                Liste.append('114')
        if player_y <= 400 or player_y >= 720 or player_x >= 320 or player_x <= 0:
            if Liste.count('115') == 0:
                hidden_asset(80*2,80*7,black_square,gameDisplay)
        else:
            if Liste.count('115') == 0:
                Liste.append('115')
        if player_y <= 400 or player_y >= 720 or player_x >= 400 or player_x <= 80:
            if Liste.count('116') == 0:
                hidden_asset(80*3,80*7,black_square,gameDisplay)
        else:
            if Liste.count('116') == 0:
                Liste.append('116')
        if player_y <= 400 or player_y >= 720 or player_x >= 480 or player_x <= 160:
            if Liste.count('117') == 0:
                hidden_asset(80*4,80*7,black_square,gameDisplay)
        else:
            if Liste.count('117') == 0:
                Liste.append('117')
        if player_y <= 400 or player_y >= 720 or player_x >= 560 or player_x <= 240:
            if Liste.count('118') == 0:
                hidden_asset(80*5,80*7,black_square,gameDisplay)
        else:
            if Liste.count('118') == 0:
                Liste.append('118')
        if player_y <= 400 or player_y >= 720 or player_x >= 640 or player_x <= 320:
            if Liste.count('119') == 0:
                hidden_asset(80*6,80*7,black_square,gameDisplay)
        else:
            if Liste.count('119') == 0:
                Liste.append('119')
        if player_y <= 400 or player_y >= 720 or player_x >= 720 or player_x <= 400:
            if Liste.count('120') == 0:
                hidden_asset(80*7,80*7,black_square,gameDisplay)
        else:
            if Liste.count('120') == 0:
                Liste.append('120')
        if player_y <= 400 or player_y >= 720 or player_x >= 800 or player_x <= 480:
            if Liste.count('121') == 0:
                hidden_asset(80*8,80*7,black_square,gameDisplay)
        else:
            if Liste.count('121') == 0:
                Liste.append('121')
        if player_y <= 400 or player_y >= 720 or player_x >= 880 or player_x <= 560:
            if Liste.count('122') == 0:
                hidden_asset(80*9,80*7,black_square,gameDisplay)
        else:
            if Liste.count('122') == 0:
                Liste.append('122')
        if player_y <= 400 or player_y >= 720 or player_x >= 960 or player_x <= 640:
            if Liste.count('123') == 0:
                hidden_asset(80*10,80*7,black_square,gameDisplay)
        else:
            if Liste.count('123') == 0:
                Liste.append('123')
        if player_y <= 400 or player_y >= 720 or player_x >= 1040 or player_x <= 720:
            if Liste.count('124') == 0:
                hidden_asset(80*11,80*7,black_square,gameDisplay)
        else:
            if Liste.count('124') == 0:
                Liste.append('124')
        if player_y <= 400 or player_y >= 720 or player_x >= 1120 or player_x <= 800:
            if Liste.count('125') == 0:
                hidden_asset(80*12,80*7,black_square,gameDisplay)
        else:
            if Liste.count('125') == 0:
                Liste.append('125')
        if player_y <= 400 or player_y >= 720 or player_x >= 1200 or player_x <= 880:
            if Liste.count('126') == 0:
                hidden_asset(80*13,80*7,black_square,gameDisplay)
        else:
            if Liste.count('126') == 0:
                Liste.append('126')
        if player_y <= 400 or player_y >= 720 or player_x >= 1280 or player_x <= 960:
            if Liste.count('127') == 0:
                hidden_asset(80*14,80*7,black_square,gameDisplay)
        else:
            if Liste.count('127') == 0:
                Liste.append('127')
        if player_y <= 400 or player_y >= 720 or player_x <= 1040:
            if Liste.count('128') == 0:
                hidden_asset(80*15,80*7,black_square,gameDisplay)
        else:
            if Liste.count('128') == 0:
                Liste.append('128')
        if player_y <= 480 or player_y >= 800 or player_x >= 160:
            if Liste.count('129') == 0:
                hidden_asset(80*0,80*8,black_square,gameDisplay)
        else:
            if Liste.count('129') == 0:
                Liste.append('129')
        if player_y <= 480 or player_y >= 800 or player_x >= 240:
            if Liste.count('130') == 0:
                hidden_asset(80*1,80*8,black_square,gameDisplay)
        else:
            if Liste.count('130') == 0:
                Liste.append('130')
        if player_y <= 480 or player_y >= 800 or player_x >= 320 or player_x <= 0:
            if Liste.count('131') == 0:
                hidden_asset(80*2,80*8,black_square,gameDisplay)
        else:
            if Liste.count('131') == 0:
                Liste.append('131')
        if player_y <= 480 or player_y >= 800 or player_x >= 400 or player_x <= 80:
            if Liste.count('132') == 0:
                hidden_asset(80*3,80*8,black_square,gameDisplay)
        else:
            if Liste.count('132') == 0:
                Liste.append('132')
        if player_y <= 480 or player_y >= 800 or player_x >= 480 or player_x <= 160:
            if Liste.count('133') == 0:
                hidden_asset(80*4,80*8,black_square,gameDisplay)
        else:
            if Liste.count('133') == 0:
                Liste.append('133')
        if player_y <= 480 or player_y >= 800 or player_x >= 560 or player_x <= 240:
            if Liste.count('134') == 0:
                hidden_asset(80*5,80*8,black_square,gameDisplay)
        else:
            if Liste.count('134') == 0:
                Liste.append('134')
        if player_y <= 480 or player_y >= 800 or player_x >= 640 or player_x <= 320:
            if Liste.count('135') == 0:
                hidden_asset(80*6,80*8,black_square,gameDisplay)
        else:
            if Liste.count('135') == 0:
                Liste.append('135')
        if player_y <= 480 or player_y >= 800 or player_x >= 720 or player_x <= 400:
            if Liste.count('136') == 0:
                hidden_asset(80*7,80*8,black_square,gameDisplay)
        else:
            if Liste.count('136') == 0:
                Liste.append('136')
        if player_y <= 480 or player_y >= 800 or player_x >= 800 or player_x <= 480:
            if Liste.count('137') == 0:
                hidden_asset(80*8,80*8,black_square,gameDisplay)
        else:
            if Liste.count('137') == 0:
                Liste.append('137')
        if player_y <= 480 or player_y >= 800 or player_x >= 880 or player_x <= 560:
            if Liste.count('138') == 0:
                hidden_asset(80*9,80*8,black_square,gameDisplay)
        else:
            if Liste.count('138') == 0:
                Liste.append('138')
        if player_y <= 480 or player_y >= 800 or player_x >= 960 or player_x <= 640:
            if Liste.count('139') == 0:
                hidden_asset(80*10,80*8,black_square,gameDisplay)
        else:
            if Liste.count('139') == 0:
                Liste.append('139')
        if player_y <= 480 or player_y >= 800 or player_x >= 1040 or player_x <= 720:
            if Liste.count('140') == 0:
                hidden_asset(80*11,80*8,black_square,gameDisplay)
        else:
            if Liste.count('140') == 0:
                Liste.append('140')
        if player_y <= 480 or player_y >= 800 or player_x >= 1120 or player_x <= 800:
            if Liste.count('141') == 0:
                hidden_asset(80*12,80*8,black_square,gameDisplay)
        else:
            if Liste.count('141') == 0:
                Liste.append('141')
        if player_y <= 480 or player_y >= 800 or player_x >= 1200 or player_x <= 880:
            if Liste.count('142') == 0:
                hidden_asset(80*13,80*8,black_square,gameDisplay)
        else:
            if Liste.count('142') == 0:
                Liste.append('142')
        if player_y <= 480 or player_y >= 800 or player_x >= 1280 or player_x <= 960:
            if Liste.count('143') == 0:
                hidden_asset(80*14,80*8,black_square,gameDisplay)
        else:
            if Liste.count('143') == 0:
                Liste.append('143')
        if player_y <= 480 or player_y >= 800 or player_x <= 1040:
            if Liste.count('144') == 0:
                hidden_asset(80*15,80*8,black_square,gameDisplay)
        else:
            if Liste.count('144') == 0:
                Liste.append('144')
    if Hardmode  == 2:
        Fog_asset((player_x-1240),(player_y-680),Fog,gameDisplay)
    if Hardmode == 3:
        gameDisplay.fill(black)
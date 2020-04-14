import pandas as pd

import smtplib

import time

from fortnite_python import Fortnite

from fortnite_python.domain import Mode

from fortnite_python.domain import Platform




to = '9255239257'

fortnite = Fortnite('2097c63b-b464-4712-9fe8-8e1bfeb73281')
t = input("What is your fortnite username: ")
i = input("What is your platform: ")
carrier = input("What carrier domain: sprint, verizon, atnt, tmobile, xfinity:  ")

carrier_domain = ''

if i == 'pc':
	player = fortnite.player(t)
elif i == 'xbox':
	player = fortnite.player(t, Platform.XBOX)
else:
	player = fortnite.player(t, Platform.PSN)


sprint = '@messaging.sprintpcs.com'
verizon = '@vtext.com'
atnt = '@txt.att.net'
tmobile = '@tmomail.net'
xfinity = '@vtext.com'

#Carrier selctors

if carrier == 'sprint': 
    carrier_domain = sprint

elif carrier == 'verizon':
    carrier_domain = verizon

elif carrier == 'atnt':
    carrier_domain = atnt

elif carrier  == 'xfinity':
    carrier_domain = xfinity

else:
    carrier_domain = tmobile


a = player.getStats(Mode.SOLO)
b = player.getStats(Mode.DUO)
c = player.getStats(Mode.SQUAD)

solo_wins = [a.wins]
duo_wins = [b.wins]
squad_wins  = [c.wins]
solo_kills = [a.kills]         
duo_kills = [b.kills]
squad_kills  = [c.kills]
win_list = ['SOLO WINS', a.wins, 'DUO WINS',  b.wins, 'SQUAD WINS',  c.wins]
kill_list = ['SOLO KILLS', a.kills, 'DUO KILLS',  b.kills, 'SQUAD KILLS',  c.kills]
complete_list = win_list + kill_list

test_df = pd.DataFrame({' Solo-Wins': solo_wins,'  Solo-Kills': solo_kills,'  Duo_wins': duo_wins,'  Duo_Kills': duo_kills,' Squad_Wins':squad_wins,'  Squad_kills':squad_kills})
#'ASolo-Wins': solo_wins,
# 'ASolo-Kills': solo_kills,
# '  Duo-Wins ':  duo_wins,
# '  Duo-Kills ': duo_kills,
# '  Squad-Wins ': squad_wins,
# '  Squad-Kills ': squad_kills 

print(test_df)
#Login Info

usr = 'shreyastulsi@gmail.com'
psw = 'quiet786'
fromacc = 'Unknown'



for x in complete_list:
        print('')
        print(x)
        msg = x
        for y in range(1):
                smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo
                smtpserver.login(usr, psw)
                smtpserver.sendmail(fromacc, to + carrier_domain, msg)
                smtpserver.close()
                print('ALL done')

	







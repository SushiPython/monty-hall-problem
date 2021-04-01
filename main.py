import random

doors = ['goatA', 'car', 'goatB']

runs = 0

no_switch_wins = 0
switch_wins = 0

def switch_sim():
    data = ['goatA', 'goatB', 'car']
    con_item = random.choice(doors)
    if con_item == 'goatA':
        data.remove('goatB')
    elif con_item == 'car':
        data.remove(random.choice(['goatA', 'goatB']))
    elif con_item == 'goatB':
        data.remove('goatA')
    data.remove(con_item)
    if data[0] == 'goatA' or data[0] == 'goatB':
        return False
    elif data[0] == 'car':
        return True

def no_switch_sim():
    con_item = random.choice(doors)
    if con_item == "car":
        return True
    elif con_item == "goatA" or con_item == "goatB":
        return False

for i in range(0, 1000000):
    runs += 1
    if no_switch_sim():
        no_switch_wins += 1
    if switch_sim():
        switch_wins += 1


print(f'Number of Runs: {runs}')

print(f'Number of Wins [No Switch]: {no_switch_wins}')
print(f'Win Probability [No Switch]: {no_switch_wins/runs*100}%')

print(f'Number of Wins [Switch]: {switch_wins}')
print(f'Win Probability [Switch]: {switch_wins/runs*100}%')

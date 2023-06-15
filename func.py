# imports
import random
from random import seed
from random import randint
# seed random number generator
seed(1)


# creates all consumables in the game
def create_consumables():
    global consumable_list
    consumable_list = []
    global minor_hp_potion
    minor_hp_potion = {
        "name": "Minor Health Potion",
        'type': 'HP regain',
        'hp_gain': 10,
        "description": "Increases current HP by 10",
        "value": 3,
        "class_usage": ["All"],
        'extra_move_cost': 1
    }
    consumable_list.append(minor_hp_potion)
    global medium_hp_potion
    medium_hp_potion = {
        "name": "Medium Health Potion",
        'type': 'HP regain',
        'hp_gain': 10,
        "description": "Increases current HP by 20",
        "value": 6,
        "class_usage": ["All"],
        'extra_move_cost': 1
    }
    consumable_list.append(medium_hp_potion)
    global major_hp_potion
    major_hp_potion = {
        "name": "Major Health Potion",
        'type': 'HP regain',
        'hp_gain': 10,
        "description": "Increases current HP by 30",
        "value": 9,
        "class_usage": ["All"],
        'extra_move_cost': 1
    }
    consumable_list.append(major_hp_potion)


# creates all armour in the game
def create_armour():
    global mohawk
    mohawk = {
        "name": "Mohawk",
        "armour": 0,
        "Body_part": "head",
        "description": "A dope pink mohawk",
        "value": 0,
        "class_usage": ["All"]
    }
    global chest_hair
    chest_hair = {
        "name": "Chest Hair",
        "armour": 0,
        "Body_part": "body",
        "description": "Just like Tarzan",
        "value": 0,
        "class_usage": ["All"]
    }
    global jeans
    jeans = {
        "name": "Jeans",
        "armour": 0,
        "Body_part": "leg",
        "description": "Made by American Eagle",
        "value": 0,
        "class_usage": ["All"]
    }
    global bucket_helmet
    bucket_helmet = {
        "name": "Bucket Helmet",
        "armour": 1,
        "Body_part": "head",
        "description": "Made out of wood and nails",
        "value": 3,
        "class_usage": ["All"]
    }
    global north_face_jacket
    north_face_jacket = {
        "name": "North Face Jacket",
        "armour": 1,
        "Body_part": "body",
        "description": "Could survive a blizzard in this",
        "value": 3,
        "class_usage": ["All"]
    }
    global bark_jeans
    bark_jeans = {
        "name": "Jeans with bark",
        "armour": 1,
        "Body_part": "leg",
        "description": "Jeans, duct tape and bark combined",
        "value": 3,
        "class_usage": ["All"]
    }


# creates all weapons in the game
def create_weapons():
    global weapon_list
    weapon_list = []
    global fists
    fists = {
        "name": "Fists",
        "damage": 1,
        "damage_type": "Physical",
        "description": "Should wrap them before boxing",
        "value": 0,
        "class_usage": ["All"]
    }
    weapon_list.append(fists)
    global wooden_sword
    wooden_sword = {
        "name": "Wooden Sword",
        "damage": 1,
        "damage_type": "Physical",
        "description": "A children's toy",
        "value": 1,
        "class_usage": ["All"]
    }
    weapon_list.append(wooden_sword)
    global steel_sword
    steel_sword = {
        "name": "Steel Sword",
        "damage": 3,
        "damage_type": "Physical",
        "description": "Pointy",
        "value": 7,
        "class_usage": ["All"]
    }
    weapon_list.append(steel_sword)


# intro is a function that describes class types and lets the user choose their class and player name
# intro creates the character dictionary which is constantly edited during the playthrough
def intro():
    global player
    global dungeon_lvl
    dungeon_lvl = 1
    player = {
        "name": "",
        "class": "",
        "level": 1,
        "EXP": 0,
        "max_EXP": 10,
        "HP": 0,
        "max_HP": 0,
        "AP": 0,
        "max_AP": 0,
        "gold": 10,
        "bag": [],
        "head_armour": mohawk,
        "body_armour": chest_hair,
        "leg_armour": jeans,
        "weapon": fists,
        "armour": 0,
        "strength": 0,
        "moves": [],
        "skills": [],
        'move': 0,
        'extra_move': 0,
        'dead': False
    }
    print("Welcome to Whakan!")
    done = False
    while not done:
        print("Pick a class: \n1.) Warrior")
        option = input("Class: ")
        if option == "1" or option.lower() == "warrior":
            print("\nWarriors have strong base attacks, strong defense with a high armour count.\n"
                  "Warriors are great against non-magical opponents but have a weakness to magic based opponents.\n"
                  "Warriors deal extra damage with physical attacks\n"
                  "Would you like to play as a warrior?\n"
                  "1.) Yes\n"
                  "2.) No")
            option = input('Input: ')
            if option == "1" or option.lower() == "yes":
                done = True
                player["class"] = "Warrior"
                player["HP"] = 13 + player["level"] * 2
                player["max_HP"] = 13 + player["level"] * 2
                player["current_max_HP"] = 13 + player["level"] * 2
                player["AP"] = 1 + player["level"] * 1
                player["max_AP"] = 1 + player["level"] * 1
                player["current_max_AP"] = 1 + player["level"] * 1
                player["strength"] = 5 + int(player["level"] * 0.5)
                player["current_strength"] = 5 + int(player["level"] * 0.5)
                player['armour'] = 1
                player['current_armour'] = 1
                player["all_moves"] = []
                player['bag'] = [minor_hp_potion, medium_hp_potion]
    print("\nWhat is the name of your " + player["class"] + "?")
    player["name"] = input("Player Name: \n\n")


# creates all moves in the game
# these moves can be used by both, the player and the enemy
def create_moves():
    global move_list
    move_list = []
    global punch
    punch = {
        "name": "Punch",
        "type": ['Attack'],
        "enemy_damage": int(player["strength"] + player["weapon"]["damage"]),
        "damage_type": "physical",
        "AP_cost": 0,
        "description": "A straight jab",
        "class_usage": ["Warrior"],
        "required_equipment": "None",
        'player_has': False,
        'move_cost': 1,
        'extra_move_cost': 0
        }
    if player['class'] == 'Warrior':
        punch['player_has'] = True
    player["moves"].append(punch)
    player["all_moves"].append(punch)
    move_list.append(punch)


    global headbutt
    headbutt = {
        "name": "headbutt",
        "type": ['Attack', 'stun'],
        "enemy_damage": int((player["strength"] + player["weapon"]["damage"]) / 2),
        "damage_type": "physical",
        "AP_cost": 2,
        "description": "A stunning headbutt",
        "class_usage": ["Warrior"],
        "required_equipment": "None",
        'player_has': False,
        'move_cost': 1,
        'extra_move_cost': 1,
        'stun': 1
        }
    if player['class'] == 'Warrior':
        headbutt['player_has'] = True
    player["moves"].append(headbutt)
    player["all_moves"].append(headbutt)
    move_list.append(headbutt)
    
    global weaken
    weaken = {
        "name": "weaken",
        "type": ["debuff"],
        'debuff': 'strength',
        "damage_type": "physical",
        "AP_cost": 1,
        "description": "A straight jab",
        "class_usage": ["Warrior"],
        "required_equipment": "None",
        'player_has': False,
        'move_cost': 0,
        'extra_move_cost': 0,
        'strength': 2
        }
    if player['class'] == 'Warrior':
        weaken['player_has'] = True
    player["moves"].append(weaken)
    player["all_moves"].append(weaken)
    move_list.append(weaken)

def update_punch():
    punch["enemy_damage"]: int(player["current_strength"] + player["weapon"]["damage"])

def update_headbuttt():
    headbutt["enemy_damage"]: int((player["current_strength"] + player["weapon"]["damage"]) / 2)


def update_moves():
    x = 0
    while x < len(player['moves']):
        if player["moves"][x] == punch:
            update_punch()
        elif player["moves"][x] == headbutt:
            update_headbuttt()
        x = x + 1
# creates all skills in the game
def create_skills():
    # skill_list = []
    if player["class"] == "Warrior":
        warriors_pride = {
            "description": "Deal 1 extra damage to all physical attacks",
            "class": "Warrior"
        }
        x = 0
        while x < len(weapon_list):
            if weapon_list[x]["damage_type"] == "Physical":
                weapon_list[x]["damage"] = weapon_list[x]["damage"] + 1
            x = x + 1
        player["skills"].append(warriors_pride)
    # skill_list.append["Warrior's Pride"]


# creates the minotoar enemy
def create_minotoar():
    global minotoar
    minotoar = {
        "name": "Minotoar",
        "level": player['level'],
        "HP": 0,
        "max_HP": 0,
        "AP": 0,
        "max_AP": 0,
        "bag": [],
        "head_armour": mohawk,
        "body_armour": chest_hair,
        "leg_armour": jeans,
        "weapon": fists,
        "armour": 0,
        'dead': False,
        "strength": 0,
        "moves": [],
        "experience drop": 0,
        'gold drop': 0,
        'item drop': steel_sword,
        'stun': 0,
        'move': 0,
        'extra_move': 0,
        'pass': False,
        'playable_moves': []
    }
    if minotoar['strength'] > 10:
        minotoar['strength'] = 10
    minotoar["HP"] = 8 + 2 * minotoar['level']
    minotoar["max_HP"] = 8 + 2 * minotoar['level']
    minotoar["AP"] = 1
    minotoar["max_AP"] = minotoar['level']
    minotoar["strength"] = 4 + int(minotoar['level'] / 2)
    minotoar["experience drop"] = 5 + minotoar['level'] * 5
    minotoar['gold drop'] = 13 + minotoar['level'] * 5

def create_minotoar_moves():
    global iron_skin
    iron_skin = {
        "name": "Iron Skin",
        "type": ['buff'],
        "buff": "armour",
        "AP_cost": 1,
        "description": "Creates a thick wall of skin",
        'move_cost': 1,
        'armour': 2
    }
    minotoar["moves"].append(iron_skin)
    global bull_rush
    bull_rush = {
        "name": "Bull Rush",
        "type": ['attack'],
        'damage_type': 'physical',
        "damage": int(minotoar['strength'] + minotoar['weapon']['damage']),
        "AP_cost": 0,
        'move_cost': 1,
    }
    minotoar["moves"].append(bull_rush)
    global horn_attack
    horn_attack = {
        "name": "Horn Attack",
        "type": ['attack'],
        'damage_type': 'physical',
        "damage": int(minotoar['strength']),
        "AP_cost":0,
        'move_cost': 1,
    }
    minotoar["moves"].append(horn_attack)

def end_fight():
    player['current_armour'] = player['armour']
    player['current_max_AP'] = player['max_AP']
    player['AP'] = player['max_AP']
    player['current_max_HP'] = player['max_HP']
    player['HP'] = player['max_HP']
    player['current_strength'] = player['strength']
    player['gold'] = player['gold'] + minotoar['gold drop']
    print(str(player['name']) + ' gained ' + str(minotoar['gold drop']) + ' gold!\n')
    player['EXP'] = player['EXP'] + minotoar['experience drop']
    print(str(player['name']) + ' gained ' + str(minotoar['experience drop']) + ' XP!\n')
    while player['EXP'] >= player['max_EXP']:
        player['EXP'] =  player['EXP'] - player['max_EXP']
        player['level'] = player['level'] + 1
        print(str(player['name']) + ' grew to level ' + str(player['level']) + '!\n')
# creates a fight
def fight():
    round_num = 0
    player['move'] = 0
    player['extra_move'] = 0
    create_minotoar()
    create_minotoar_moves()
    if player['level'] <= 2:
        minotoar['level'] = player['level']
    else:
        minotoar['level'] = random.randint((player['level'] - 2), (player['level'] + 2))
    print("A wild " + str(minotoar['name']) + " appeared!\n")
    while minotoar['HP'] > 0 and player['HP'] > 0:
        round_num = round_num + 1
        player['move'] = player['move'] + 1
        player['extra_move'] = player['extra_move'] + 1
        update_moves()
        player_pass = True
        # player turn
        while player_pass:
            current_turn_user = player
            print(
                'Turn ' + str(round_num) + '\n' +
                str(minotoar['name']) + " LVL " + str(minotoar['level']) +
                "\nHP: " + str(minotoar['HP']) + "/" + str(minotoar['max_HP']) +
                "\nAP: " + str(minotoar['AP']) + "/" + str(minotoar['max_AP']) + "\n\n\n\n\n" +
                str(player['name']) + " LVL " + str(player['level']) + "\n" +
                "HP: " + str(player['HP']) + "/" + str(player['max_HP']) +
                "\nAP: " + str(player['AP']) + "/" + str(player['max_AP']) +
                "\nYou have " + str(player['move']) + " move(s) remaining and " + str(player['extra_move']) + " extra moves remaining\n"
                "----------What would you do?----------\n"
                "1.) Moves                        2.) Bag\n"
                "3.) Inspect Enemy               4.) pass"
            )
            x = input("Input: ")
            if x == '1' or x.lower() == 'moves':
                tmp = 0
                while tmp < len(player['moves']):
                    print(str(tmp + 1) + '.) ' + player['moves'][tmp]['name'] + '\n')
                    tmp = tmp + 1
                print(str(tmp + 1) + ".) Back")
                x = input("What move will you use? ")
                tmp = 1
                while tmp <= len(player['moves']):
                    if x == str(tmp):
                        if player['move'] < player['moves'][int(x) - 1]['move_cost']:
                            print("You don't have the move")
                        if player['move'] < player['moves'][int(x) - 1]['move_cost']:
                            print("You don't have the move")
                        elif player['AP'] < player['moves'][int(x) - 1]['AP_cost']:
                            print("You don't have the AP")
                        else:
                            print(str(player['name']) + " used " + str(player['moves'][int(x) - 1]['name']) + "!\n")
                            player['move'] = player['move'] - 1
                            player['AP'] = player['AP'] - player['moves'][int(x) - 1]['AP_cost']
                            if 'Attack' in player['moves'][int(x) - 1]['type']:
                                damage = player['moves'][int(x) - 1]['enemy_damage'] - minotoar['armour']
                                if damage < 1:
                                    damage = 1
                                print(
                                    str(player['name']) + ' dealt ' + str(damage) +
                                    ' to the ' + str(minotoar['name'] + "!\n")
                                )
                                minotoar['HP'] = minotoar['HP'] - damage
                                if minotoar['HP'] <= 0:
                                    player_pass = False
                                    minotoar['dead'] = True
                                    print(str(player['name']) + ' defeated the ' + minotoar['name'] + '!\n')
                            if 'stun' in player['moves'][int(x) - 1]['type']:
                                print(
                                    str(player['name']) + ' stunned ' + str(minotoar['name'] + "!\n")
                                )
                                minotoar['stun'] = minotoar['stun'] + 1
                            if 'debuff' in player['moves'][int(x) - 1]['type']:
                                if player['moves'][int(x) - 1]['debuff']:
                                    print(
                                        str(player['name']) + ' lowered ' + str(minotoar['name'] +
                                        "'s strenght by " + str(player['moves'][int(x) - 1]['strength']) + "!\n")
                                    )
                                    minotoar['strength'] = minotoar['strength'] - player['moves'][int(x) - 1]['strength']
                                    if minotoar['strength'] < 1:
                                        minotoar['strength'] = 1
                                        print(str(minotoar['name']) + 's strength can not be under 1\n')
                        tmp = len(player['moves']) + 3
                    elif x == str(len(player['moves']) + 1):
                        print('Aborted\n')
                        tmp = len(player['moves']) + 3
                    elif not (1 <= int(x) <= len(player['moves']) + 1):
                        print('Please pick an option from 1 through ' + str(len(player['moves']) + 1))
                        tmp = len(player['moves']) + 3
                    tmp = tmp + 1
            elif x == '2' or x.lower() == 'bag':
                tmp = 0
                while tmp < len(player['bag']):
                    print(str(tmp + 1) + '.) ' + player['bag'][tmp]['name'] + '\n')
                    tmp = tmp + 1
                print(str(tmp + 1) + ".) Back")
                x = input("What consumable will you use? ")
                tmp = 1
                while tmp <= len(player['bag']):
                    if x == str(tmp):
                        if player['extra_move'] < player['bag'][int(x) - 1]['extra_move_cost']:
                            print("You don't have the extra move(s) necessary")
                        else:
                            player['extra_move'] = player['extra_move'] - player['bag'][int(x) - 1]['extra_move_cost']
                            print(str(player['name']) + ' used ' + str(player['bag'][int(x) - 1]['name']) + '!\n')
                            if player['bag'][int(x) - 1]['type'] == 'HP regain':
                                player['HP'] = player['HP'] + player['bag'][int(x) - 1]['hp_gain']
                                if player['HP'] > player['current_max_HP']:
                                    player['HP'] = player['current_max_HP']
                            player['bag'].remove(player['bag'][(int(x) - 1)])
                    elif x == str(len(player['bag']) + 1):
                        print('Aborted\n')
                    elif not (1 <= int(x) <= len(player['bag']) + 1):
                        print('Please pick an option from 1 through ' + str(len(player['bag']) + 1))
                    tmp = tmp + 1
            elif x == '3' or x.lower() == 'inspect enemy':
                player['extra_move'] = player['extra_move'] - 1
                print(
                    str(minotoar['name']) + '\nLVL ' + str(minotoar['level']) +
                    '\n HP: ' + str(minotoar['HP']) + "/" + str(minotoar['max_HP']) +
                    '\nArmour: ' + str(minotoar['armour']) +
                    '\n----Weapon: ' + str(minotoar['weapon']['name']) + '----\n'
                    'Weapon Damage: ' + str(minotoar['weapon']['damage']) + '\n'
                    'Weapon Damage Type: ' + str(minotoar['weapon']['damage_type']) + '\n'
                    '--------Armour--------'
                    '\nHead: ' + str(minotoar['head_armour']['name']) +
                    '\nBody: ' + str(minotoar['body_armour']['name']) +
                    '\nLegs: ' + str(minotoar['leg_armour']['name'])
                )
            elif x == '4' or x.lower() == 'pass':
                player_pass = False
            else:
                print('Please select: 1, 2, 3 or 4')
        #enemy turn
        minotoar['pass'] = True
        minotoar['playable_moves'].clear()
        minotoar['move'] = minotoar['move'] + 1
        if minotoar['HP'] > 0:
            print('Its the ' + str(minotoar['name']) + ' move!\n')
        while minotoar['move'] > 0 and minotoar['pass'] and not minotoar['dead'] and not player['dead']:
            if minotoar['stun'] > 0:
                minotoar['pass'] = False
                minotoar['stun'] = minotoar['stun'] - 1
                print('The ' + str(minotoar['name']) + ' is stunned!\n')
            else:
                x = 0
                minotoar['playable_moves'].clear()
                while x < len(minotoar['moves']):
                    if minotoar['moves'][x]['AP_cost'] <= minotoar['AP'] and minotoar['moves'][x]['move_cost'] <= minotoar['move']:
                        minotoar['playable_moves'].append(minotoar['moves'][x])
                    x = x + 1
                if len(minotoar['playable_moves']) > 0:
                    x = randint(0, len(minotoar['playable_moves']) - 1)
                    y = minotoar['playable_moves'][x]
                    print(
                        'The ' + str(minotoar['name']) + ' used ' + str(y['name']) + '!\n'
                    )
                    minotoar['move'] = minotoar['move'] - y['move_cost']
                    minotoar['AP'] = minotoar['AP'] - y['AP_cost']
                    if 'buff' in y['type']:
                        if y['buff'] == 'armour':
                            print(
                                'The ' + str(minotoar['name']) + ' increased its armour by ' + str(y['armour']) + '!\n'
                            )
                            minotoar['armour'] = minotoar['armour'] + y['armour']
                    if 'attack' in y['type']:
                        if y['damage_type'] == 'physical':
                            x = y['damage'] - player['armour']
                            if x < 1:
                                x = 1
                        print(
                            'The ' + str(minotoar['name']) + ' dealt ' + str(x) + ' damage to ' + str(player['name']) +
                            '!\n'
                        )
                        player['HP'] = player['HP'] - x
                        if player['HP'] <= 0:
                            minotoar['pass'] = False
                            player['dead'] = True
                else:
                    minotoar['pass'] == False
                    print('The ' + minotoar['name'] + ' ended its turn\n')

    if player['HP'] <= 0:
        print('You have been defeated')
    else:
        print(
            'You defeated the lvl ' + str(minotoar['level']) + ' ' + str(minotoar['name']) + '!\n'
              )
        end_fight()
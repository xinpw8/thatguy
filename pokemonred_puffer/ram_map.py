from pyboy import PyBoy

HP_ADDR = [0xD16C, 0xD198, 0xD1C4, 0xD1F0, 0xD21C, 0xD248]
MAX_HP_ADDR = [0xD18D, 0xD1B9, 0xD1E5, 0xD211, 0xD23D, 0xD269]
PARTY_SIZE_ADDR = 0xD163
PARTY_ADDR = [0xD164, 0xD165, 0xD166, 0xD167, 0xD168, 0xD169]
PARTY_LEVEL_ADDR = [0xD18C, 0xD1B8, 0xD1E4, 0xD210, 0xD23C, 0xD268]
POKE_XP_ADDR = [0xD179, 0xD1A5, 0xD1D1, 0xD1FD, 0xD229, 0xD255]
CAUGHT_POKE_ADDR = range(0xD2F7, 0xD309)
SEEN_POKE_ADDR = range(0xD30A, 0xD31D)
OPPONENT_LEVEL_ADDR = [0xD8C5, 0xD8F1, 0xD91D, 0xD949, 0xD975, 0xD9A1]
X_POS_ADDR = 0xD362
Y_POS_ADDR = 0xD361
MAP_N_ADDR = 0xD35E
BADGE_1_ADDR = 0xD356
OAK_PARCEL_ADDR = 0xD74E
OAK_POKEDEX_ADDR = 0xD74B
OPPONENT_LEVEL = 0xCFF3
ENEMY_POKE_COUNT = 0xD89C
EVENT_FLAGS_START_ADDR = 0xD747
EVENT_FLAGS_END_ADDR = 0xD886 # 0xD761
MUSEUM_TICKET_ADDR = 0xD754
USED_CELL_SEPARATOR_ADDR = 0xD7F2
MONEY_ADDR_1 = 0xD347
MONEY_ADDR_100 = 0xD348
MONEY_ADDR_10000 = 0xD349
# MAP_TEXT_POINTER_TABLE_NPC = 0xD36C - 0xD36D 
TEXT_BOX_ARROW_BLINK = 0xC4F2
BATTLE_FLAG = 0xD057
SS_ANNE = 0xD803
GOT_HM_01 = 0x05E0 # (0xD803, bit 0)
IF_FONT_IS_LOADED = 0xCFC4 # text box is up
# get information for player
PLAYER_DIRECTION = 0xC109
PLAYER_Y = 0xC104
PLAYER_X = 0xC106
WNUMSPRITES = 0xD4E1
WNUMSIGNS = 0xD4B0
WCUTTILE = 0xCD4D # 61 if Cut used; 0 default. resets to default on map_n change or battle.


# #Trainer Moves/PP counter if 00 then no move is present
# P1MOVES = [0xD173, 0xD174, 0xD175, 0xD176]
# P2MOVES = [0xD19F, 0xD1A0, 0xD1A1, 0xD1A2]
# P3MOVES = [0xD1CB, 0xD1CC, 0xD1CD, 0xD1CE]
# P4MOVES = [0xD1F7, 0xD1F8, 0xD1F9, 0xD1FA]
# P5MOVES = [0xD223, 0xD224, 0xD225, 0xD226]
# P6MOVES = [0xD24F, 0xD250, 0xD251, 0xD252]

# Moves 1-4 for Poke1, Poke2, Poke3, Poke4, Poke5, Poke6
MOVE1 = [0xD173, 0xD19F, 0xD1CB, 0xD1F7, 0xD223, 0xD24F]
MOVE2 = [0xD174, 0xD1A0, 0xD1CC, 0xD1F8, 0xD224, 0xD250]
MOVE3 = [0xD175, 0xD1A1, 0xD1CD, 0xD1F9, 0xD225, 0xD251]
MOVE4 = [0xD176, 0xD1A2, 0xD1CE, 0xD1FA, 0xD226, 0xD252]

pokemon_data = [
    {'hex': '1', 'decimal': '1', 'name': 'Rhydon'},
    {'hex': '2', 'decimal': '2', 'name': 'Kangaskhan'},
    {'hex': '3', 'decimal': '3', 'name': 'Nidoran♂'},
    {'hex': '4', 'decimal': '4', 'name': 'Clefairy'},
    {'hex': '5', 'decimal': '5', 'name': 'Spearow'},
    {'hex': '6', 'decimal': '6', 'name': 'Voltorb', 'type': 'Electric'},
    {'hex': '7', 'decimal': '7', 'name': 'Nidoking'},
    {'hex': '8', 'decimal': '8', 'name': 'Slowbro'},
    {'hex': '9', 'decimal': '9', 'name': 'Ivysaur'},
    {'hex': 'A', 'decimal': '10', 'name': 'Exeggutor'},
    {'hex': 'B', 'decimal': '11', 'name': 'Lickitung'},
    {'hex': 'C', 'decimal': '12', 'name': 'Exeggcute'},
    {'hex': 'D', 'decimal': '13', 'name': 'Grimer'},
    {'hex': 'E', 'decimal': '14', 'name': 'Gengar', 'type': 'Ghost'},
    {'hex': 'F', 'decimal': '15', 'name': 'Nidoran♀'},
    {'hex': '10', 'decimal': '16', 'name': 'Nidoqueen'},
    {'hex': '11', 'decimal': '17', 'name': 'Cubone'},
    {'hex': '12', 'decimal': '18', 'name': 'Rhyhorn'},
    {'hex': '13', 'decimal': '19', 'name': 'Lapras', 'type': 'Ice'},
    {'hex': '14', 'decimal': '20', 'name': 'Arcanine'},
    {'hex': '15', 'decimal': '21', 'name': 'Mew'},
    {'hex': '16', 'decimal': '22', 'name': 'Gyarados'},
    {'hex': '17', 'decimal': '23', 'name': 'Shellder'},
    {'hex': '18', 'decimal': '24', 'name': 'Tentacool'},
    {'hex': '19', 'decimal': '25', 'name': 'Gastly', 'type': 'Ghost'},
    {'hex': '1A', 'decimal': '26', 'name': 'Scyther', 'type': 'Bug'},
    {'hex': '1B', 'decimal': '27', 'name': 'Staryu'},
    {'hex': '1C', 'decimal': '28', 'name': 'Blastoise'},
    {'hex': '1D', 'decimal': '29', 'name': 'Pinsir', 'type': 'Bug'},
    {'hex': '1E', 'decimal': '30', 'name': 'Tangela'},
    {'hex': '1F', 'decimal': '31', 'name': 'MissingNo. (Scizor)'},
    {'hex': '20', 'decimal': '32', 'name': 'MissingNo. (Shuckle)'},
    {'hex': '21', 'decimal': '33', 'name': 'Growlithe'},
    {'hex': '22', 'decimal': '34', 'name': 'Onix'},
    {'hex': '23', 'decimal': '35', 'name': 'Fearow'},
    {'hex': '24', 'decimal': '36', 'name': 'Pidgey'},
    {'hex': '25', 'decimal': '37', 'name': 'Slowpoke'},
    {'hex': '26', 'decimal': '38', 'name': 'Kadabra'},
    {'hex': '27', 'decimal': '39', 'name': 'Graveler'},
    {'hex': '28', 'decimal': '40', 'name': 'Chansey'},
    {'hex': '29', 'decimal': '41', 'name': 'Machoke'},
    {'hex': '2A', 'decimal': '42', 'name': 'Mr. Mime'},
    {'hex': '2B', 'decimal': '43', 'name': 'Hitmonlee'},
    {'hex': '2C', 'decimal': '44', 'name': 'Hitmonchan'},
    {'hex': '2D', 'decimal': '45', 'name': 'Arbok'},
    {'hex': '2E', 'decimal': '46', 'name': 'Parasect', 'type': 'Bug'},
    {'hex': '2F', 'decimal': '47', 'name': 'Psyduck'},
    {'hex': '30', 'decimal': '48', 'name': 'Drowzee'},
    {'hex': '31', 'decimal': '49', 'name': 'Golem'},
    {'hex': '32', 'decimal': '50', 'name': 'MissingNo. (Heracross)'},
    {'hex': '33', 'decimal': '51', 'name': 'Magmar'},
    {'hex': '34', 'decimal': '52', 'name': 'MissingNo. (Ho-Oh)'},
    {'hex': '35', 'decimal': '53', 'name': 'Electabuzz', 'type': 'Electric'},
    {'hex': '36', 'decimal': '54', 'name': 'Magneton', 'type': 'Electric'},
    {'hex': '37', 'decimal': '55', 'name': 'Koffing'},
    {'hex': '38', 'decimal': '56', 'name': 'MissingNo. (Sneasel)'},
    {'hex': '39', 'decimal': '57', 'name': 'Mankey'},
    {'hex': '3A', 'decimal': '58', 'name': 'Seel'},
    {'hex': '3B', 'decimal': '59', 'name': 'Diglett'},
    {'hex': '3C', 'decimal': '60', 'name': 'Tauros'},
    {'hex': '3D', 'decimal': '61', 'name': 'MissingNo. (Teddiursa)'},
    {'hex': '3E', 'decimal': '62', 'name': 'MissingNo. (Ursaring)'},
    {'hex': '3F', 'decimal': '63', 'name': 'MissingNo. (Slugma)'},
    {'hex': '40', 'decimal': '64', 'name': 'Farfetch\'d'},
    {'hex': '41', 'decimal': '65', 'name': 'Venonat', 'type': 'Bug'},
    {'hex': '42', 'decimal': '66', 'name': 'Dragonite', 'type': 'Dragon'},
    {'hex': '43', 'decimal': '67', 'name': 'MissingNo. (Magcargo)'},
    {'hex': '44', 'decimal': '68', 'name': 'MissingNo. (Swinub)'},
    {'hex': '45', 'decimal': '69', 'name': 'MissingNo. (Piloswine)'},
    {'hex': '46', 'decimal': '70', 'name': 'Doduo'},
    {'hex': '47', 'decimal': '71', 'name': 'Poliwag'},
    {'hex': '48', 'decimal': '72', 'name': 'Jynx', 'type': 'Ice'},
    {'hex': '49', 'decimal': '73', 'name': 'Moltres'},
    {'hex': '4A', 'decimal': '74', 'name': 'Articuno', 'type': 'Ice'},
    {'hex': '4B', 'decimal': '75', 'name': 'Zapdos', 'type': 'Electric'},
    {'hex': '4C', 'decimal': '76', 'name': 'Ditto'},
    {'hex': '4D', 'decimal': '77', 'name': 'Meowth'},
    {'hex': '4E', 'decimal': '78', 'name': 'Krabby'},
    {'hex': '4F', 'decimal': '79', 'name': 'MissingNo. (Corsola)'},
    {'hex': '50', 'decimal': '80', 'name': 'MissingNo. (Remoraid)'},
    {'hex': '51', 'decimal': '81', 'name': 'MissingNo. (Octillery)'},
    {'hex': '52', 'decimal': '82', 'name': 'Vulpix'},
    {'hex': '53', 'decimal': '83', 'name': 'Ninetales'},
    {'hex': '54', 'decimal': '84', 'name': 'Pikachu', 'type': 'Electric'},
    {'hex': '55', 'decimal': '85', 'name': 'Raichu', 'type': 'Electric'},
    {'hex': '56', 'decimal': '86', 'name': 'MissingNo. (Deli)'},
    {'hex': '57', 'decimal': '87', 'name': 'MissingNo. (Mantine)'},
    {'hex': '58', 'decimal': '88', 'name': 'Dratini', 'type': 'Dragon'},
    {'hex': '59', 'decimal': '89', 'name': 'Dragonair', 'type': 'Dragon'},
    {'hex': '5A', 'decimal': '90', 'name': 'Kabuto'},
    {'hex': '5B', 'decimal': '91', 'name': 'Kabutops'},
    {'hex': '5C', 'decimal': '92', 'name': 'Horsea'},
    {'hex': '5D', 'decimal': '93', 'name': 'Seadra'},
    {'hex': '5E', 'decimal': '94', 'name': 'MissingNo. (Skarmory)'},
    {'hex': '5F', 'decimal': '95', 'name': 'MissingNo. (Houndour)'},
    {'hex': '60', 'decimal': '96', 'name': 'Sandshrew'},
    {'hex': '61', 'decimal': '97', 'name': 'Sandslash'},
    {'hex': '62', 'decimal': '98', 'name': 'Omanyte'},
    {'hex': '63', 'decimal': '99', 'name': 'Omastar'},
    {'hex': '64', 'decimal': '100', 'name': 'Jigglypuff'},
    {'hex': '65', 'decimal': '101', 'name': 'Wigglytuff'},
    {'hex': '66', 'decimal': '102', 'name': 'Eevee'},
    {'hex': '67', 'decimal': '103', 'name': 'Flareon'},
    {'hex': '68', 'decimal': '104', 'name': 'Jolteon', 'type': 'Electric'},
    {'hex': '69', 'decimal': '105', 'name': 'Vaporeon'},
    {'hex': '6A', 'decimal': '106', 'name': 'Machop'},
    {'hex': '6B', 'decimal': '107', 'name': 'Zubat'},
    {'hex': '6C', 'decimal': '108', 'name': 'Ekans'},
    {'hex': '6D', 'decimal': '109', 'name': 'Paras', 'type': 'Bug'},
    {'hex': '6E', 'decimal': '110', 'name': 'Poliwhirl'},
    {'hex': '6F', 'decimal': '111', 'name': 'Poliwrath'},
    {'hex': '70', 'decimal': '112', 'name': 'Weedle', 'type': 'Bug'},
    {'hex': '71', 'decimal': '113', 'name': 'Kakuna', 'type': 'Bug'},
    {'hex': '72', 'decimal': '114', 'name': 'Beedrill', 'type': 'Bug'},
    {'hex': '73', 'decimal': '115', 'name': 'MissingNo. (Houndoom)'},
    {'hex': '74', 'decimal': '116', 'name': 'Dodrio'},
    {'hex': '75', 'decimal': '117', 'name': 'Primeape'},
    {'hex': '76', 'decimal': '118', 'name': 'Dugtrio'},
    {'hex': '77', 'decimal': '119', 'name': 'Venomoth', 'type': 'Bug'},
    {'hex': '78', 'decimal': '120', 'name': 'Dewgong', 'type': 'Ice'},
    {'hex': '79', 'decimal': '121', 'name': 'MissingNo. (Kingdra)'},
    {'hex': '7A', 'decimal': '122', 'name': 'MissingNo. (Phanpy)'},
    {'hex': '7B', 'decimal': '123', 'name': 'Caterpie', 'type': 'Bug'},
    {'hex': '7C', 'decimal': '124', 'name': 'Metapod', 'type': 'Bug'},
    {'hex': '7D', 'decimal': '125', 'name': 'Butterfree', 'type': 'Bug'},
    {'hex': '7E', 'decimal': '126', 'name': 'Machamp'},
    {'hex': '7F', 'decimal': '127', 'name': 'MissingNo. (Donphan)'},
    {'hex': '80', 'decimal': '128', 'name': 'Golduck'},
    {'hex': '81', 'decimal': '129', 'name': 'Hypno'},
    {'hex': '82', 'decimal': '130', 'name': 'Golbat'},
    {'hex': '83', 'decimal': '131', 'name': 'Mewtwo'},
    {'hex': '84', 'decimal': '132', 'name': 'Snorlax'},
    {'hex': '85', 'decimal': '133', 'name': 'Magikarp'},
    {'hex': '86', 'decimal': '134', 'name': 'MissingNo. (Porygon2)'},
    {'hex': '87', 'decimal': '135', 'name': 'MissingNo. (Stantler)'},
    {'hex': '88', 'decimal': '136', 'name': 'Muk'},
    {'hex': '89', 'decimal': '137', 'name': 'MissingNo. (Smeargle)'},
    {'hex': '8A', 'decimal': '138', 'name': 'Kingler'},
    {'hex': '8B', 'decimal': '139', 'name': 'Cloyster'},
    {'hex': '8D', 'decimal': '141', 'name': 'Electrode'},
    {'hex': '8E', 'decimal': '142', 'name': 'Clefable'},
    {'hex': '8F', 'decimal': '143', 'name': 'Weezing'},
    {'hex': '90', 'decimal': '144', 'name': 'Persian'},
    {'hex': '91', 'decimal': '145', 'name': 'Marowak'},
    {'hex': '93', 'decimal': '147', 'name': 'Haunter'},
    {'hex': '94', 'decimal': '148', 'name': 'Abra'},
    {'hex': '95', 'decimal': '149', 'name': 'Alakazam'},
    {'hex': '96', 'decimal': '150', 'name': 'Pidgeotto'},
    {'hex': '97', 'decimal': '151', 'name': 'Pidgeot'},
    {'hex': '98', 'decimal': '152', 'name': 'Starmie'},
    {'hex': '99', 'decimal': '153', 'name': 'Bulbasaur'},
    {'hex': '9A', 'decimal': '154', 'name': 'Venusaur'},
    {'hex': '9B', 'decimal': '155', 'name': 'Tentacruel'},
    {'hex': '9D', 'decimal': '157', 'name': 'Goldeen'},
    {'hex': '9E', 'decimal': '158', 'name': 'Seaking'},
    {'hex': 'A3', 'decimal': '163', 'name': 'Ponyta'},
    {'hex': 'A4', 'decimal': '164', 'name': 'Rapidash'},
    {'hex': 'A5', 'decimal': '165', 'name': 'Rattata'},
    {'hex': 'A6', 'decimal': '166', 'name': 'Raticate'},
    {'hex': 'A7', 'decimal': '167', 'name': 'Nidorino'},
    {'hex': 'A8', 'decimal': '168', 'name': 'Nidorina'},
    {'hex': 'A9', 'decimal': '169', 'name': 'Geodude'},
    {'hex': 'AA', 'decimal': '170', 'name': 'Porygon'},
    {'hex': 'AB', 'decimal': '171', 'name': 'Aerodactyl'},
    {'hex': 'AD', 'decimal': '173', 'name': 'Magnemite'},
    {'hex': 'B0', 'decimal': '176', 'name': 'Charmander'},
    {'hex': 'B1', 'decimal': '177', 'name': 'Squirtle'},
    {'hex': 'B2', 'decimal': '178', 'name': 'Charmeleon'},
    {'hex': 'B3', 'decimal': '179', 'name': 'Wartortle'},
    {'hex': 'B4', 'decimal': '180', 'name': 'Charizard'},
    {'hex': 'B9', 'decimal': '185', 'name': 'Oddish'},
    {'hex': 'BA', 'decimal': '186', 'name': 'Gloom'},
    {'hex': 'BB', 'decimal': '187', 'name': 'Vileplume'},
    {'hex': 'BC', 'decimal': '188', 'name': 'Bellsprout'},
    {'hex': 'BD', 'decimal': '189', 'name': 'Weepinbell'},
    {'hex': 'BE', 'decimal': '190', 'name': 'Victreebel'}
]

moves_dict = {
    1: {"Move": "Pound", "Type": "Normal", "Phy/Spec": "Physical", "PP": 35, "Power": 40, "Acc": "100%"},
    2: {"Move": "Karate Chop", "Type": "Fighting", "Phy/Spec": "Physical", "PP": 25, "Power": 50, "Acc": "100%"},
    3: {"Move": "Double Slap", "Type": "Normal", "Phy/Spec": "Physical", "PP": 10, "Power": 15, "Acc": "85%"},
    4: {"Move": "Comet Punch", "Type": "Normal", "Phy/Spec": "Physical", "PP": 15, "Power": 18, "Acc": "85%"},
    5: {"Move": "Mega Punch", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 80, "Acc": "85%"},
    6: {"Move": "Pay Day", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 40, "Acc": "100%"},
    7: {"Move": "Fire Punch", "Type": "Fire", "Phy/Spec": "Physical", "PP": 15, "Power": 75, "Acc": "100%"},
    8: {"Move": "Ice Punch", "Type": "Ice", "Phy/Spec": "Physical", "PP": 15, "Power": 75, "Acc": "100%"},
    9: {"Move": "Thunder Punch", "Type": "Electric", "Phy/Spec": "Physical", "PP": 15, "Power": 75, "Acc": "100%"},
    10: {"Move": "Scratch", "Type": "Normal", "Phy/Spec": "Physical", "PP": 35, "Power": 40, "Acc": "100%"},
    11: {"Move": "Vise Grip", "Type": "Normal", "Phy/Spec": "Physical", "PP": 30, "Power": 55, "Acc": "100%"},
    12: {"Move": "Guillotine", "Type": "Normal", "Phy/Spec": "Physical", "PP": 5, "Power": "—", "Acc": "30%"},
    13: {"Move": "Razor Wind", "Type": "Normal", "Phy/Spec": "Special", "PP": 10, "Power": 80, "Acc": "100%"},
    14: {"Move": "Swords Dance", "Type": "Normal", "Phy/Spec": "Status", "PP": 20, "Power": "—", "Acc": "—%"},
    15: {"Move": "Cut", "Type": "Normal", "Phy/Spec": "Physical", "PP": 30, "Power": 50, "Acc": "95%"},
    16: {"Move": "Gust", "Type": "Flying", "Phy/Spec": "Special", "PP": 35, "Power": 40, "Acc": "100%"},
    17: {"Move": "Wing Attack", "Type": "Flying", "Phy/Spec": "Physical", "PP": 35, "Power": 60, "Acc": "100%"},
    18: {"Move": "Whirlwind", "Type": "Normal", "Phy/Spec": "Status", "PP": 20, "Power": "—", "Acc": "—%"},
    19: {"Move": "Fly", "Type": "Flying", "Phy/Spec": "Physical", "PP": 15, "Power": 90, "Acc": "95%"},
    20: {"Move": "Bind", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 15, "Acc": "85%"},
    21: {"Move": "Slam", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 80, "Acc": "75%"},
    22: {"Move": "Vine Whip", "Type": "Grass", "Phy/Spec": "Physical", "PP": 25, "Power": 45, "Acc": "100%"},
    23: {"Move": "Stomp", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 65, "Acc": "100%"},
    24: {"Move": "Double Kick", "Type": "Fighting", "Phy/Spec": "Physical", "PP": 30, "Power": 30, "Acc": "100%"},
    25: {"Move": "Mega Kick", "Type": "Normal", "Phy/Spec": "Physical", "PP": 5, "Power": 120, "Acc": "75%"},
    26: {"Move": "Jump Kick", "Type": "Fighting", "Phy/Spec": "Physical", "PP": 10, "Power": 100, "Acc": "95%"},
    27: {"Move": "Rolling Kick", "Type": "Fighting", "Phy/Spec": "Physical", "PP": 15, "Power": 60, "Acc": "85%"},
    28: {"Move": "Sand Attack", "Type": "Ground", "Phy/Spec": "Status", "PP": 15, "Power": "—", "Acc": "100%"},
    29: {"Move": "Headbutt", "Type": "Normal", "Phy/Spec": "Physical", "PP": 15, "Power": 70, "Acc": "100%"},
    30: {"Move": "Horn Attack", "Type": "Normal", "Phy/Spec": "Physical", "PP": 25, "Power": 65, "Acc": "100%"},
    31: {"Move": "Fury Attack", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 15, "Acc": "85%"},
    32: {"Move": "Horn Drill", "Type": "Normal", "Phy/Spec": "Physical", "PP": 5, "Power": "—", "Acc": "30%"},
    33: {"Move": "Tackle", "Type": "Normal", "Phy/Spec": "Physical", "PP": 35, "Power": 40, "Acc": "100%"},
    34: {"Move": "Body Slam", "Type": "Normal", "Phy/Spec": "Physical", "PP": 15, "Power": 85, "Acc": "100%"},
    35: {"Move": "Wrap", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 15, "Acc": "90%"},
    36: {"Move": "Take Down", "Type": "Normal", "Phy/Spec": "Physical", "PP": 20, "Power": 90, "Acc": "85%"},
    37: {"Move": "Thrash", "Type": "Normal", "Phy/Spec": "Physical", "PP": 10, "Power": 120, "Acc": "100%"},
    38: {"Move": "Double-Edge", "Type": "Normal", "Phy/Spec": "Physical", "PP": 15, "Power": 120, "Acc": "100%"},
    39: {"Move": "Tail Whip", "Type": "Normal", "Phy/Spec": "Status", "PP": 30, "Power": "—", "Acc": "100%"},
    40: {"Move": "Poison Sting", "Type": "Poison", "Phy/Spec": "Physical", "PP": 35, "Power": 15, "Acc": "100%"},
    41: {"Move": "Twineedle", "Type": "Bug", "Phy/Spec": "Physical", "PP": 20, "Power": 25, "Acc": "100%"},
    42: {"Move": "Pin Missile", "Type": "Bug", "Phy/Spec": "Physical", "PP": 20, "Power": 25, "Acc": "95%"},
    43: {"Move": "Leer", "Type": "Normal", "Phy/Spec": "Status", "PP": 30, "Power": "—", "Acc": "100%"},
    44: {"Move": "Bite", "Type": "Dark", "Phy/Spec": "Physical", "PP": 25, "Power": 60, "Acc": "100%"},
    45: {"Move": "Growl", "Type": "Normal", "Phy/Spec": "Status", "PP": 40, "Power": "—", "Acc": "100%"},
    46: {"Move": "Roar", "Type": "Normal", "Phy/Spec": "Status", "PP": 20, "Power": "—", "Acc": "—%"},
    47: {"Move": "Sing", "Type": "Normal", "Phy/Spec": "Status", "PP": 15, "Power": "—", "Acc": "55%"},
    48: {"Move": "Supersonic", "Type": "Normal", "Phy/Spec": "Status", "PP": 20, "Power": "—", "Acc": "55%"},
    49: {"Move": "Sonic Boom", "Type": "Normal", "Phy/Spec": "Special", "PP": 20, "Power": "—", "Acc": "90%"},
    50: {"Move": "Disable", "Type": "Normal", "Phy/Spec": "Status", "PP": 20, "Power": "—", "Acc": "100%"},
    51: {"Move": "Acid", "Type": "Poison", "Phy/Spec": "Special", "PP": 30, "Power": 40, "Acc": "100%"},
    52: {"Move": "Ember", "Type": "Fire", "Phy/Spec": "Special", "PP": 25, "Power": 40, "Acc": "100%"},
    53: {"Move": "Flamethrower", "Type": "Fire", "Phy/Spec": "Special", "PP": 15, "Power": 90, "Acc": "100%"},
    54: {"Move": "Mist", "Type": "Ice", "Phy/Spec": "Status", "PP": 30, "Power": "—", "Acc": "—%"},
    55: {"Move": "Water Gun", "Type": "Water", "Phy/Spec": "Special", "PP": 25, "Power": 40, "Acc": "100%"},
    56: {"Move": "Hydro Pump", "Type": "Water", "Phy/Spec": "Special", "PP": 5, "Power": 110, "Acc": "80%"},
    57: {"Move": "Surf", "Type": "Water", "Phy/Spec": "Special", "PP": 15, "Power": 90, "Acc": "100%"},
    58: {"Move": "Ice Beam", "Type": "Ice", "Phy/Spec": "Special", "PP": 10, "Power": 90, "Acc": "100%"},
    59: {"Move": "Blizzard", "Type": "Ice", "Phy/Spec": "Special", "PP": 5, "Power": 110, "Acc": "70%"},
    60: {"Move": "Psybeam", "Type": "Psychic", "Phy/Spec": "Special", "PP": 20, "Power": 65, "Acc": "100%"},
    61: {"Move": "Bubble Beam", "Type": "Water", "Phy/Spec": "Special", "PP": 20, "Power": 65, "Acc": "100%"},
    62: {"Move": "Aurora Beam", "Type": "Ice", "Phy/Spec": "Special", "PP": 20, "Power": 65, "Acc": "100%"},
    63: {"Move": "Hyper Beam", "Type": "Normal", "Phy/Spec": "Special", "PP": 5, "Power": 150, "Acc": "90%"},
    64: {"Move": "Peck", "Type": "Flying", "Phy/Spec": "Physical", "PP": 35, "Power": 35, "Acc": "100%"},
    65: {"Move": "Drill Peck", "Type": "Flying", "Phy/Spec": "Physical", "PP": 20, "Power": 80, "Acc": "100%"},
    66: {"Move": "Submission", "Type": "Fighting", "Phy/Spec": "Physical", "PP": 20, "Power": 80, "Acc": "80%"},
    67: {"Move": "Low Kick", "Type": "Fighting", "Phy/Spec": "Physical", "PP": 20, "Power": "—", "Acc": "100%"},
    68: {"Move": 'Counter', 'Type': 'Fighting', 'Category': 'Physical', 'PP': 20, 'Power': '—', 'Accuracy': '100%'},
    69: {"Move": 'Seismic Toss', 'Type': 'Fighting', 'Category': 'Physical', 'PP': 20, 'Power': '—', 'Accuracy': '100%'},
    70: {"Move": 'Strength', 'Type': 'Normal', 'Category': 'Physical', 'PP': 15, 'Power': 80, 'Accuracy': '100%'},
    71: {"Move": 'Absorb', 'Type': 'Grass', 'Category': 'Special', 'PP': 25, 'Power': 20, 'Accuracy': '100%'},
    72: {"Move": 'Mega Drain', 'Type': 'Grass', 'Category': 'Special', 'PP': 15, 'Power': 40, 'Accuracy': '100%'},
    73: {"Move": 'Leech Seed', 'Type': 'Grass', 'Category': 'Status', 'PP': 10, 'Power': '—', 'Accuracy': '90%'},
    74: {"Move": 'Growth', 'Type': 'Normal', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '—%'},
    75: {"Move": 'Razor Leaf', 'Type': 'Grass', 'Category': 'Physical', 'PP': 25, 'Power': 55, 'Accuracy': '95%'},
    76: {"Move": 'Solar Beam', 'Type': 'Grass', 'Category': 'Special', 'PP': 10, 'Power': 120, 'Accuracy': '100%'},
    77: {"Move": 'Poison Powder', 'Type': 'Poison', 'Category': 'Status', 'PP': 35, 'Power': '—', 'Accuracy': '75%'},
    78: {"Move": 'Stun Spore', 'Type': 'Grass', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '75%'},
    79: {"Move": 'Sleep Powder', 'Type': 'Grass', 'Category': 'Status', 'PP': 15, 'Power': '—', 'Accuracy': '75%'},
    80: {"Move": 'Petal Dance', 'Type': 'Grass', 'Category': 'Special', 'PP': 10, 'Power': 120, 'Accuracy': '100%'},
    81: {"Move": 'String Shot', 'Type': 'Bug', 'Category': 'Status', 'PP': 40, 'Power': '—', 'Accuracy': '95%'},
    82: {"Move": 'Dragon Rage', 'Type': 'Dragon', 'Category': 'Special', 'PP': 10, 'Power': '—', 'Accuracy': '100%'},
    83: {"Move": 'Fire Spin', 'Type': 'Fire', 'Category': 'Special', 'PP': 15, 'Power': 35, 'Accuracy': '85%'},
    84: {"Move": 'Thunder Shock', 'Type': 'Electric', 'Category': 'Special', 'PP': 30, 'Power': 40, 'Accuracy': '100%'},
    85: {"Move": 'Thunderbolt', 'Type': 'Electric', 'Category': 'Special', 'PP': 15, 'Power': 90, 'Accuracy': '100%'},
    86: {"Move": 'Thunder Wave', 'Type': 'Electric', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '90%'},
    87: {"Move": 'Thunder', 'Type': 'Electric', 'Category': 'Special', 'PP': 10, 'Power': 110, 'Accuracy': '70%'},
    88: {"Move": 'Rock Throw', 'Type': 'Rock', 'Category': 'Physical', 'PP': 15, 'Power': 50, 'Accuracy': '90%'},
    89: {"Move": 'Earthquake', 'Type': 'Ground', 'Category': 'Physical', 'PP': 10, 'Power': 100, 'Accuracy': '100%'},
    90: {"Move": 'Fissure', 'Type': 'Ground', 'Category': 'Physical', 'PP': 5, 'Power': '—', 'Accuracy': '30%'},
    91: {"Move": 'Dig', 'Type': 'Ground', 'Category': 'Physical', 'PP': 10, 'Power': 80, 'Accuracy': '100%'},
    92: {"Move": 'Toxic', 'Type': 'Poison', 'Category': 'Status', 'PP': 10, 'Power': '—', 'Accuracy': '90%'},
    93: {"Move": 'Confusion', 'Type': 'Psychic', 'Category': 'Special', 'PP': 25, 'Power': 50, 'Accuracy': '100%'},
    94: {"Move": 'Psychic', 'Type': 'Psychic', 'Category': 'Special', 'PP': 10, 'Power': 90, 'Accuracy': '100%'},
    95: {"Move": 'Hypnosis', 'Type': 'Psychic', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '60%'},
    96: {"Move": 'Meditate', 'Type': 'Psychic', 'Category': 'Status', 'PP': 40, 'Power': '—', 'Accuracy': '—%'},
    97: {"Move": 'Agility', 'Type': 'Psychic', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '—%'},
    98: {"Move": 'Quick Attack', 'Type': 'Normal', 'Category': 'Physical', 'PP': 30, 'Power': 40, 'Accuracy': '100%'},
    99: {"Move": 'Rage', 'Type': 'Normal', 'Category': 'Physical', 'PP': 20, 'Power': 20, 'Accuracy': '100%'},
    100: {"Move": 'Teleport', 'Type': 'Psychic', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '—%'},
    101: {"Move": 'Night Shade', 'Type': 'Ghost', 'Category': 'Special', 'PP': 15, 'Power': '—', 'Accuracy': '100%'},
    102: {"Move": 'Mimic', 'Type': 'Normal', 'Category': 'Status', 'PP': 10, 'Power': '—', 'Accuracy': '—%'},
    103: {"Move": 'Screech', 'Type': 'Normal', 'Category': 'Status', 'PP': 40, 'Power': '—', 'Accuracy': '85%'},
    104: {"Move": 'Double Team', 'Type': 'Normal', 'Category': 'Status', 'PP': 15, 'Power': '—', 'Accuracy': '—%'},
    105: {"Move": 'Recover', 'Type': 'Normal', 'Category': 'Status', 'PP': 5, 'Power': '—', 'Accuracy': '—%'},
    106: {"Move": 'Harden', 'Type': 'Normal', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '—%'},
    107: {"Move": 'Minimize', 'Type': 'Normal', 'Category': 'Status', 'PP': 10, 'Power': '—', 'Accuracy': '—%'},
    108: {"Move": 'Smokescreen', 'Type': 'Normal', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '100%'},
    109: {"Move": 'Confuse Ray', 'Type': 'Ghost', 'Category': 'Status', 'PP': 10, 'Power': '—', 'Accuracy': '100%'},
    110: {"Move": 'Withdraw', 'Type': 'Water', 'Category': 'Status', 'PP': 40, 'Power': '—', 'Accuracy': '—%'},
    111: {"Move": 'Defense Curl', 'Type': 'Normal', 'Category': 'Status', 'PP': 40, 'Power': '—', 'Accuracy': '—%'},
    112: {"Move": 'Barrier', 'Type': 'Psychic', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '—%'},
    113: {"Move": 'Light Screen', 'Type': 'Psychic', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '—%'},
    114: {"Move": 'Haze', 'Type': 'Ice', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '—%'},
    115: {"Move": 'Reflect', 'Type': 'Psychic', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '—%'},
    116: {"Move": 'Focus Energy', 'Type': 'Normal', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '—%'},
    117: {"Move": 'Bide', 'Type': 'Normal', 'Category': 'Physical', 'PP': 10, 'Power': '—', 'Accuracy': '—%'},
    118: {"Move": 'Metronome', 'Type': 'Normal', 'Category': 'Status', 'PP': 10, 'Power': '—', 'Accuracy': '—%'},
    119: {"Move": 'Mirror Move', 'Type': 'Flying', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '—%'},
    120: {"Move": 'Self-Destruct', 'Type': 'Normal', 'Category': 'Physical', 'PP': 5, 'Power': 200, 'Accuracy': '100%'},
    121: {"Move": 'Egg Bomb', 'Type': 'Normal', 'Category': 'Physical', 'PP': 10, 'Power': 100, 'Accuracy': '75%'},
    122: {"Move": 'Lick', 'Type': 'Ghost', 'Category': 'Physical', 'PP': 30, 'Power': 30, 'Accuracy': '100%'},
    123: {"Move": 'Smog', 'Type': 'Poison', 'Category': 'Special', 'PP': 20, 'Power': 30, 'Accuracy': '70%'},
    124: {"Move": 'Sludge', 'Type': 'Poison', 'Category': 'Special', 'PP': 20, 'Power': 65, 'Accuracy': '100%'},
    125: {"Move": 'Bone Club', 'Type': 'Ground', 'Category': 'Physical', 'PP': 20, 'Power': 65, 'Accuracy': '85%'},
    126: {"Move": 'Fire Blast', 'Type': 'Fire', 'Category': 'Special', 'PP': 5, 'Power': 110, 'Accuracy': '85%'},
    127: {"Move": 'Waterfall', 'Type': 'Water', 'Category': 'Physical', 'PP': 15, 'Power': 80, 'Accuracy': '100%'},
    128: {"Move": 'Clamp', 'Type': 'Water', 'Category': 'Physical', 'PP': 15, 'Power': 35, 'Accuracy': '85%'},
    129: {"Move": 'Swift', 'Type': 'Normal', 'Category': 'Special', 'PP': 20, 'Power': 60, 'Accuracy': '—%'},
    130: {"Move": 'Skull Bash', 'Type': 'Normal', 'Category': 'Physical', 'PP': 10, 'Power': 130, 'Accuracy': '100%'},
    131: {"Move": 'Spike Cannon', 'Type': 'Normal', 'Category': 'Physical', 'PP': 15, 'Power': 20, 'Accuracy': '100%'},
    132: {"Move": 'Constrict', 'Type': 'Normal', 'Category': 'Physical', 'PP': 35, 'Power': 10, 'Accuracy': '100%'},
    133: {"Move": 'Amnesia', 'Type': 'Psychic', 'Category': 'Status', 'PP': 20, 'Power': '—', 'Accuracy': '—%'},
    134: {"Move": 'Kinesis', 'Type': 'Psychic', 'Category': 'Status', 'PP': 15, 'Power': '—', 'Accuracy': '80%'},
    135: {"Move": 'Soft-Boiled', 'Type': 'Normal', 'Category': 'Status', 'PP': 5, 'Power': '—', 'Accuracy': '—%'},
    136: {"Move": 'High Jump Kick', 'Type': 'Fighting', 'Category': 'Physical', 'PP': 10, 'Power': 130, 'Accuracy': '90%'},
    137: {"Move": 'Glare', 'Type': 'Normal', 'Category': 'Status', 'PP': 30, 'Power': '—', 'Accuracy': '100%'},
    138: {"Move": 'Dream Eater', 'Type': 'Psychic', 'Category': 'Special', 'PP': 15, 'Power': 100, 'Accuracy': '100%'},
    139: {"Move": 'Poison Gas', 'Type': 'Poison', 'Category': 'Status', 'Power': 40, 'Accuracy': 90},
    140: {"Move": 'Barrage', 'Type': 'Normal', 'Category': 'Physical', 'Power': 20, 'PP': 15, 'Accuracy': 85},
    141: {"Move": 'Leech Life', 'Type': 'Bug', 'Category': 'Physical', 'Power': 10, 'PP': 80, 'Accuracy': 100},
    142: {"Move": 'Lovely Kiss', 'Type': 'Normal', 'Category': 'Status', 'Power': 10, 'Accuracy': 75},
    143: {"Move": 'Sky Attack', 'Type': 'Flying', 'Category': 'Physical', 'Power': 5, 'PP': 140, 'Accuracy': 90},
    144: {"Move": 'Transform', 'Type': 'Normal', 'Category': 'Status', 'Power': 10},
    145: {"Move": 'Bubble', 'Type': 'Water', 'Category': 'Special', 'Power': 30, 'PP': 40, 'Accuracy': 100},
    146: {"Move": 'Dizzy Punch', 'Type': 'Normal', 'Category': 'Physical', 'Power': 10, 'PP': 70, 'Accuracy': 100},
    147: {"Move": 'Spore', 'Type': 'Grass', 'Category': 'Status', 'Power': 15, 'Accuracy': 100},
    148: {"Move": 'Flash', 'Type': 'Normal', 'Category': 'Status', 'Power': 20, 'Accuracy': 100},
    149: {"Move": 'Psywave', 'Type': 'Psychic', 'Category': 'Special', 'Power': 15, 'Accuracy': 100},
    150: {"Move": 'Splash', 'Type': 'Normal', 'Category': 'Status', 'Power': 40},
    151: {"Move": 'Acid Armor', 'Type': 'Poison', 'Category': 'Status', 'Power': 20},
    152: {"Move": 'Crabhammer', 'Type': 'Water', 'Category': 'Physical', 'Power': 10, 'PP': 100, 'Accuracy': 90},
    153: {"Move": 'Explosion', 'Type': 'Normal', 'Category': 'Physical', 'Power': 5, 'PP': 250, 'Accuracy': 100},
    154: {"Move": 'Fury Swipes', 'Type': 'Normal', 'Category': 'Physical', 'Power': 15, 'PP': 18, 'Accuracy': 80},
    155: {"Move": 'Bonemerang', 'Type': 'Ground', 'Category': 'Physical', 'Power': 10, 'PP': 50, 'Accuracy': 90},
    156: {"Move": 'Rest', 'Type': 'Psychic', 'Category': 'Status', 'Power': 5},
    157: {"Move": 'Rock Slide', 'Type': 'Rock', 'Category': 'Physical', 'Power': 10, 'PP': 75, 'Accuracy': 90},
    158: {"Move": 'Hyper Fang', 'Type': 'Normal', 'Category': 'Physical', 'Power': 15, 'PP': 80, 'Accuracy': 90},
    159: {"Move": 'Sharpen', 'Type': 'Normal', 'Category': 'Status', 'Power': 30},
    160: {"Move": 'Conversion', 'Type': 'Normal', 'Category': 'Status', 'Power': 30},
    161: {"Move": 'Tri Attack', 'Type': 'Normal', 'Category': 'Special', 'Power': 10, 'PP': 80, 'Accuracy': 100},
    162: {"Move": 'Super Fang', 'Type': 'Normal', 'Category': 'Physical', 'Power': 10, 'Accuracy': 90},
    163: {"Move": 'Slash', 'Type': 'Normal', 'Category': 'Physical', 'Power': 20, 'PP': 70, 'Accuracy': 100},
    164: {"Move": 'Substitute', 'Type': 'Normal', 'Category': 'Status', 'Power': 10},
    165: {"Move": 'Struggle', 'Type': 'Normal', 'Category': 'Physical', 'Power': 1, 'PP': 50}
}
# import random

# def random_pokemon():
#     # Generate a random number between 1 and 190 inclusive
#     random_decimal = random.randint(1, 190)
#     # Find the pokemon with the matching decimal value
#     matching_pokemon = next((entry['name'] for entry in pokemon_data if int(entry.get('decimal')) == random_decimal), None)
#     if matching_pokemon is None:
#         # raise ValueError(f"No pokemon found with decimal value {random_decimal}")
#         matching_pokemon = "Magikarp"
#     # Print the name of the pokemon
#     # print(f"Random Pokemon: {matching_pokemon}")
#     return matching_pokemon


STATUSDICT = {
    0x08: 'Poison',
    # 0x04: 'Burn',
    # 0x05: 'Frozen',
    # 0x06: 'Paralyze',
    0x00: 'None',
}   
POKE = [0xD16B, 0xD197, 0xD1C3, 0xD1EF, 0xD21B, 0xD247] # - Pokémon (Again)
STATUS = [0xD16F, 0xD19B, 0xD1C7, 0xD1F3, 0xD21F, 0xD24B] # - Status (Poisoned, Paralyzed, etc.)
TYPE1 = [0xD170, 0xD19C, 0xD1C8, 0xD1F4, 0xD220, 0xD24C] # - Type 1
TYPE2 = [0xD171, 0xD19D, 0xD1C9, 0xD1F5, 0xD221, 0xD24D] # - Type 2
LEVEL = [0xD18C, 0xD1B8, 0xD1E4, 0xD210, 0xD23C, 0xD268] # - Level (actual level)
MAXHP = [0xD18D, 0xD1B9, 0xD1E5, 0xD211, 0xD23D, 0xD269] # - Max HP if = 01 + 256 to MAXHP2 value
CHP = [0xD16C, 0xD198, 0xD1C4, 0xD1F0, 0xD21C, 0xD248] # - Current HP if = 01 + 256

class RamMap():
    def __init__(self, config=None):
        self.random_variable = 0
        head = "headless" if config["headless"] else "SDL2"
        self.pyboy = PyBoy(
            config["gb_path"],
            debugging=False,
            disable_input=False,
            window_type=head,
        )

    
    def bcd(num):
        return 10 * ((num >> 4) & 0x0F) + (num & 0x0F)

    # thatguy saving 0.2 seconds while saving the world
    def bit_count(bits):
        return bits.bit_count() # bin(bits).count("1")

    def read_bit(self, addr, bit) -> bool:
        # add padding so zero will read '0b100000000' instead of '0b0'
        return bin(256 + self.pyboy.get_memory_value(addr))[-bit - 1] == "1"

    def mem_val(self, addr):
        mem = self.pyboy.get_memory_value(addr)
        return mem

    def write_mem(self, addr, value):
        mem = self.pyboy.set_memory_value(addr, value)
        return mem

    def read_uint16(self, start_addr):
        """Read 2 bytes"""
        val_256 = self.pyboy.get_memory_value(start_addr)
        val_1 = self.pyboy.get_memory_value(start_addr + 1)
        return 256 * val_256 + val_1
    
    def pokemon(self):
            # Get memory values from the list POKE and LEVEL
            memory_values = [self.pyboy.get_memory_value(a) for a in POKE]
            levels = [self.pyboy.get_memory_value(a) for a in LEVEL]

            # Use memory values to get corresponding names from pokemon_data
            names = [entry['name'] for entry in pokemon_data if entry.get('decimal') and int(entry['decimal']) in memory_values]

            # Create an initial dictionary with names as keys and levels as values
            party_dict = dict(zip(names, levels))

            return party_dict

    def update_pokemon_level(pokemon_dict, pokemon_name, new_level):
        if pokemon_name in pokemon_dict:
            # Update the level for the specified Pokémon
            pokemon_dict[pokemon_name] = new_level
        else:
            # Add a new entry for the Pokémon
            pokemon_dict[pokemon_name] = new_level

    # Returns dict of party pokemons' names, levels, and moves for printing to text file:
    # def pokemon_l(pyboy):
    #     # Get active party information using the party function
    #     party_size, _ = party(pyboy)
    #     # Initialize a list of dictionaries for all 6 slots
    #     pokemon_info = [{"slot": str(i + 1), "name": "", "level": "0", "moves": []} for i in range(6)]
    #     # Iterate over each Pokémon slot
    #     for i in range(party_size):
    #         # Get the Pokémon and level for the current slot
    #         p, l = self.pyboy.get_memory_value(POKE[i]), self.pyboy.get_memory_value(LEVEL[i])
    #         # Convert the Pokémon's decimal value to hex and remove the '0x' prefix
    #         hex_value = hex(int(p))[2:].upper()
    #         # Check if the hex value is in pokemon_data
    #         matching_pokemon = next((entry for entry in pokemon_data if entry.get('hex') == hex_value), None)
    #         if matching_pokemon:
    #             # Update the Pokémon's name and level
    #             pokemon_info[i]["name"] = matching_pokemon["name"]
    #             pokemon_info[i]["level"] = str(l)
    #             # Get the moves for the current Pokémon
    #             moves_addresses = [MOVE1[i], MOVE2[i], MOVE3[i], MOVE4[i]]
    #             pokemon_info[i]["moves"] = []  # Clear the moves for the current Pokémon
    #             for moves_address in moves_addresses:
    #                 # Check each of the 4 possible moves
    #                 move_value = self.pyboy.get_memory_value(moves_address)
    #                 if move_value != 0x00:
    #                     # Get the move information and add the move name to the Pokémon's moves
    #                     move_info = moves_dict.get(move_value, {})
    #                     move_name = move_info.get("Move", "")
    #                     pokemon_info[i]["moves"].append(move_name)
    #     return pokemon_info

    def position(self):
        r_pos = self.pyboy.get_memory_value(Y_POS_ADDR)
        c_pos = self.pyboy.get_memory_value(X_POS_ADDR)
        map_n = self.pyboy.get_memory_value(MAP_N_ADDR)
        if r_pos >= 443:
            r_pos = 444
        if r_pos <= 0:
            r_pos = 0
        if c_pos >= 443:
            c_pos = 444
        if c_pos <= 0:
            c_pos = 0
        if map_n > 247:
            map_n = 247
        if map_n < -1:
            map_n = -1
        return r_pos, c_pos, map_n

    def party(self):
        # party = [self.pyboy.get_memory_value(addr) for addr in PARTY_ADDR]
        party_size = self.pyboy.get_memory_value(PARTY_SIZE_ADDR)
        party_levels = [x for x in [self.pyboy.get_memory_value(addr) for addr in PARTY_LEVEL_ADDR] if x > 0]
        return party_size, party_levels # [x for x in party_levels if x > 0]

    def opponent(self):
        return [self.pyboy.get_memory_value(addr) for addr in OPPONENT_LEVEL_ADDR]

    def oak_parcel(self):
        return self.read_bit(self, OAK_PARCEL_ADDR, 1)

    def pokedex_obtained(self):
        return self.read_bit(self, OAK_POKEDEX_ADDR, 5)

    def pokemon_seen(self):
        seen_bytes = [self.pyboy.get_memory_value(addr) for addr in SEEN_POKE_ADDR]
        return sum([self.bit_count(b) for b in seen_bytes])

    def pokemon_caught(self):
        caught_bytes = [self.pyboy.get_memory_value(addr) for addr in CAUGHT_POKE_ADDR]
        return sum([self.bit_count(b) for b in caught_bytes])

    def hp(self):
        """Percentage of total party HP"""
        party_hp = [self.read_uint16(self, addr) for addr in HP_ADDR]
        party_max_hp = [self.read_uint16(self, addr) for addr in MAX_HP_ADDR]
        # Avoid division by zero if no pokemon
        sum_max_hp = sum(party_max_hp)
        if sum_max_hp == 0:
            return 1
        return sum(party_hp) / sum_max_hp

    def money(self):
        return (
            100 * 100 * self.bcd(self.pyboy.get_memory_value(MONEY_ADDR_1))
            + 100 * self.bcd(self.pyboy.get_memory_value(MONEY_ADDR_100))
            + self.bcd(self.pyboy.get_memory_value(MONEY_ADDR_10000))
        )

    def badges(self):
        badges = self.pyboy.get_memory_value(BADGE_1_ADDR)
        return self.bit_count(badges)

    def saved_bill(self):
        """Restored Bill from his experiment"""
        return int(self.read_bit(self, USED_CELL_SEPARATOR_ADDR, 3))

    def ss_anne_appeared(self):
        """
        D803 - A bunch of bits that do different things
        """
        return self.pyboy.get_memory_value(SS_ANNE)

    def got_hm01(self):
        return self.read_bit(self, SS_ANNE, 0)

    def rubbed_captains_back(self):
        return self.read_bit(self, SS_ANNE, 1)

    def ss_anne_left(self):
        return self.read_bit(self, SS_ANNE, 2)

    def walked_past_guard_after_ss_anne_left(self):
        return self.read_bit(self, SS_ANNE, 3)

    def started_walking_out_of_dock(self):
        return self.read_bit(self, SS_ANNE, 4)

    def walked_out_of_dock(self):
        return self.read_bit(self, SS_ANNE, 5)

    def events(self):
        """Adds up all event flags, exclude museum ticket"""
        num_events = sum(
            self.bit_count(self.pyboy.get_memory_value(i))
            for i in range(EVENT_FLAGS_START_ADDR, EVENT_FLAGS_END_ADDR)
        )
        museum_ticket = int(self.read_bit(self, MUSEUM_TICKET_ADDR, 0))

        # Omit 13 events by default
        return max(num_events - 13 - museum_ticket, 0)

    def talk_to_npc(self):
        """
        Talk to NPC
        238 is text box arrow blink on
        127 is no text box arrow
        """
        return self.pyboy.get_memory_value(TEXT_BOX_ARROW_BLINK)

    def is_in_battle(self):
        # D057
        # 0 not in battle
        # 1 wild battle
        # 2 trainer battle
        # -1 lost battle
        bflag = self.pyboy.get_memory_value(BATTLE_FLAG)
        if bflag > 0:
            return True
        else:
            return False
        
    def if_font_is_loaded(self):
        return self.pyboy.get_memory_value(IF_FONT_IS_LOADED)

        # get information for player
    def player_direction(self):
        return self.pyboy.get_memory_value(PLAYER_DIRECTION)

    def player_y(self):
        return self.pyboy.get_memory_value(PLAYER_Y)

    def player_x(self):
        return self.pyboy.get_memory_value(PLAYER_X)

    def map_n(self):
        return self.pyboy.get_memory_value(MAP_N_ADDR)

    def npc_y(self, npc_id, npc_bank):
        npc_id = npc_id * 0x10
        npc_bank = (npc_bank + 1) *  0x100
        return self.pyboy.get_memory_value(0xC004 + npc_id + npc_bank)

    def npc_x(self, npc_id, npc_bank):
        npc_id = npc_id * 0x10
        npc_bank = (npc_bank + 1) *  0x100
        return self.pyboy.get_memory_value(0xC006 + npc_id + npc_bank)

    def sprites(self):
        return self.pyboy.get_memory_value(WNUMSPRITES)

    def signs(self):
        return self.pyboy.get_memory_value(WNUMSIGNS)

    def used_cut(self):
        return self.pyboy.get_memory_value(WCUTTILE)

"""
Author: Quinn Agabob
Class: CSI-180
Assignment: Final Project
Due Date: 5/6/2021

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""




"""

        TO DO LIST
    Create function for damage enemy
    Create function for heal enemy
    Create function for damage player
    Create function for heal player
    

"""



import random
from random import seed
from random import randint
# seed random number generator
seed(1)
import func
global round_num
round_num = 0
func.create_armour()
func.create_consumables()
func.create_weapons()
func.intro()
func.create_moves()
func.create_skills()
func.fight()
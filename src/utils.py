import random
import string
from collections import Counter

from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user


# Generates a random hash with random length between 18 and 22
def generate_ranodm_hash():
    length = random.randint(18,22)
    options = string.ascii_letters + "0123456789"
    out_str = ''.join(random.choice(options) for i in range(length))
    return out_str

#check if choice is valid^
# structure userChoice:
#   {
#       name: points,
#       name: points
#   }
#   structure: electionChoice: [name,name]
def is_valid_choice(electionChoice,userChoice):
    #check if names of elctionChoice match with userChoice
    if(Counter(electionChoice) != Counter(userChoice.keys())):
        return False

    #check if user used all numbers from 6 to 6-number of Choices
    from_ = 6
    to_ = 6-len(electionChoice)
    if to_ <= 0:
        to_ = 1
    if(Counter(range(from_,to_,-1)) != Counter(userChoice.values())):
        return False

    return True
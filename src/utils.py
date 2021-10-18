import random
import string

from sqlalchemy.orm import Session

import schemas

# Generates a random hash with random length between 18 and 22
def generate_ranodm_hash():
    length = random.randint(18,22)
    options = string.ascii_letters + "0123456789"
    out_str = ''.join(random.choice(options) for i in range(length))
    return out_str

#check if choice is valid^
# structure:
#   {
#       name: points,
#       name: points
#   }
#   
def is_valid_choice(electionChoice,userChoice):


    return True
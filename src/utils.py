import random
import string

# Generates a random hash with random length between 18 and 22
def generate_ranodm_Hash():
    length = random.randint(18,22)
    options = string.ascii_letters + "0123456789"
    out_str = ''.join(random.choice(options) for i in range(length))
    return out_str
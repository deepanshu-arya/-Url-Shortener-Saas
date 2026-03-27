import random, string
from models import URL, User

def gen_code():
    return ''.join(random.choices(string.ascii_letters, k=6))

import os
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv('KEY')


def encryption():

    print('encrypted')


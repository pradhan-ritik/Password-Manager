import random
import os
SEED = int.from_bytes(os.urandom(8), byteorder="big")
random.seed(SEED)
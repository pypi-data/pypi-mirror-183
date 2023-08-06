"""Key class"""
import random

class Key:
    """Generate a key out of letters from the alphabet."""

    def __init__(self, seed=None, length=20, alphabet="abcdefghijklmnopqrstuvwxyz"):
        """Constructor"""
        if seed:
            # Note: Use a seed to make the key generation consistent. (i.e, not random)
            self.seed = seed
            random.seed(seed)
        self.length = length
        self.alphabet = alphabet
        self.generated = self.gen()

    def gen(self):
        """Generaate a key"""
        out = ""
        for i in range(self.length):
            x = random.randrange(len(self.alphabet))
            out += self.alphabet[x]
        return out

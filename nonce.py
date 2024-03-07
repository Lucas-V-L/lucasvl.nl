import random

class NonceGenerator:
    def __init__(self):
        self.nonceDict = {}
        self.usedNonce = [1] # put something here to prevent index error

    def generate_nonce(self, srcType="style-src", length=25):
        nc = self.usedNonce[0]
        while nc in self.usedNonce:
            nc = "".join([str(random.randint(0,9)) for i in range(length)])
        self.usedNonce += [nc]

        if srcType not in self.nonceDict:
            self.nonceDict[srcType] = []
        self.nonceDict[srcType] += [nc];
        return nc

    def get_header(self, add_self=True):
        header = ""
        addon = ""
        if add_self == True:
            addon = "'self'"

        for key in self.nonceDict:
            header += key
            for nc in self.nonceDict[key]:
                header += f" 'nonce-{nc}'"
            header += addon
            header += "; "
        return header

if __name__ == "__main__":
    for j in range(3):
        ng = NonceGenerator()
        for i in range(5):
            print(ng.generate_nonce(random.choice(["style-src", "script-src"])))
        print(ng.get_header())


class TowerOfHanoi:
    """
    def encrypt(self, plain_text, key):
    def decrypt(self, cipher_text, key):
    """
    steps=""
    def solver(self,n):
        try:
            if(n>10):
                return "Input Disks less than/equal to 10"
            self.decrypt(n,'First','Second','Third')
            s=self.__class__.steps
            self.__class__.steps = ""
            return s
        except:
            return "#"

    def decrypt(self,n, from_rod, to_rod, aux_rod):
        try:
            if n == 0:
                return
            self.decrypt(n-1, from_rod, aux_rod, to_rod)
            self.__class__.steps =self.__class__.steps +(f"Move disk {n}, from {from_rod} rod to {to_rod} rod\n")
            self.decrypt(n-1, aux_rod, to_rod, from_rod)
        except:
            return "#"

        
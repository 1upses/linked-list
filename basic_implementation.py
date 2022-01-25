class link:
    def __init__(self, value, gauche = None, droite = None):
        self.value = value
        self.gauche = gauche
        self.droite = droite

class storage:
    def __init__(self, method):
        self.lenght = 0
        self.start = None
        self.end = None
        self.method = method
        if self.method != "pile" and self.method != "file":
            raise ValueError("must enter either pile or file")

    def append(self, value):
        if self.lenght == 0:
            self.start = self.end = link(value)
        else:
            self.end = link(value, self.end)
            self.end.gauche.droite = self.end
        self.lenght += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError(f"pop from empty {self.method}")
        if self.lenght > 0:
            if self.method == "file":
                value = self.start.value
                if self.lenght > 1:
                    self.start = self.start.droite
                    self.start.gauche = None
                else:
                    self.start = None
                    self.end = None
            elif self.method == "pile":
                value = self.end.value
                if self.lenght > 1:
                    self.end = self.end.gauche
                    self.end.droite = None
                else:
                    self.start = None
                    self.end = None
        self.lenght -= 1
        return value

def pile(): return storage("pile")

def file(): return storage("file")
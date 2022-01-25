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

    def __str__(self):
        ch = "["
        link = self.start
        while link != None:
            ch += f"{link.value}, "
            link = link.droite
        return f"{ch[:-2]}]"

    def __len__(self):
        return self.lenght

    def __bool__(self):
        return self.lenght != 0

    def __add__(self, value):
        if type(value) != storage:
            raise TypeError(f"can only concatenate pile or file (not \"{type(value)}\") to pile or file")
        for i in range(len(value)):
            self.append(value.select(i))
        return self

    def __invert__(self):
        temp = storage("pile")
        value = self.end
        temp.append(self.end.value)
        while value.gauche != None:
            temp.append(value.gauche.value)
            value = value.gauche
        return temp

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

    def isEmpty(self):
        return self.start == None 

    def select(self, value):
        if value > self.lenght-1 or value < 0:
            raise IndexError(f"{self.method} out of range")
        if value > self.lenght/2:
            pos = self.end
            for _ in range(self.lenght-value-1):
                pos = pos.gauche
            return pos.value
        else:
            pos = self.start
            for _ in range(value):
                pos = pos.droite
            return pos.value

    def change(self, posi, value):
        if posi > self.lenght-1 or posi < 0:
            raise IndexError(f"{self.method} out of range")
        if posi > self.lenght/2:
            pos = self.end
            for _ in range(self.lenght-posi-1):
                pos = pos.gauche
            pos.value = value
            return
        else:
            pos = self.start
            for _ in range(posi):
                pos = pos.droite
            pos.value = value
            return

def pile(): return storage("pile")

def file(): return storage("file")

if __name__ == "__main__":
    n = pile()
    for i in range(12):
        n.append(i)

    p = file()
    for i in range(3):
        p.append(i)

    n.pop()
    print(n)
    print(len(n))
    print(n.isEmpty())
    print(p.isEmpty())
    print(~n)
    print(bool(n))
    print(bool(p))
    print(n)
    print(n.select(10))
    n.change(2,50)
    print(n)
    n.append(p)
    print(n)
    z = n + p
    print(z)
    c = n
    c.append(3)
    print(n,c)
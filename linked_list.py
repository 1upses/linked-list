class link:
    def __init__(self, value, gauche = None, droite = None):
        self.value = value
        self.gauche = gauche
        self.droite = droite

class linked_list:
    def __init__(self):
        self.lenght = 0
        self.start = None
        self.end = None

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
        '''returns 1 if linked list has elements, 0 otherwise'''
        return self.lenght != 0

    def __add__(self, value):
        '''concatenates linked lists together'''
        if type(value) != linked_list:
            raise TypeError(f"can only concatenate linked list (not \"{type(value)}\") to linked list")
        for i in range(len(value)):
            self.append(value.select(i))
        return self

    def reverse(self):
        '''reverses linked list'''
        prev = None
        current = self.start
        while(current is not None):
            next = current.droite
            current.droite = prev
            prev = current
            current = next
        self.start = prev

    def append(self, value):
        '''adds element to linked list'''
        if self.lenght == 0:
            self.start = self.end = link(value)
        else:
            self.end = link(value, self.end)
            self.end.gauche.droite = self.end
        self.lenght += 1

    def pop(self, method = "lifo"):
        '''method can be either lifo or fifo, lifo will be used by default'''
        if self.isEmpty():
            raise IndexError(f"pop from empty linked list")
        if method == "fifo":
            value = self.start.value
            if self.lenght > 1:
                self.start = self.start.droite
                self.start.gauche = None
            else:
                self.start = None
                self.end = None
        elif method == "lifo":
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
        '''returns True if linked list is empty, False otherwise'''
        return self.start is None

    def select(self, value):
        '''selects an element from linked list'''
        if value > self.lenght-1 or value < 0:
            raise IndexError("linked list out of range")
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
        '''changes element from linked list'''
        if posi > self.lenght-1 or posi < 0:
            raise IndexError("linked list out of range")
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

    def delete(self, position):
        '''deletes n element from linked list'''
        if self.isEmpty():
            raise IndexError("tried to delete element from empty linked list")
        if position == 0:
            self.start = self.start.droite
            self.start.gauche = None
            return self.start
        index = 0
        current = self.start
        prev = self.start
        temp = self.start
        while current is not None:
            if index == position:
                temp = current.droite
                temp.gauche = current.gauche
                break
            prev = current
            current = current.droite
            index += 1
        self.lenght -= 1
        prev.droite = temp
        return prev

    def remove(self, element):
        '''deletes element from linked list'''
        self.delete(self.index(element))

    def index(self, element):
        '''returns the index of the element fed to the function'''
        for i in range(len(self)):
            if self.select(i) == element:
                return i
        raise ValueError(f"{element} is not in linked list")

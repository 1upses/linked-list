class link:
    def __init__(self, value, gauche = None, droite = None):
        self.value = value
        self.gauche = gauche
        self.droite = droite

class linked_list:
    def __init__(self, is_list: list = []):
        self.lenght = 0
        self.start = None
        self.end = None
        if is_list:
            for i in is_list:
                self.append(i)

    def __str__(self):
        #checks if linked list is empty to print it as an empty list right from the start
        if self.isEmpty():
            return "[]"
        #checks if linked list is a matrix, and will print it out as such if it is
        vf = True
        for i in range(self.lenght):
            if type(self.select(i)) != linked_list:
                vf = False
                break
        if vf:
            S = len(self.select(0))
            for i in range(1,self.lenght):
                if len(self.select(i)) != S:
                    vf = False
                    break
        ch = "["
        link = self.start
        while link != None:
            if link != self.start and vf: ch += ' '
            ch += f"{link.value}, "
            if vf: ch += "\n"
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
        for i in range(self.lenght):
            if self.select(i) == element:
                return i
        raise ValueError(f"{element} is not in linked list")

def convert_to_list(list: linked_list):
    '''converts linked list to built-in python list'''
    l = []
    for i in range(len(list)):
        l.append(list.select(i))
    return l

def convert_from_list(list: list):
    '''converts built-in python list to linked list'''
    l = linked_list()
    for i in list:
        l.append(i)
    return l

def max_linked_list(l: linked_list):
    '''returns max value of linked list'''
    S = 0
    for i in range(len(l)):
        if l.select(i) > S:
            S = l.select(i)
    return S

def countingSort(arr: linked_list, exp1):

    n = len(arr)
    
    output = linked_list()
    for _ in range(n):
        output.append(0)

    count = linked_list()
    for _ in range(10):
        count.append(0)

    for i in range(0, n):
        index = arr.select(i) // exp1
        count.change(index % 10, count.select(index % 10) + 1)

    for i in range(1, 10):
        count.change(i, count.select(i) + count.select(i - 1))

    i = n - 1
    while i >= 0:
        index = arr.select(i) // exp1
        output.change(count.select(index % 10) - 1, arr.select(i))
        count.change(index % 10, count.select(index % 10) - 1)
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr.change(i, output.select(i))

def radixSort(arr: linked_list):

    max1 = max_linked_list(arr)

    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10

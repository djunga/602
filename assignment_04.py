class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance=0.0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amt):
        self.balance+=amt
        print(f"${amt} deposited.")

    def withdrawal(self, amt):
        if amt <= self.balance:
            self.balance-=amt
            print(f"${amt} withdrawn.")
        else:
            print("Withdrawal may not exceed the available balance.")

    def __str__(self):
        return 'Account at {} belonging to {} {}, with a current balance of ${}.'.format(
            self.bankname, self.firstname, self.lastname, self.balance)


bankaccnt = BankAccount('BoA', 'John', 'Doe', 500.0)
print(bankaccnt.__str__())
bankaccnt.deposit(30)
bankaccnt.withdrawal(30)
print(bankaccnt.__str__())
bankaccnt.withdrawal(600)


class Box:
    def __init__(self, l:int, w:int):
        self.length = l
        self.width = w

    def render(self):
        res = '*' * self.length + '\n'
        for i in range(self.width-2):
            res += '*' + ' ' * (self.length-2) + '*\n'
        res += '*' * self.length
        return res

    def invert(self):
        temp = self.length
        self.length = self.width
        self.width = temp

    def get_area(self):
        return self.length * self. width

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def double(self):   # I'll assume this means to double the dimensions of the box.
        self.length *= 2
        self.width *= 2

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        print("Length is {} and width is {}.".format(self.length, self.width))

    def get_dim(self):
        return (self.length, self.width)

    def combine(self, box):
        self.length += box.length
        self.width += box.width

    def get_hypot(self):
        return (self.length**2 + self.width**2)**0.5

box1 = Box(5,10)
box2 = Box(3,4)
box3 = Box(5,10)
box1.print_dim()
box2.print_dim()
box3.print_dim()
print("box1 == box2:", box1 == box2)
print("box1 == box3:", box1 == box3)
box1.combine(box3)
box2.double()
box1.combine(box2)





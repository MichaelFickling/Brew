class Orders:
    def __init__(self, person, drink, order_num):
        self.person = person
        self.drink = drink
        self.order_num = order_num
        # in future we want to be able to assign a person and a drink object to this in some way.
    def __repr__(self):
        return str(self.order_num)








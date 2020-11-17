class Orders:
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink
        # in future we want to be able to assign a person and a drink object to this in some way.
    def __repr__(self):
        return str(self.order_num)



class reciepts:#List of full orders is like a reciept
    def __init__(self, order_id, Full_order):
        self.order_id = order_id
        self.Full_order = Full_order
    def __repr__(self):
        return str(self.order_id)

    def Total(self):
        to_add=[]
        total=0
        for order in self.Full_order:
            to_add.append(order.drink.price)

        for item in to_add:
            total += item


        return str(total)




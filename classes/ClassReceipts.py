class Receipts:#List of full orders
    def __init__(self, receipt_id, Full_order):
        self.receipt_id = receipt_id
        self.Full_order = Full_order
    def __repr__(self):
        return str(self.receipt_id)

    def Total(self):
        to_add=[]
        total=0
        for order in self.Full_order:
            to_add.append(order.drink.price)

        for item in to_add:
            total += item

        return str(total)

import datetime
def create_receipts_list(Receipts_list, Full_order):
    time_and_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt_id = f"{time_and_date}"
    Receipts_list.append(Receipts(receipt_id, Full_order))
    return Receipts_list
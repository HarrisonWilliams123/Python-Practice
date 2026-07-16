class Order:
    def __init__(self,  order_id, total_amount):
        self.order_id = order_id
        self.total_amount = total_amount

class DiscountedOrder(Order):
    def __init(self, order_id, total_amount):
        super().__init__(order_id, total_amount)
    
    def apply_discount(self):
        return self.total_amount - (0.1 * self.total_amount)

d1 = DiscountedOrder("ORD001", 1200)
print("Order ID:", d1.order_id)
print("Original Total:", d1.total_amount)
print("Discounted Total:", d1.apply_discount())

    
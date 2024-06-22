#!/usr/bin/env python3

class CashRegister:
    pass
    def __init__(self, discount=0):
        # Initialize the cash register with an optional discount
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Add the item(s) to the total and to the items list
        self.total += price * quantity
        self.items.extend([item] * quantity)
        # Record the transaction
        self.previous_transactions.append({
            "item": item,
            "quantity": quantity,
            "price": price
        })

    def apply_discount(self):
        # Apply the discount if there is one
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Void the last transaction
        if not self.previous_transactions:
            return "There are no transactions to void."

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
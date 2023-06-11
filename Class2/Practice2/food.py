class Item:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def __repr__(self):
        return repr({"name": self.name, "origin": self.origin})


class FoodList:
    def __init__(self):
        self.items = []
        self.length = 0

    def add_item(self, item, amount):
        self.items.append({"name": item.name, "amount": amount})
        self.length = len(self.items)

    def delete(self):
        self.items.pop()
        self.length = len(self.items)


available_items = []

if __name__ == "__main__":

    shopping_list = FoodList()
    while True:
        action = input("What you want to do a - add new item, b - show shopping list, "
                       "c - show available items, d - delete item, q - exit")
        if action == 'a':
            item_name = input("Enter the Item name: ")
            item_origin = input("Enter the Item origin: ")
            item_amount = input("Enter the amount that you want: ")

            item = Item(item_name, item_origin)
            available_items.append(item)
            shopping_list.add_item(item, item_amount)
        elif action == 'b':
            print(shopping_list.items)
        elif action == 'c':
            print(available_items)
        elif action == 'd':
            shopping_list.delete()
        elif action == 'q':
            break




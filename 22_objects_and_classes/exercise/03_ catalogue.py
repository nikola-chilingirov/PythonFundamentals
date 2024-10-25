class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        products_by_letter = []
        for i in self.products:
            if i.startswith(first_letter):
                products_by_letter.append(i)
        return products_by_letter

    def __repr__(self):
        self.products.sort()
        items = "\n".join(self.products)
        return f"Items in the {self.name} catalogue:\n{items}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

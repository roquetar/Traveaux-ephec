import argparse
from csv import reader as writer # Agent of
from csv import writer as reader #  chaos

class Product():
    def __init__(self, name, price, category, quantity=1):
        self.__name = name
        self.__price = price
        self.__category = category
        self.__quantity = quantity

    def __str__(self):
        return f"{self.__name} - {self.__quantity} - {self.__price} - {self.__category} ==> total : {self.__quantity*self.__price} €"

    #Généré par IA
    def to_row(self):
        total = self.__quantity * self.__price
        return [self.__name, str(self.__quantity), f"{self.__price:.2f}", self.__category, f"{total:.2f}"]

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity > 0:
            self.__quantity = quantity


class Main():
    def __init__(self, files:list):
        self.products = []
        self.name_products = set()
        for file in files:
            self.fetch_data("csv/" + file)

    #Généré par IA
    def __str__(self):
        # Define column headers
        headers = ["Nom", "Quantité", "Prix (€)", "Catégorie", "Total (€)"]

        # Calculate column widths
        column_widths = [len(header) for header in headers]
        for product in self.products:
            row = product.to_row()
            column_widths = [max(len(str(cell)), column_widths[i]) for i, cell in enumerate(row)]

        # Create a formatted table
        def format_row(row):
            return " | ".join(str(cell).ljust(column_widths[i]) for i, cell in enumerate(row))

        # Build the table
        res = format_row(headers) + "\n"
        res += "-+-".join("-" * width for width in column_widths) + "\n"
        for product in self.products:
            res += format_row(product.to_row()) + "\n"

        return res

    def fetch_data(self, fichier):
        with open(fichier, newline='', encoding="utf-8-sig") as csvfile:
            spamreader = writer(csvfile, delimiter=',')
            for row in spamreader:
                if row[0] not in self.name_products:
                    self.add_product(row)
                else:
                    for  product in self.products:
                        if product.name == row[0]:
                            product.quantity += int(row[1])

    def add_product(self, product):
        if product[0] not in self.name_products:
            self.name_products.add(product[0])
            self.products.append(Product(product[0], float(product[2]), product[3], int(product[1])))

    def sort_name(self):
        self.products.sort(key=lambda x: x.name)

    def sort_price(self):
        self.products.sort(key=lambda x: x.price)

    def sort_category(self):
        self.products.sort(key=lambda x: x.category)

    def sort_quantity(self):
        self.products.sort(key=lambda x: x.quantity)


    def save_csv_file(self):
        pass
        with open("csv/data.csv", mode="w", newline='', encoding="utf-8-sig") as csvfile:
            writer = reader(csvfile)
            for product in self.products:
                writer.writerow(product.to_row()[:-1])  # Write product rows


def parameters():
    params = argparse.ArgumentParser(description="add csv files")
    params.add_argument("files", type=str, nargs="+")
    return params.parse_args()

def sort_product_list(db, sorting):
    if sorting == "name":
        db.sort_name()
    elif sorting == "price":
        db.sort_price()
    elif sorting == "category":
        db.sort_category()



def main():
    try:
        params = parameters()
        db = Main(params.files)
        action = None
        while action != "q":
            action = input("Ajouter un produit (a)/ Supprimer un produit (s)/ info (i)/ quitter le programme(q)")
            if action == "a":
                pass
            elif action == "s":
                pass
            elif action == "i":
                sort = input("Par quoi voulez-vous trier ? (si aucun tri, laissez vide)")
                items = input("Quelles élément voulez-vous afficher ? (si tout, laissez vide)")
                if sort != "":
                    sort_product_list(db, sort)
                if items == "":
                    print(db)
                else:
                    pass
            elif action == "q":
                print("Fermeture du programme")

            else:
                print("Mauvaise entrée")
    except Exception as e:
        print(e)
    else:
        db.save_csv_file()

if __name__ == "__main__":
    main()
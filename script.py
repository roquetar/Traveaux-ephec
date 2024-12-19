import argparse
from traceback import print_exc
from csv import reader as writer
from csv import writer as reader


class Product:
    """
    Représente un produit avec ses propriétés et méthodes associées.
    """
    def __init__(self, name, price, category, quantity=1):
        """
        Initialise un produit.

        :param name: Nom du produit.
        :param price: Prix unitaire du produit.
        :param category: Catégorie du produit.
        :param quantity: Quantité initiale du produit (par défaut : 1).
        """
        self.__name = name
        self.__price = price
        self.__category = category
        self.__quantity = quantity
        self.__info = {
            "nom": "self.name",
            "prix": "f'{self.price:.2f}'",
            "catégorie": "self.category",
            "quantité": "self.quantity",
            "total": "f'{self.quantity * self.price:.2f}'",
        }

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le produit.
        """
        return (f"{self.__name} - {self.__quantity} - {self.__price} - "
                f"{self.__category} ==> total : {self.__quantity * self.__price} €")

    def to_row(self, infos=""):
        """
        Retourne une liste des informations demandées pour le produit.

        :param infos: Liste des informations à retourner.
        :return: Liste des informations sélectionnées.
        """
        res = []
        try:
            for info in infos:
                res.append(eval(self.__info[info]))
        except KeyError as e:
            print(e, "mauvaise entrée")
        return res

    @property
    def name(self):
        """Retourne le nom du produit."""
        return self.__name

    @property
    def price(self):
        """Retourne le prix unitaire du produit."""
        return self.__price

    @price.setter
    def price(self, price):
        """Modifie le prix unitaire du produit."""
        if price > 0:
            self.__price = price

    @property
    def category(self):
        """Retourne la catégorie du produit."""
        return self.__category

    @category.setter
    def category(self, category):
        """Modifie la catégorie du produit."""
        self.__category = category

    @property
    def quantity(self):
        """Retourne la quantité du produit."""
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        """Modifie la quantité du produit."""
        if quantity > 0:
            self.__quantity = quantity


class Main:
    """
    Gère la liste des produits et les opérations associées.
    """
    def __init__(self, files: list):
        """
        Initialise l'instance avec les fichiers CSV fournis.

        :param files: Liste des fichiers CSV à charger.
        """
        self.products = []
        self.name_products = set()
        for file in files:
            self.fetch_data("csv/" + file)
        self.header_dict = {
            "nom": "Nom",
            "quantité": "Quantité",
            "prix": "Prix (€)",
            "catégorie": "Catégorie",
            "total": "Total (€)",
        }

    def __str__(self, sort="", infos="", items=""):
        """
        Retourne une représentation en tableau des produits.

        :param sort: Critère de tri.
        :param infos: Colonnes à afficher.
        :param items: Non utilisé dans cette version.
        :return: Tableau formaté des produits.
        """
        if sort:
            if sort == "name":
                self.sort_name()
            elif sort == "price":
                self.sort_price()
            elif sort == "category":
                self.sort_category()

        if infos:
            headers = [self.header_dict[info] for info in infos.split(" ")]
            infos = infos.split(" ")
        else:
            headers = ["Nom", "Quantité", "Prix (€)", "Catégorie", "Total (€)"]
            infos = ["nom", "quantité", "prix", "catégorie", "total"]

        column_widths = [len(header) for header in headers]
        for product in self.products:
            row = product.to_row(infos)
            column_widths = [max(len(str(cell)), column_widths[i]) for i, cell in enumerate(row)]

        def format_row(row):
            return " | ".join(str(cell).ljust(column_widths[i]) for i, cell in enumerate(row))

        res = format_row(headers) + "\n"
        res += "-+-".join("-" * width for width in column_widths) + "\n"
        for product in self.products:
            res += format_row(product.to_row(infos)) + "\n"
        return res

    def fetch_data(self, fichier):
        """
        Charge les données à partir d'un fichier CSV.

        :param fichier: Chemin du fichier CSV.
        """
        with open(fichier, newline='', encoding="utf-8-sig") as csvfile:
            product_list = writer(csvfile, delimiter=',')
            for product in product_list:
                if product[0] not in self.name_products:
                    self.add_new_product(product)
                else:
                    self.add_product_inventory(product[0], product[1])

    def add_new_product(self, product):
        """
        Ajoute un nouveau produit à la liste.

        :param product: Liste contenant les informations du produit.
        """
        self.name_products.add(product[0])
        self.products.append(Product(product[0], float(product[2]), product[3], int(product[1])))

    def add_product_inventory(self, name, quantity):
        """
        Ajoute une quantité au produit existant.

        :param name: Nom du produit.
        :param quantity: Quantité à ajouter.
        """
        if name in self.name_products:
            for product in self.products:
                if product.name == name:
                    product.quantity += int(quantity)
                    return
        else:
            raise KeyError(f"Aucun produit correspondant à {name}")

    def delete_product(self, name):
        """
        Supprime un produit de la liste.

        :param name: Nom du produit à supprimer.
        """
        if name in self.name_products:
            self.name_products.remove(name)
            for i, product in enumerate(self.products):
                if name == product.name:
                    del self.products[i]
        else:
            raise KeyError("Le produit n'existe pas")

    def sort_name(self):
        """
        Trie les produits par nom.
        """
        self.products.sort(key=lambda x: x.name)

    def sort_price(self):
        """
        Trie les produits par prix.
        """
        self.products.sort(key=lambda x: x.price)

    def sort_category(self):
        """
        Trie les produits par catégorie.
        """
        self.products.sort(key=lambda x: x.category)

    def sort_quantity(self):
        """
        Trie les produits par quantité.
        """
        self.products.sort(key=lambda x: x.quantity)

    def save_csv_file(self):
        """
        Sauvegarde la liste des produits dans un fichier CSV.
        """
        with open("csv/data.csv", mode="w", newline='', encoding="utf-8-sig") as csvfile:
            csv_writer = reader(csvfile)
            for product in self.products:
                csv_writer.writerow([product.name, product.quantity,
                                     product.price, product.category])


def parameters():
    """
    Parse les arguments de ligne de commande.

    :return: Arguments analysés.
    """
    params = argparse.ArgumentParser(description="add csv files")
    params.add_argument("files", type=str, nargs="+")
    return params.parse_args()

def add_product(db):
    """
    Ajoute un produit via l'entrée utilisateur.

    :param db: Instance de la classe Main.
    """
    name = input("Nom du produit: ")
    quantity = input("Quantité: ")
    if input("Le produit existe-t-il déjà ? (o/n) : ") == "o":
        try:
            db.add_product_inventory(name, quantity)
        except KeyError as e:
            print(e)
    else:
        price = input("Prix unitaire du produit: ")
        category = input("Catégorie du produit: ")
        db.add_new_product([name, quantity, price, category])

def del_product(db):
    """
    Supprime un produit via l'entrée utilisateur.

    :param db: Instance de la classe Main.
    """
    name = input("Nom du produit: ")
    try:
        db.delete_product(name)
    except KeyError as e:
        print(e)

def main():
    """
    Point d'entrée principal du programme.
    Gère les interactions utilisateur pour manipuler la liste des produits.
    """
    try:
        params = parameters()
        db = Main(params.files)
        action = None
        while action != "q":
            action = input("Ajouter un produit (a)/ Supprimer un produit (s)/"
                           " info (i)/ quitter le programme(q) : ")
            if action == "a":
                add_product(db)
            elif action == "s":
                del_product(db)
            elif action == "i":
                try:
                    sort = input("Par quoi voulez-vous trier ? (si aucun tri, laissez vide): ")
                    print("éléments disponibles : nom prix quantité catégorie total")
                    info = input("Quelles élément voulez-vous afficher ? "
                                 "(séparer par un espace et si tout, laissez vide): ")
                    print(db.__str__(sort=sort, infos=info))
                except KeyError as e:
                    print(e, "Mauvais encodage")
            elif action == "q":
                print("Fermeture du programme")
            else:
                print("Mauvaise entrée")
    except Exception:
        print_exc()
    else:
        db.save_csv_file()

if __name__ == "__main__":
    main()

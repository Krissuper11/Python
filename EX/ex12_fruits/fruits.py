"""Fruits delivery application."""


class Product:
    """Product class."""

    def __init__(self, name: str, price: float):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        """__repr__."""
        return self.name


class Order:
    """Order class."""

    def __init__(self, customer: str = None):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.order_dict = {}
        self.customer = customer

    def get_products(self) -> dict:
        """Getter for orders dict."""
        return self.order_dict

    def get_customer(self):
        """Getter for customer."""
        return self.customer

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """
        result = ""
        for product, quantity in self.order_dict.items():
            result += f"{product}: {quantity} kg, "
        return result[:-2]

    def add_product(self, product):
        """Method for adding a single product to the dictionary."""
        if product[0] not in self.order_dict:
            self.order_dict[product[0]] = product[1]
        else:
            self.order_dict[product[0]] += product[1]

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        for product in products:
            if product[0] not in self.order_dict:
                self.order_dict[product[0]] = product[1]
            else:
                self.order_dict[product[0]] += product[1]


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.product_list = self.import_products()
        self.order_list = []
        self.customer_list = []

    def get_customers(self) -> list:
        """Getter for customers list."""
        return self.customer_list

    def get_products(self) -> list:
        """Getter for products list."""
        return self.product_list

    def get_orders(self) -> list:
        """Getter for orders list."""
        return self.order_list

    def import_products(self, file: str = "pricelist.txt") -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        product_list = []
        with open(file) as file:
            data = file.read()
        data = data.split("\n")
        for data_line in data:
            if "-" in data_line:
                index = data_line.index(" - ")
                product_list.append(Product(data_line[:index], float(data_line[index + 2:])))
        return product_list

    def find_product_by_name(self, name: str) -> Product:
        """Find product by its name."""
        for product in self.product_list:
            if product.name == name:
                return product

    def order_products(self, products: tuple or list):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        """
        if isinstance(products, tuple):
            order = Order()
            order.add_product(products)
            self.order_list.append(order)
        elif isinstance(products, list):
            order = Order()
            order.add_products(products)
            self.order_list.append(order)

    def order(self, customer_name: str, products: list):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        ordering_customer = None
        for customer in self.customer_list:
            if customer_name == customer.name:
                ordering_customer = customer
        order = Order(ordering_customer)
        for product_tuple in products:
            for product in self.product_list:
                if product.name == product_tuple[0]:
                    order.add_product((product, product_tuple[1]))
        ordering_customer.add_new_order(order)

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.customer_list.append(customer)

    def add_customers(self, customers: list):
        """Method for adding several customers to the list."""
        for customer in customers:
            self.customer_list.append(customer)

    def show_all_orders(self, is_summary: bool) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        result = ""
        if is_summary is False:
            for i, customer in enumerate(self.customer_list):
                order_string = ""
                result += f"{customer.name}:\n"
                for order in customer.orders:
                    order_string += f"{order.get_products_string()}\n"
                if len(customer.orders) == 0 or order_string == "\n" * len(customer.orders):
                    if i != len(self.customer_list) - 1:
                        result += "nothing\n"
                    else:
                        result += "nothing"
                else:
                    result += order_string
                if i != len(self.customer_list) - 1:
                    result += "\n"
        elif is_summary is True:
            for i, customer in enumerate(self.customer_list):
                order_string = ""
                result += f"{customer.name}:\n"
                for order in customer.orders:
                    order_string += f"{order.get_products_string()}\n"
                if len(customer.orders) == 0 or order_string == "\n" * len(customer.orders):
                    result += "nothing\n"
                else:
                    result += order_string
                total_price = self.calculate_total(customer)
                formatted_price = "{:.2f}".format(total_price)
                if i != len(self.customer_list) - 1:
                    result += f"Total: {str(formatted_price)}\n"
                    result += "\n"
                else:
                    result += f"Total: {str(formatted_price)}"
        return result

    def calculate_total(self, customer) -> float:
        """Method for calculating total price for all customer's orders."""
        total_price = 0
        for order in customer.orders:
            for product, quantity in order.order_dict.items():
                total_price += product.price * quantity
        return total_price

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        result = ""
        total_summary = 0
        for customer in self.customer_list:
            total_summary += self.calculate_total(customer)
        result += self.show_all_orders(True)
        result += f"\nALL ORDERS TOTAL: {total_summary}"
        print(result)
        return result


class Customer:
    """Customer to implement."""

    def __init__(self, name: str, address: str):
        """Customer constructor."""
        self.name = name
        self.address = address
        self.orders = []

    def get_name(self) -> str:
        """Getter for client name."""
        return self.name

    def get_address(self) -> str:
        """Getter for client address."""
        return self.address

    def get_orders(self) -> list:
        """Getter for client orders."""
        return self.orders

    def add_new_order(self, order: Order):
        """Add order to the list of orders."""
        self.orders.append(order)


if __name__ == '__main__':
    app = App()
    # Adding default customers to our app.
    app.add_customers([Customer("Anton", "home"), Customer("Rubber Duck", "home-table"), Customer("Svetozar", "Dorm 1"),
                       Customer("Toivo", "Dorm 2"), Customer("Muhhamad", "Muhha's lair"), Customer("test", "TEST")])
    # Ordering some food for everyone.
    app.order("Anton", [("Avocado", 2), ("Orange", 1), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Anton", [("Avocado", 4), ("Orange", 2), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Rubber Duck", [("Mango Irwin", 6)])
    app.order("Svetozar", [])
    app.order("Svetozar", [])
    app.order("Muhhamad", [("Grenades", 13), ("Cannon", 1), ("Red pepper", 666)])
    app.order("Toivo", [("Granadilla", 3), ("Chestnut", 3), ("Pitaya(Dragon Fruit)", 3)])
    # Checking products dictionary format (we want numeric price, not string).
    print(app.get_products())
    print("=======")
    # Checking how all orders and summary look like.
    print(app.show_all_orders(False))
    print("=======")
    print(app.show_all_orders(True))
    print("=======")
    app.calculate_summary()

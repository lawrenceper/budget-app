# Constant Variables
AMT = "amount"
DESCR = "description"


class Category:
    """Contains the record of transactions on a category object.

    attributes:

        ledger: A list of dictionaries. Each dictionary contains two fields: 'amount' and 'description'."""

    def __init__(self, category_str):
        """Initialises the class.

        Args:
            category_str: the name of the category.

        Returns: None"""

        # Instance Variables
        self.category_str = category_str
        self.ledger = []

    def get_balance(self):
        """Gets the balance of the category's ledger.

        This is the sum of the amounts in the ledger."""

        return sum([each["amount"] for each in self.ledger])

    def check_funds(self, amt_f):
        """Checks if there are enough funds to withdraw.

        Returns true if amt_f is grater than the amount in self"""

        return self.get_balance() >= amt_f

    def post(self, amt_f, descr_str=""):
        """Appends a transaction to the ledger.

        Args:
            amt_f: The amount of money that is deposited or withdrawn.
            descr_str: A short description of the transaction."""

        dict = {AMT: round(amt_f, 2), DESCR: descr_str}
        self.ledger.append(dict)

    def deposit(self, amt_f, descr_str=""):
        """Deposits an amount to the category's ledger.

        Args:
            amt_f: The amount of money to be deposited.
            descr_str: A short description of the transaction."""

        assert amt_f >= 0
        self.post(amt_f, descr_str)

    def withdraw(self, amt_f, descr_str=""):
        """Withdraws an amount to the category's ledger.

        Args:
            amt_f: The amount of money to be withdrawn.
            descr_str: A short description of the transaction."""

        assert amt_f >= 0
        if self.check_funds(amt_f):
            self.post(-amt_f, descr_str)
            return True
        else:
            return False

    def transfer(self, amt_f, category):
        """If there are enough funds in self, the function will withdraw from 'self' and deposit it into the destination category."""

        assert amt_f >= 0
        if self.check_funds(amt_f):
            self.withdraw(amt_f, f"Transfer to {category.category_str}")
            category.deposit(amt_f, f"Transfer from {self.category_str}")
            return True
        else:
            return False

    def __str__(self):
        """Prints a formatted title, ledger list, and a total."""
        return_list = []
        return_list.append(f"{self.category_str:*^30}")
        for each in self.ledger:
            return_list.append(f"{each[DESCR][:23]: <23}{each[AMT]: >7.2f}")
        return_list.append(f"Total:{self.get_balance(): >7.2f}")

        return "\n".join(return_list)


def create_spend_chart(categories):
    """Returns a propperly-formatted stack chart."""
    return ""

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
        self.category_str = category.name  #
        self.ledger = []
        # Constant Variables
        AMT = "amount"
        DESCR = "description"

    def change_sign(number):
        """Returns the changed sign of a number (integer or float).

        E.G. 42 becomes -42."""

        try:
            return number - (number * 2)
        except:
            raise ValueError("Error: not a number.")

    def get_balance():
        """Gets the balance of the category's ledger.

        This is the sum of the amounts in the ledger."""

        return sum([each["amount"] for each in self.ledger])

    def check_funds(amt_f):
        """Checks if there are enough funds to withdraw.

        Returns true if amt_f is grater than the amount in self"""

        if get_balance() > amt_f:
            return False
        else:
            return True

    def post(amt_f, descr_str=""):
        """Appends a transaction to the ledger.

        Args:
            amt_f: The amount of money that is deposited or withdrawn.

            descr_str: A short description of the transaction."""

        dict = {AMT: amt_f, DESCR: descr_str}
        self.ledger.append(dict)

    def deposit(amt_f, descr_str=""):
        """Deposits an amount to the category's ledger.

        Args:
            amt_f: The amount of money to be deposited.
            descr_str: A short description of the transaction."""

        assert amt_f >= 0
        post(amt_f, descr_str)

    def withdraw(amt_f, descr_str=""):
        """Withdraws an amount to the category's ledger.

        Args:
            amt_f: The amount of money to be withdrawn.
            descr_str: A short description of the transaction."""

        assert amt_f >= 0
        if get_balance():
            amt_changed = change_sign(amt_f)
            post(amt_changed, descr_str)

    def transfer(amt_f, category):
        """If there are enough funds in self, the function will withdraw from 'self' and deposit it into the destination category."""

        assert amt_f >= 0
        if get_balance():
            amt_changed = change_sign(amt_f)
            post(amt_changed, descr_str)
            # Note to self: this class method is not finish. Google 'How to access another class object from the current  class object in Python?"

    def __str__():
        """Prints a formatted title, ledger list, and a total."""
        return ""


def create_spend_chart(categories):
    """Returns a propperly-formatted stack chart."""
    return ""

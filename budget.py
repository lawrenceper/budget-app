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
        ledger = []
        # Constant Variables
        AMT = "amount"
        DESCR = "description"

    def check_funds(amt_f):
        """This function will check if there are enough funds to withdraw.

        Returns true if amt_f is grater than the amount in self"""
        return False

    def get_balance():
        """Gets the balance of the category's ledger.

        This is the sum of the amounts in the ledger."""
        return 0

    def post(amt_f, descr_str=""):
        """Appends a transaction to the ledger.

        Args:
            amt_f: The amount of money that is deposited or withdrawn.

            descr_str: A short description of the transaction."""
        dict = {AMT: amt_f, DESCR: descr_str}
        ledger.append(dict)

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
        pass

    def transfer(amt_f, category):
        """If there are enough funds in self, the function will withdraw from 'self' and deposit it into the destination category."""
        pass

    def __str__():
        """Prints a formatted title, ledger list, and a total."""
        return ""


def create_spend_chart(categories):
    """Returns a propperly-formatted stack chart."""
    return ""

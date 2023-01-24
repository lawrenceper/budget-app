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

    def get_balance():
        """Gets the balance of the category's ledger.

        This is the sum of the amounts in the ledger."""

        return sum([each["amount"] for each in ledger])

    def check_funds(amt_f):
        """Checks if there are enough funds to withdraw.

        Returns true if amt_f is grater than the amount in self"""

        if get_balance() > amt_f:
            return True
        else:
            return False

    def post(amt_f, descr_str="", change_sign=False):
        """Appends a transaction to the ledger.

        Args:
            amt_f: The amount of money that is deposited or withdrawn.
            descr_str: A short description of the transaction.
            change_sign: if set to true, then the amount is converted to a negative number."""

        if change_sign:
            dict = {AMT: round(amt_f - (amt_f * 2), 2), DESCR: descr_str}
        else:
            dict = {AMT: round(amt_f, 2), DESCR: descr_str}

        ledger.append(dict)

    def deposit(amt_f, descr_str=""):
        """Deposits an amount to the category's ledger.

        Args:
            amt_f: The amount of money to be deposited.
            descr_str: A short description of the transaction."""

        assert amt_f >= 0
        self.post(amt_f, descr_str)

    def withdraw(amt_f, descr_str=""):
        """Withdraws an amount to the category's ledger.

        Args:
            amt_f: The amount of money to be withdrawn.
            descr_str: A short description of the transaction."""

        assert amt_f >= 0
        if self.get_balance() == False:
            self.post(amt_f, descr_str, True)
            return True

    def transfer(amt_f, category_):
        """If there are enough funds in self, the function will withdraw from 'self' and deposit it into the destination category."""

        assert amt_f >= 0
        if get_balance() == False:
            self.withdraw(amt_f, f"Transfer to {category}")
            category.deposit(amt_f, f"Transfer from {self.category_str")
            return True

    def __str__():
        """Prints a formatted title, ledger list, and a total."""
        return ""


def create_spend_chart(categories):
    """Returns a propperly-formatted stack chart."""
    return ""

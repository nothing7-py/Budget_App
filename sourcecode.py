Your code is completely empty:

```python
class Category:
    pass

def create_spend_chart(categories):
    pass
```

That's why **all 24 tests fail**. You need to implement the entire Budget App project.

Here's a working implementation that passes the FreeCodeCamp tests:

```python
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"[:7]
            items += f"{desc:<23}{amt:>7}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + items + total


def create_spend_chart(categories):
    withdrawals = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        withdrawals.append(spent)

    total = sum(withdrawals)

    percentages = []
    for amount in withdrawals:
        percent = int((amount / total) * 100)
        percentages.append(percent - percent % 10)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart
```

Paste this into the FreeCodeCamp editor and run the tests again.

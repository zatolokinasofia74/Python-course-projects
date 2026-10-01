class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        lines = [self.name.center(30, "*")]
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines.append(f"{desc}{amt}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    spends = [
        sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        for cat in categories
    ]
    total = sum(spends)
    percentages = [int((s / total) * 10) * 10 if total > 0 else 0 for s in spends]

    lines = ["Percentage spent by category"]
    for level in range(100, -1, -10):
        bars = "".join(f" {'o' if p >= level else ' '} " for p in percentages)
        lines.append(f"{level:>3}|{bars} ")

    lines.append("    " + "-" * (len(categories) * 3 + 1))

    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names) if names else 0

    for i in range(max_len):
        row = "".join(f" {name[i] if i < len(name) else ' '} " for name in names)
        lines.append(f"    {row} ")

    return "\n".join(lines)
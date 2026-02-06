def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)


class Account:
    def __init__(self, initial_deposit: float) -> None:
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.portfolio = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({'type': 'withdraw', 'amount': amount, 'balance': self.balance})
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if self.balance >= total_cost:
            self.balance -= total_cost
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
            self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price, 'total': total_cost})
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if self.portfolio.get(symbol, 0) >= quantity:
            price = get_share_price(symbol)
            total_gain = price * quantity
            self.balance += total_gain
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price, 'total': total_gain})
            return True
        return False

    def get_portfolio_value(self) -> float:
        return sum(quantity * get_share_price(symbol) for symbol, quantity in self.portfolio.items())

    def get_holdings(self) -> dict:
        return self.portfolio.copy()

    def get_profit_loss(self) -> float:
        current_value = self.balance + self.get_portfolio_value()
        return current_value - self.initial_deposit

    def get_transactions(self) -> list:
        return self.transactions

# Test cases
account = Account(10000)
account.deposit(500)
account.withdraw(300)
account.buy_shares('AAPL', 10)
account.sell_shares('AAPL', 5)

print('Final Balance:', account.balance)
print('Portfolio Value:', account.get_portfolio_value())
print('Holdings:', account.get_holdings())
print('Profit/Loss:', account.get_profit_loss())
print('Transactions:', account.get_transactions())
import unittest
from accounts import Account, get_share_price

class TestAccounts(unittest.TestCase):
    
    def test_get_share_price(self):
        self.assertEqual(get_share_price('AAPL'), 150.0)
        self.assertEqual(get_share_price('TSLA'), 700.0)
        self.assertEqual(get_share_price('GOOGL'), 2800.0)
        self.assertEqual(get_share_price('MSFT'), 0.0)  # Default case for unknown symbol

    def test_initial_deposit(self):
        account = Account(10000)
        self.assertEqual(account.balance, 10000)
    
    def test_deposit(self):
        account = Account(10000)
        account.deposit(500)
        self.assertEqual(account.balance, 10500)
    
    def test_withdraw(self):
        account = Account(10000)
        result = account.withdraw(300)
        self.assertTrue(result)
        self.assertEqual(account.balance, 9700)
        
        # Test insufficient funds
        result = account.withdraw(10000)
        self.assertFalse(result)
        self.assertEqual(account.balance, 9700)

    def test_buy_shares(self):
        account = Account(10000)
        result = account.buy_shares('AAPL', 10)
        self.assertTrue(result)
        self.assertEqual(account.balance, 8500)
        self.assertEqual(account.get_holdings(), {'AAPL': 10})
        
        # Test insufficient funds
        result = account.buy_shares('AAPL', 100)  # Cost would be 15000
        self.assertFalse(result)
        self.assertEqual(account.balance, 8500)

    def test_sell_shares(self):
        account = Account(10000)
        account.buy_shares('AAPL', 10)
        result = account.sell_shares('AAPL', 5)
        self.assertTrue(result)
        self.assertEqual(account.balance, 9250)
        self.assertEqual(account.get_holdings(), {'AAPL': 5})
        
        # Test selling more shares than owned
        result = account.sell_shares('AAPL', 10)
        self.assertFalse(result)
        self.assertEqual(account.balance, 9250)

    def test_get_portfolio_value(self):
        account = Account(10000)
        account.buy_shares('AAPL', 10)
        self.assertEqual(account.get_portfolio_value(), 1500)
    
    def test_get_profit_loss(self):
        account = Account(10000)
        account.buy_shares('AAPL', 10)
        account.sell_shares('AAPL', 5)
        self.assertEqual(account.get_profit_loss(), -750)  # Initial deposit is 10000, spends 1500 buys, earns 750 on sales
        
    def test_get_transactions(self):
        account = Account(10000)
        account.buy_shares('AAPL', 10)
        account.sell_shares('AAPL', 5)
        transactions = account.get_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]['type'], 'buy')
        self.assertEqual(transactions[1]['type'], 'sell')

if __name__ == '__main__':
    unittest.main()
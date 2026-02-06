import gradio as gr
from accounts import Account, get_share_price

account = Account(initial_deposit=10000)

def create_account(initial_deposit):
    global account
    account = Account(initial_deposit=initial_deposit)
    return f"Account created with initial deposit: ${initial_deposit}"

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited: ${amount}, Current Balance: ${account.balance}"

def withdraw_funds(amount):
    success = account.withdraw(amount)
    if success:
        return f"Withdrew: ${amount}, Current Balance: ${account.balance}"
    else:
        return f"Insufficient balance to withdraw: ${amount}"

def buy_shares(symbol, quantity):
    success = account.buy_shares(symbol, quantity)
    if success:
        return f"Bought {quantity} shares of {symbol}, New Balance: ${account.balance}"
    else:
        return f"Unable to buy {quantity} shares of {symbol}, Insufficient funds."

def sell_shares(symbol, quantity):
    success = account.sell_shares(symbol, quantity)
    if success:
        return f"Sold {quantity} shares of {symbol}, New Balance: ${account.balance}"
    else:
        return f"Unable to sell {quantity} shares of {symbol}, Insufficient holdings."

def get_portfolio_value():
    return f"Total Portfolio Value: ${account.get_portfolio_value()}"

def get_holdings():
    holdings = account.get_holdings()
    return f"Holdings: {holdings}"

def get_profit_loss():
    return f"Profit/Loss: ${account.get_profit_loss()}"

def get_transactions():
    transactions = account.get_transactions()
    return f"Transactions: {transactions}"

with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation Platform")

    with gr.Tab("Account Management"):
        initial_deposit = gr.Number(label="Initial Deposit", value=10000)
        create_account_button = gr.Button("Create Account")
        create_account_button.click(create_account, inputs=initial_deposit, outputs="")

        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit Funds")
        deposit_button.click(deposit_funds, inputs=deposit_amount, outputs="")

        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw Funds")
        withdraw_button.click(withdraw_funds, inputs=withdraw_amount, outputs="")

    with gr.Tab("Stock Operations"):
        symbol = gr.Dropdown(choices=['AAPL', 'TSLA', 'GOOGL'], label="Stock Symbol")
        buy_quantity = gr.Number(label="Buy Quantity")
        buy_button = gr.Button("Buy Shares")
        buy_button.click(buy_shares, inputs=[symbol, buy_quantity], outputs="")

        sell_quantity = gr.Number(label="Sell Quantity")
        sell_button = gr.Button("Sell Shares")
        sell_button.click(sell_shares, inputs=[symbol, sell_quantity], outputs="")

    with gr.Tab("Reports"):
        portfolio_value_button = gr.Button("Get Portfolio Value")
        portfolio_value_button.click(get_portfolio_value, inputs=None, outputs=gr.Textbox())

        holdings_button = gr.Button("Get Holdings")
        holdings_button.click(get_holdings, inputs=None, outputs=gr.Textbox())

        profit_loss_button = gr.Button("Get Profit/Loss")
        profit_loss_button.click(get_profit_loss, inputs=None, outputs=gr.Textbox())

        transactions_button = gr.Button("Get Transactions")
        transactions_button.click(get_transactions, inputs=None, outputs=gr.Textbox())

demo.launch()
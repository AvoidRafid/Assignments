class Account:
    def __init__(self, name, iban, balance, max_daily_turnover=1500):
        self.name = name
        self.iban = iban
        self.max_daily_turnover = max_daily_turnover
        self.balance = balance
        self.daily_turnover = 0

    def add_money(self, amount):
        if amount < 0 or self.daily_turnover + amount > self.max_daily_turnover:
            return False
        else:
            self.balance += amount
            self.daily_turnover += amount
            return True

    def get_money(self, amount):
        if amount < 0 or self.daily_turnover + amount > self.max_daily_turnover or self.balance < amount:
            return False
        else:
            self.balance -= amount
            self.daily_turnover += amount
            return True

    def transfer_money(self, amount, receiver):
        if amount < 0 or self.daily_turnover + amount > self.max_daily_turnover or\
                receiver.daily_turnover + amount > receiver.max_daily_turnover or self.balance < amount:
            return False
        else:
            self.balance -= amount
            self.daily_turnover += amount
            receiver.daily_turnover += amount
            receiver.balance += amount
            return True

    def show_account(self):

        print('Name : ', self.name)
        print('Account Balance: ', self.balance)
        print('Daily Turnover: ', self.daily_turnover, '\n')


a_pip = Account('Pip', 555342, 2000)
a_Leia = Account('Leia', 555442, 2500)

a_pip.show_account()
a_Leia.show_account()

a_pip.transfer_money(400, a_Leia)
a_pip.add_money(700)

a_pip.show_account()
a_Leia.show_account()

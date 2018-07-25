class BankAccount:
    def __init__(self, balance):
        self.balance = current_balance

    def deposit(self, added_to_balance):
        print("The previous balance of {}, with the deposit, brings the new balance to {}.".format(self.balance, added_to_balance))

    def withdraw(self, withdrawn_amount):
        print("The amount I withdrew was {}.")

    def accumulate_interest(self, )
  pass

class ChildrensAccount(BankAccount):
  pass

class OverdraftAccount:
  pass









basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))

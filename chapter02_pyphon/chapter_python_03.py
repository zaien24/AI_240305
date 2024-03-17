person_a_numbers = [ 70, 85, 90, 60]
person_b_numbers = [ 30, 75, 30, 90]
person_c_numbers = [ 70, 85, 90, 60]

def calc_avg(numbers):
    avg = sum(numbers) / len(numbers)
    print(f"avg: {avg}")
    return avg

person_numbers_list = [person_a_numbers, person_b_numbers, person_c_numbers]

for numbers in person_numbers_list:
    calc_avg(numbers)
    
    
class BankAccount:
    def __inint__(self, account_number, balance=0):    
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        pass
    
    def withdraw(self, amount):
        pass
    
account = BankAccount("123-456-789", 10000)    

account.deposit(5000)
account.withdraw(12000)
account.withdraw(5000)




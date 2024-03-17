
class User:
    def __init__(self, username, rank):
        self.username = username
        self.rank = rank
        
    def print_info(self):
        print(f"username: {self.username}, rank: {self.rank}")
        
        
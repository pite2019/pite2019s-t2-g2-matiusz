



class Bank:
    def __init__(self, name):
        self.BankName = name
        self.ClientList = []
    def add_client(self, Name):
        client = Client(Name)
        self.ClientList.append(client)
        return client
    def remove_client(self, Client):
        self.ClientList.remove(Client)


class Client:
    def __init__(self, Name):
        self.Name = Name
        self.Money = 0
        self.Log = []
        self.MaxCredit = 0
    def money_input(self, Amount):
        self.Money = self.Money + Amount
        self.Log.append({"input", Amount})
    def money_withdrawal(self, Amount):
        if self.Money+self.MaxCredit<Amount:
            self.Log.append({"withdrawal attempt, not enough money", Amount})
            return 0
        else:
            self.Log.append({"withdrawal", Amount})
            self.Money =  self.Money-Amount
            return Amount
    def transaction(self, Client, Amount):
        if self.Money+self.MaxCredit<Amount:
            self.Log.append({"transaction failed, not enough money", Amount})
            return 0
        else:
            self.Money = self.Money - Amount
            Client.Money = Client.Money + Amount
            self.Log.append({"transaction from " + self.Name + " to " + Client.Name, Amount})
            Client.Log.append({"transaction from " + self.Name + " to " + Client.Name, Amount})
            return Amount
    def __str__(self):
        return self.Name +" " + str(self.Money) + " " + str(self.Log)

def Main():
    return 0

if __name__ == "__main__" :
    Main()
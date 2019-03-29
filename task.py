

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
    def money_input(self, Amount):
        self.Money = self.Money + Amount
        self.Log.append({"input", Amount})
    def money_withdrawal(self, Amount):
        if self.Money<Amount:
            self.Log.append({"withdrawal attempt, not enough money", Amount})
            return 0
        else:
            self.Log.append({"withdrawal", Amount})
            self.Money =  self.Money-Amount
            return Amount
    def transaction(self, Client, Amount):
        if self.Money<Amount:
            self.Log.append({"transaction failed, not enough money", Amount})
            return 0
        else:
            self.Money = self.Money - Amount
            Client.Money = Client.Money + Amount
            self.Log.append({"transaction from " + self.Name + " to " + Client.Name, Amount})
            self.Log.append({"transaction from " + self.Name + " to " + Client.Name, Amount})
            return Amount

def Main():
    bank1 = Bank("Polski")
    client1 = bank1.add_client("kowalski")
    client2 = bank1.add_client("nowak")
    client1.money_input(100)
    client1.money_withdrawal(50)
    client1.money_withdrawal(100)
    client2.money_input(200)
    client2.transaction(client1, 150)
    print(client1.Log)
    print(client2.Log)

Main()


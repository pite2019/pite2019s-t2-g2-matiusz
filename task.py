
import unittest

class TestBank(unittest.TestCase):
    def test_add_client(self):
        bank = Bank("testbank")
        bank.add_client("testclient")
        self.assertEqual(bank.ClientList[0].Name, "testclient")
    def test_remove_client(self):
        bank = Bank("testbank")
        client = bank.add_client("testclient")
        bank.remove_client(client)
        self.assertEqual(bank.ClientList, [])

class TestClient(unittest.TestCase):
    def test_money_input(self):
        client = Client("testclient")
        client.Money=100
        client.money_input(42)
        self.assertEqual(client.Money, 142)
    def test_money_withdrawal(self):
        client = Client("testclient")
        client.Money=100
        client.money_withdrawal(42)
        self.assertEqual(client.Money, 58)
    def test_failed_withdrawal(self):
        client = Client("testclient")
        client.Money=100
        self.assertEqual(client.money_withdrawal(142), 0)
        self.assertEqual(client.Money, 100)
    def test_transaction(self):
        client1 = Client("testclient1")
        client2 = Client("testclient2")
        client1.Money=100
        client2.Money=50
        client1.transaction(client2, 60)
        self.assertEqual(client1.Money, 40)
        self.assertEqual(client2.Money, 110)
    def test_failed_transaction(self):
        client1 = Client("testclient1")
        client2 = Client("testclient2")
        client1.Money=50
        client2.Money=50
        self.assertEqual(client1.transaction(client2, 60), 0)




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

if __name__ == "__main__" :
    unittest.main()
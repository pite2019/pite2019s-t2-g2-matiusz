import unittest
import task

class TestBank(unittest.TestCase):
    def test_add_client(self):
        bank = task.Bank("testbank")
        bank.add_client("testclient")
        self.assertEqual(bank.ClientList[0].Name, "testclient")
    def test_remove_client(self):
        bank = task.Bank("testbank")
        client = bank.add_client("testclient")
        bank.remove_client(client)
        self.assertEqual(bank.ClientList, [])

class TestClient(unittest.TestCase):
    def test_money_input(self):
        client = task.Client("testclient")
        client.Money=100
        client.money_input(42)
        self.assertEqual(client.Money, 142)
    def test_money_withdrawal(self):
        client = task.Client("testclient")
        client.Money=100
        client.money_withdrawal(42)
        self.assertEqual(client.Money, 58)
    def test_failed_withdrawal(self):
        client = task.Client("testclient")
        client.Money=100
        self.assertEqual(client.money_withdrawal(142), 0)
        self.assertEqual(client.Money, 100)
    def test_transaction(self):
        client1 = task.Client("testclient1")
        client2 = task.Client("testclient2")
        client1.Money=100
        client2.Money=50
        client1.transaction(client2, 60)
        self.assertEqual(client1.Money, 40)
        self.assertEqual(client2.Money, 110)
    def test_failed_transaction(self):
        client1 = task.Client("testclient1")
        client2 = task.Client("testclient2")
        client1.Money=50
        client2.Money=50
        self.assertEqual(client1.transaction(client2, 60), 0)



if __name__ == "__main__" :
    unittest.main()
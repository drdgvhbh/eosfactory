# python3 ./tests/test1.py

import json
import setup
import cleos
import teos
import entities

import unittest

class Test1(unittest.TestCase):

    def run(self, result=None):
        """ Stop after first error """      
        if not result.failures:
            super().run(result)
        print("-------------------------------------------\n")

    @classmethod
    def setUpClass(cls):
        setup.set_verbose(False)
        cleos.dont_keosd()

    def setUp(self):
        pass

    def test_05(self):
        node_reset = teos.node_reset()
        self.assertTrue(node_reset, "node_reset")

    def test_08(self):
        wallet_default = entities.Wallet()
        wallet_second = entities.Wallet("second")
        self.assertTrue(not wallet_default.error, "Wallet default")
        key_owner = cleos.CreateKey("owner")
        self.assertTrue(wallet_default.import_key(key_owner), "import_key")
        print(wallet_default)
        self.assertTrue(wallet_default.open(), "open")
        self.assertTrue(wallet_default.lock(), "lock")
        print(wallet_default)
        self.assertTrue(wallet_default.unlock(), "unlock")

    def test_12(self):
        account_eosio = cleos.AccountEosio()
        key_owner = cleos.CreateKey("owner")
        account_tokenika = entities.Account(
            account_eosio, "tokenika", key_owner, key_owner)
        self.assertTrue(not account_tokenika.error, "account_tokenika")

        code = account_tokenika.code()
        self.assertTrue(not code.error, "account_tokenika")
        print(account_tokenika.code)
        
        print(account_tokenika)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
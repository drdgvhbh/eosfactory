"""
# Account name conflict
## Cases
```
The structure of the `Cases` files is explained in the file `setup.md` in
this file's directory.

Note, that all case files are both ``Markdown`` and ``Python` scripts. 
Therefore, you can execute them with `python3 <file name>` bash command, or 
you can view them, (RIGHT MOUSE -> Open Preview if you use the ``Visual Studio 
Code``).
```

## Set-up
```
"""
import setup
import eosf
from eosf_wallet import Wallet
from eosf_account import account_create, account_master_create

eosf.restart()
eosf.set_throw_error(True)
eosf.reset([eosf.Verbosity.TRACE]) 
wallet = Wallet()
account_master_create("account_master")
eosf.set_throw_error(False)
"""
```
## Case
```
The ``EOSFactory`` wraps EOSIO accounts with objects. The symbolic name of an 
account object, for example ``account_alice`` has to be unique in a program. 
Moreover, it has be unique in a collection of scripts, especially if they 
execute real transactions.

The ``EOSFactory`` uses a mapping files that keep the uniqueness.

However, what if a user wants to ascribe a previously used name to another 
physical account. Then, the only way to keep the previous physical account 
within the system is to change its mapping name.

Create two account objects: ``account_alice`` and ``account_carrol``.

Then try to create another account object called ``account_alice``. Although
this object is going to refer to a new blockchain account, it cannot accept
the given name: error is issued.

You are prompted to change the blocking name. On acceptance, the ``nano`` 
editor opens. CTR+X, to save and exit.

Change ``account_alice`` to ``account_alice_b``.
```

```
"""
account_create("account_alice", account_master)
account_create("account_carrol", account_master)
account_create("account_alice", account_master)
"""
```
"""
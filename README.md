# MeowMeow ATM

_project url_ https://github.com/precidiatom/2515_ATM/


This is a python project that models a banking system, with the GUI developed using Tkinter 
and the persistance data created using shelve.


The interface includes:
* A GUI that simulates a bank machine, allowing a user to view their account info, withdraw and deposit
  from their accounts.
* A Bank Management CLI that allows a teller to add and delete users and accounts0, 
  as well as run reports.
* Transaction logging
* Login and user authentication


## Authors
* **Emilie Zhang**
* **Precidia Tom**

## Installation
* Run the atm.exe to start the customer banking GUI.
* Run the bank_mgmt.exe to start the teller admin CLI.


The atm.exe starts with an admin account, with account ID _a0101_ and PIN _1234_


The bank_mgmt.exe starts with a default customer account, with account ID _b9090_ and PIN _1234_.


Log in with the corresponding credentials to start exploring the CLI and the GUI. All persisted user data could be found in the **data** folder, with user ID's as the file names.

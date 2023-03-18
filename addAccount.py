import json

fileHandler = open('accounts.txt', 'r')
accountsHandler = open('accountsJson.txt', 'r')

accounts = fileHandler.read().split()
passwords = json.loads(accountsHandler.read())

inputaccountlist = []
passwordlist = []

for i in range(len(inputaccountlist)):

    accounts.append(inputaccountlist[i])
    passwords[inputaccountlist[i]] = passwordlist[i]

saveFile = " ".join(accounts)
SaveFilePass = json.dumps(passwords)

fileHandler = open('accounts.txt', 'w')
accountsHandler = open('accountsJson.txt', 'w')

fileHandler.write(saveFile)
accountsHandler.write(SaveFilePass)
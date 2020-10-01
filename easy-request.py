from venmo_api import Client
from datetime import datetime, timedelta
import config

# Get your access token. You will need to complete the 2FA process
#access_token = Client.get_access_token(username='config.username', password='config.password')

#print(access_token)

class ValidTransactions:
    transactions = []
    sum = 0

venmo = Client(access_token=config.apiKey)

"""
users = venmo.user.search_for_users(query="Clinton Hausman",
                                    page=1)
for user in users:
  print(user)
"""

user = venmo.user.get_my_profile()

def getTransactions(transactions_list):
    sum = 0
    t = ValidTransactions()

    transactionsList = []
    for transaction in transactions_list:
        #print(transaction)
        if(transaction.target.id == user.id and transaction.payment_type == 'pay'):

            d = datetime.fromtimestamp(int(transaction.date_completed)) - timedelta(hours = 4)
            #print(d.strftime('%Y-%m-%d %I:%M:%S')
            
            if d > datetime.now()-timedelta(hours=48):
                sum += transaction.amount
                print(transaction.actor.first_name + ' -> ' + str(transaction.amount) + ' -> ' + transaction.target.first_name + ' ' + d.strftime('%Y-%m-%d %I:%M:%S'))
                t.transactions.append(transaction)

    t.sum = sum
    return t
    

# callback is optional. Max number of transactions per request is 50.
transactions = venmo.user.get_user_transactions(user_id=user.id, count=50)

validTransactions = getTransactions(transactions)

print(validTransactions.sum)

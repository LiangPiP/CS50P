amount_due=50
while True :
    print("Amount Due:",amount_due)
    coin=int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due -= coin
    if amount_due <= 0:
        print("Change Owed:",abs(amount_due))
        break
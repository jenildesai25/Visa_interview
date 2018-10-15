# VISA full time master's ph.D question.
# money = 50, items_per_bundles = 20, bundel_cost = 12
def find_bundles(money, items_per_bundles, bundel_cost):
    total_money_spent = 0
    total_bundel = 0
    if money == 0:
        return 0
    while total_money_spent <= money and money - total_money_spent >= bundel_cost:
        total_bundel += items_per_bundles
        total_money_spent += bundel_cost
    total_money_left = money - total_money_spent

    print('total bundels are', total_bundel)
    print('money left', total_money_left)


money = 50
items_per_bundles = 20
bundel_cost = 12
find_bundles(money, items_per_bundles, bundel_cost)

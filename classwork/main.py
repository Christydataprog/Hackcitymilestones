# accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
# accounts = [[1, 2, 3], [3, 2, 1]]
accounts = [[1, 5], [7, 3], [3, 5]]
# class Richest:
#     def highestWealth(self, accounts: List[List[int]]) -> int:
#         accounts = [sum(acc)] for acc in accounts]
#         return max(accounts)
def highestwealth(accounts):
    wealth = 0
    for acc in accounts:
        customer = 0
        for bank in acc:
            customer += bank
        if customer > wealth:
            wealth = customer
    return wealth
print(highestwealth(accounts))



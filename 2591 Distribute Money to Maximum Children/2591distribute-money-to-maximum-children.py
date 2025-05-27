class Solution:
    def distMoney(self, money: int, children: int) -> int:

        if children > money:
            return -1

        money -= children

        rem = money % 7
        money //= 7

        '''
        if money > children: 
            10
        '''

        print(money, rem)
        
        if money > children:
            money = children - 1
        elif (children - money == 0 and rem > 0) or (children - money == 1 and rem == 3):
            money -= 1
        
        return money



        
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        run = True
        
        while run:
            newFull = empty // numExchange    
            if newFull == 0:
                run = False                   
            else:
                total += newFull               
                empty = newFull + (empty % numExchange)  

        return total

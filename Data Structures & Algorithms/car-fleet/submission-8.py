class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        #zip position and speed together so we can sort them together
        cars = list(zip(position, speed))

        #sort by position, cars always bottlenecked by position
        #if a fast car is behind a slow car, it can only go as fast as the slow car
        cars.sort(key = lambda x: x[0], reverse=True)
        

        #think of a way to map position to speed. index in original array?
        for i in range(len(cars)):

        #calculate time to target, divide position to target by speed
            time_to_target = (target - cars[i][0])/cars[i][1]
        
        #cars with less or the same time to target will join together in a fleet
        #therefore, you can pop a car off the stack if they are part of the same fleet, and only focus on the current car in that fleet with the lowest position
        #otherwise if the current car has a greater time to target, it can be added to the stack normally and a new fleet will be started
            if(len(stack) > 0):
                popped = False
                while (len(stack) > 0 and time_to_target <= stack[-1][1]):
                    temp_target_time = stack.pop()
            #update time to target as oldest value in the stack, because now
            #the time is bottlenecked to however slow the car ahead was going
                    time_to_target = temp_target_time[1]

            #push the current car onto the stack, and other cars behind it will compare to it as the new bottleneck
                
          
            stack.append((cars[i][0], time_to_target))
           
            

        #the amount of cars in the stack represent the fleets, since each car in the stack is the lowest car in their respective fleet
        return len(stack)
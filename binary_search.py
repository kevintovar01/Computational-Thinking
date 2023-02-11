


def binary_search(objective):
    epsilon = 0.01 #14

    low = 0.0
    high = max(1.0, objective)
    
    result = (low+high)/2
    #the objective is for the square root difference between the result and the objective to be less than epsilon

    #as long as the difference between result and objective to be less than epsilon, this will iterate
    while abs(result**2-objective) >= epsilon:

        #I print the process in the iteration
        print(f'result**2:{abs(result**2-objective)} low:{low} high:{high} result:{result}')
        

        #I verify if the square root result is less of the objective
        if result**2 < objective:
            #if so, increase the value from low to result
            low = result
        else:
            #if not so, increase the value from high to result 
            high = result
        
        #I update the result as the new amplitud mean
        result = (low+high)/2

    return result

def run():
    objective = 2
    result = binary_search(objective)
    print(f'the square root of {objective} is: {result}')


if __name__ == '__main__':
    run()
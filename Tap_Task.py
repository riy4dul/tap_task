def calculate_total_earnings(X, Y, Z, N, time_ranges):
    total_earnings = 0
    
   
    for i in range(N):
        start_time, end_time = time_ranges[i]
        
        # Loop through each hour in the day
        for hour in range(start_time, end_time):
            
            if 0 <= hour < 9 or 22 <= hour < 24:
                total_earnings += Z  
            elif 9 <= hour < 17:
                total_earnings += X  
            else:
                total_earnings += Y  
    
    return total_earnings


if __name__ == "__main__":
    # Input values
    inputs = list(map(int, input().split()))  
    X, Y, Z = inputs[0], inputs[1], inputs[2]  
    N = inputs[3]  
    
    time_ranges = []
    index = 4
    for i in range(N):
        start_time = inputs[index]
        end_time = inputs[index + 1]
        time_ranges.append((start_time, end_time))
        index += 2
    
   
    result = calculate_total_earnings(X, Y, Z, N, time_ranges)
    

    print(result)

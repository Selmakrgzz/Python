def sum_of_values(list, odd_even_all):
    sum=0
    output="Output: the sum is: "
    if odd_even_all == 'odd':
        for i in list:
            if i % 2 != 0:
                sum+=i
                output=f"{sum}"
    
    if odd_even_all == 'even':
        for i in list:
            if i % 2 == 0:
                sum+=i
                output=f"{sum}"

    if odd_even_all == 'all':
        for i in list:
            sum+=i
            output=f"{sum}"
    
    print(output)
          

list = [1,2,3,4,5,100]
sum_of_values(list,'even')

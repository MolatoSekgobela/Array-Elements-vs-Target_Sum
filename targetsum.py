
# function that receives an array, target sum

def find_sum_of_two(arry,target_value):
    
    for  a in range (len(arry)):
        for j in range(a+1,len(arry)):
            if (arry[a] + arry[j]) == target_value:
                print("(",arry[a],",",arry[j],")",sep = " ")

arry = [1, 3, 2, 2]
target_value  = 3

print(find_sum_of_two(arry, target_value))
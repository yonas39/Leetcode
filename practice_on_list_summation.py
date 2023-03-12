"""
  Here I am writing a function that sum two lists 
  if the sum of the two digits is 10 or over, then the value beyond 10 will carry over to the 
  next digits. the return will be a new list with the sum of each digits of the two given lists
"""

def summation(l1, l2):
    # output= [0] * (max(len(l1), len(l2))+1)
    output=[0] *max(len(l1), len(l2))

    carryover=0

    for i in range(len(output)):

        if i < len(l1):
            digit1 = l1[i]
            # print(digit1)
        else:
            digit1 = 0

        if i < len(l2):
            digit2 = l2[i]
            # print(digit2)
        else:
            digit2 =0

        summ_digit = digit1 + digit2 + carryover
        # print(summ_digit)
        carryover = summ_digit // 10
        # print(carryover)
        # output.append(summ_digit % 10)
        output[i]= summ_digit % 10
    
    if carryover > 0:
        output.append(carryover)
    
    return output

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
l1 = [2,4,3]
l2 = [5,6,4]

print(summation(l1,l2))




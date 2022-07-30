list_stock = [1,4,2]
print(list_stock)
left, right, min_stock, max_stock = 0, len(list_stock)-1, 2147483647, 0
        
while left < right:
    print(list_stock[left])
    print(list_stock[right])
    if list_stock[left] < min_stock :
        min_stock = list_stock[left]
    if list_stock[right] > max_stock :
        max_stock = list_stock[right]
    if list_stock[left + 1] != list_stock[right - 1] :
        left += 1
        right -= 1
    else :
        if list_stock[left + 1] - list_stock[left] > list_stock[right - 1] - list_stock[right] :
            right -= 1
        else :
            left += 1

if max_stock - min_stock > 0 :
    print (max_stock - min_stock)
else :
    print (0)
l, k = map(int, input().split())

counter = 0 
if l<k:
    print(0)
else:
    while l/k>1:
        l /= k
        counter += 1
    print(counter)
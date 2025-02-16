def stock(prices):
    stack=[]
    span=[0]*len(prices)
    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span[i]=i+1
        else:
            span[i]=i-stack[-1]

        stack.append(i)
    return span

prices = [100, 80, 60, 70, 60, 75, 85]

print(stock(prices))



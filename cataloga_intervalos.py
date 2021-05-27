num = 1
intervalo0_25 = 0
intervalo26_50 = 0
intervalo51_75 = 0
intervalo76_100 = 0
while num >= 0:
    num = float(input('Entre com um numero positivo: '))
    if num >= 0 and num <= 25:
        intervalo0_25 += 1
    elif num >= 26 and num <= 50:
        intervalo26_50 += 1
    elif num >= 51 and num <= 75:
        intervalo51_75 += 1
    elif num >= 76 and num <= 100:
        intervalo76_100 += 1
print('[0,25] = {} elementos'.format(intervalo0_25))
print('[26,50] = {} elememtos'.format(intervalo26_50))
print('[51,75] = {} elementos'.format(intervalo51_75))
print('[76,100] = {} elementos'.format(intervalo76_100))

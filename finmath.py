import math

roundNum = 6 #6位小数精度

def assetpv(n, i, head): # 年金现值
    i = i / 100.0 # 利率
    v = 1 / (1 + i) # 贴现因子
    d = i / (1 + i) # 贴现率
    result = 0.0
    if head is True: # 期初年金
        result = (1 - math.pow(v, n)) / d
        pass
    else:
        result = (1 - math.pow(v, n)) / i
        pass

    return round(result, roundNum)
    pass

def assetpvinfinit(i, head): # 永久年金现值
    i = i / 100.0
    d = i / (1 + i)
    result = 0.0

    if head is True:
        result = 1 / d
        pass
    else:
        result = 1 / i
        pass

    return round(result, roundNum)
    pass

def assetfv(n, i, head): # 年金终值
    i = i / 100.0
    v = 1 / (1 + i)
    d = i / (1 + i)
    result = 0.0
    if head is True:
        result = (math.pow(1+i, n) - 1) / d
    else:
        result = (math.pow(1+i, n) - 1) / i
    return round(result, roundNum)
    pass


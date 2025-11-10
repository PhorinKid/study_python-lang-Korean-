def yun6(a) :
    year6 = int(a)
    return '윤년이다.' if (year6%4==0 and year6%100!=0) or year6%400==0 else '윤년이 아니다.'

def god7(a) :
    god = ('신','유','술','해','자','축','인','묘','진','사','오','미')
    return god[a%12]

def coin8(a, b) :
    d = [500, 100, 50, 10]
    m = b - a
    s = []

    for n in d :
        s.append(m//n)
        m %= n
    return f'{d[0]:3}원 : {s[0]:2}개\n{d[1]:3}원 : {s[1]:2}개\n{d[2]:3}원 : {s[2]:2}개\n{d[3]:3}원 : {s[3]:2}개'
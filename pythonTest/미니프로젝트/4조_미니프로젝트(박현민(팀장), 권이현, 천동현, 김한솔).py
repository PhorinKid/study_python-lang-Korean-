from menu import menu, mart

a = mart()

while 1 :
    mn = menu()

    match mn:
        case 1:
            a.martIn()
        case 2:
            a.martOut()
        case 3:
            a.search()
        case 4:
            a.modi()
        case 5:
            a.save()
        case 6:
            a.stats()
        case 7:
            print('종료합니다.')
            break
        case _ :
            print('1 ~ 7 사이의 값을 입력하시오.')

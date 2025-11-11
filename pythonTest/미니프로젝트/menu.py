from datetime import datetime
import csv
import math

def menu():
    print('-----메뉴-----')
    print('1. 입력\n2. 출력\n3. 검색\n4. 수정\n5. 저장\n6. 통계 \n7. 종료')
    
    try:
        mn = input('번호를 입력하세요 : ')
        mn = int(mn)
        return mn
    except Exception as err:
        return menu()

class mart:
    Product = []
    분류 = ('식료품', '생필품', '장난감', '문구류')

    def __init__(self):
        self.분류 = 0
        self.제품명 = 0
        self.가격 = 0
        self.재고 = 0
    
    def martIn(self):
        try:
            self.분류 = input('분류 : ')
            self.제품명 = input('제품명 : ')
            self.가격 = int(input('가격 : '))
            self.재고 = int(input('재고 : '))
            now = datetime.now()
            formatted = now.strftime("%Y-%m-%d %H:%M:%S")

            if self.분류 in mart.분류:
                mart.Product.append((self.분류, self.제품명, self.가격, self.재고, formatted))
            else:
                print('분류 - 식료품, 생필품, 장난감, 문구류')
                return mart.martIn()

        except Exception as err:
            print(err)


        계속 = input('계속 입력 하시겠습니까?(y/n) : ')
        if 계속 == 'y':
            return mart.martIn(self)
        
    def martOut(self):
            
        if mart.Product != []:
            print('---------------------------------------------------------------')
            print('  분류    제품명     가격        재고        수정날짜')
            print('---------------------------------------------------------------')
            for n in range(0,len(mart.Product)):
                print(f' {mart.Product[n][0]:<7} {mart.Product[n][1]:<10} {mart.Product[n][2]:<10} {mart.Product[n][3]:<10} {mart.Product[n][4]:<}')
            print('---------------------------------------------------------------')
        else:
            print('데이터가 없습니다.')
    
    def search(self):
        제품명 = input('제품명 : ')
        a=[]
    
        for n in range(0,len(mart.Product)):
            if mart.Product[n][1] == 제품명:
                a.append(n)

        if a != []:
            print('---------------------------------------------------------------')
            print('  분류    제품명     가격        재고        수정날짜')
            print('---------------------------------------------------------------')
            for n in a:
                if mart.Product[n][1] == 제품명:
                    print(f' {mart.Product[n][0]:<7} {mart.Product[n][1]:<10} {mart.Product[n][2]:<10} {mart.Product[n][3]:<10} {mart.Product[n][4]}')
            print('---------------------------------------------------------------')
        else:
            print('제품이 없습니다.')

    def modi(self):
        if mart.Product != []:
            분류 = input('분류 : ')
            제품명 = input('제품명 : ')
            가격 = int(input('가격 : '))
            재고 = int(input('재고 : '))
            now = datetime.now()
            formatted = now.strftime("%Y-%m-%d %H:%M:%S")

            if 분류 in mart.분류:
                for n in range(0,len(mart.Product)):
                    if mart.Product[n][1] == 제품명 and mart.Product[n][0] == 분류:
                        mart.Product[n] = (분류 , 제품명, 가격, 재고, formatted)
            else:
                print('분류 - 식료품, 생필품, 장난감, 문구류')
                return mart.modi(self)
        else:
            print('데이터가 없습니다.')
    
    def save(self):
        with open('mart.csv', 'w', newline='', encoding='utf-8') as mart1:
            wr = csv.writer(mart1)
            wr.writerow(['분류','제품명','가격','재고','수정날짜'])
            for n in range(0,len(mart.Product)):
                wr.writerow(mart.Product[n])

    def stats(self):

        if mart.Product != []:
            for i in range(0,len(mart.분류)):
                price = []
                수량 = []
                for n in range(0,len(mart.Product)):
                    if mart.Product[n][0] == mart.분류[i] :
                        price.append(mart.Product[n][2])
                        수량.append(mart.Product[n][3])

                if price != []:
                    print('--------------------------------')
                    print(f'{mart.분류[i]}의 최고가 : {max(price)}')
                    print('--------------------------------')
                    
                if 수량 != []:
                    print('--------------------------------')
                    print(f'{mart.분류[i]}의 최다수량 : {max(수량)}')
                    print('--------------------------------')

            # for i in range(0,len(mart.분류)):
            #     수량 = []
            #     for n in range(0,len(mart.Product)):
            #         if mart.Product[n][0] == mart.분류[i] :
            #             수량.append(mart.Product[n][3])
            #     if 수량 != []:
            #         print('--------------------------------')
            #         print(f'{mart.분류[i]}의 최다수량 : {max(수량)}')
            #         print('--------------------------------')
        else:
            print('데이터가 없습니다.')

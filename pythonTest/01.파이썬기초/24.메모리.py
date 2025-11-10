g = 10 # data segment 의 global(static) 영역에 데이터 할당

# 함수는 text 영역에 할당
def fn1(): # 함수 명은 global 영역에 할당 (주소로 저장 / 1000 번지)
    a = 10
    b = 20

def fn2(): # global 영역에 할당 (주소로 저장 / 2000 번지)
    c = 30
    d = 40
    fn1() # stack 영역에 fn1 함수의 복귀 번지로 저장(2010 번지)

def main(): # global 영역에 할당 (주소로 저장 / 3000 번지)
    e = 50 # stack 영역(함수 내에 선언 된 변수)
    f = 60 # stack 영역
    fn2() # stack 영역에 fn2 함수의 복귀 번지로 저장(3010 번지)

main()
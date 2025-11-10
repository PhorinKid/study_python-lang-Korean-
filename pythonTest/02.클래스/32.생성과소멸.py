class Test:
    def __init__(self): # 객체생성이 완료되면 멤버데이터 초기값을 위해 자동 호출 되는 함수
        print('init call')
        self.a = 0
        self.b = 0
    def __del__(self): # 객체소멸 전 자동 호출되는 함수
        print('del cal') 
    def setData(self,x,y):
        self.a = x
        self.b = y
    def show(self):
        print(self.a, self.b)

# obj = Test()
# obj1 = obj
# obj = 'abc
# print('hello')

# def fn():
#     obj = Test()
#     obj.show()

# fn()
# print('hello')

def fn():
    obj = Test()
    obj.show()
    return obj

rst = fn()
print('hello')
rst.show()

# 파이썬의 참조계수기법 (reference count 0 이 되면 객체 소멸)
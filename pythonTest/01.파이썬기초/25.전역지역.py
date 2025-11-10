# 파이썬 컴파일러가 만들어 주는 전역변수
# '__name__': '__main__'
# '__doc__': None 
# ...
# '__file__': 'c:\\pythonTest\\25.전역지역.py', '__cached__': None,

g = 10

def fn() :
    g=100
    print('지역변수 :', locals())

fn()
print('g =', g)
print("전역변수 :", globals())

# {'__name__': '__main__', '__doc__': None, '__package__': None, 
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F30B354AC0>, 
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
# '__file__': 'c:\\pythonTest\\25.전역지역.py', '__cached__': None, 
# 'g': 10, 'fn': <function fn at 0x000001F30B293E20>} -> 함수 fn 에 할당된 주소(16진수)
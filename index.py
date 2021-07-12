import sympy as sym

class integral:
    def __init__(self, expresstion:str, x1, x2) -> None:
        expresstion = expresstion.replace("^", "**")
        self.expresstion = expresstion
        self.x1 = int(x1)
        self.x2 = int(x2)

    def integral_expresstion(self) -> None:
        x = sym.Symbol('x')
        a = sym.integrate( eval(self.expresstion) , (x, self.x1, self.x2))
        sym.pprint(a)
        
    def exp(self, x) -> int,float:
        return(eval(self.expression))

    def square(self, x1, x2) -> int,float:
        y1 = self.exp(x1)
        y2 = self.exp(x2)
        y = (y1 + y2) / 2
        square = (x2 - x1) * y
        return square

    def square_integral(self, divisor):
        length = self.x2 - self.x1
        unit = length / divisor
        area = 0 

        _x1 = self.x1 - unit
        for i in range(1, divisor):
            _x1 = _x1 + unit
            _x2 = _x1 + unit

            area += self.square(_x1, _x2)

        sym.pprint(area)


if __name__ == "__main__":
    expresstion = input("수식을 입력하세요: y=")
    x1 = input("적분의 아래끝을 입력하세요: ")
    x2 = input("적분의 위끝을 입력하세요: ")
    a = integral(expresstion, x1, x2)
    a.integral_expresstion()
    a.square_integral(10)

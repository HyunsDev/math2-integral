import sympy as sym
import time
import decimal

class Integral:
    def __init__(self, expression:str, x1:int, x2:int, debug:bool=False):
        """
        계산할 정적분식을 입력합니다.
        """

        expression = expression.replace("^", "**")
        self.expression = expression
        self.x1 = decimal.Decimal(str(x1))
        self.x2 = decimal.Decimal(str(x2))
        self.debug = debug

    def integral_expression(self) -> float:
        "심파이의 integrate를 이용하여 정적분을 계산합니다."

        x = sym.Symbol('x')
        a = sym.integrate( eval(self.expression) , (x, self.x1, self.x2))
        return a
        
    def exp(self, x) -> float:
        """
        등록된 식을 계산하여 y값을 리턴합니다. (적분이 아닙니다.)
        """
        return decimal.Decimal(str(eval(self.expression)))

    def square_left(self, x1, x2) -> float:
        """
        x1과 x2를 받아 x1의 함수값을 기준으로 사각형의 넓이를 리턴합니다.
        리만 왼쪽합을 구할 때 사용됩니다.
        """

        y1 = self.exp(x1)
        y = y1
        square = decimal.Decimal(str(x2 - x1)) * y 
        return square

    def square_right(self, x1, x2) -> float:
        """
        x1과 x2를 받아 x1의 함수값을 기준으로 사각형의 넓이를 리턴합니다.
        리만 오른쪽합을 구할 때 사용됩니다.
        """
        y2 = self.exp(x2)
        y = y2
        square = decimal.Decimal(str(x2 - x1)) * y 
        return square

    def square_integral(self, divisor:int, mode:str) -> float:
        """
        등록된 식을 리만합을 통해 계산합니다.
        mode를 이용하여 리만 왼쪽합과 오른쪽 합을 선택할 수 있습니다. (left, right를 이용하여 선택)
        """

        length = self.x2 - self.x1
        unit = decimal.Decimal(str(length / divisor))
        area = decimal.Decimal(str(0))

        for i in range(1, divisor+1):
            _x1 = decimal.Decimal(str(self.x1 + unit * (i - 1)))
            _x2 = decimal.Decimal(str(self.x1 + unit * i))
            if mode == "left":
                square_area = decimal.Decimal(str(self.square_left(_x1, _x2)))
            elif mode == "right":
                square_area = decimal.Decimal(str(self.square_right(_x1, _x2)))
            area += square_area

            if self.debug: print(f"[{i}/{divisor} 번째] {square_area}(총 {area})")
        return area


if __name__ == "__main__":
    expression = input("수식을 입력하세요: y=")
    x1 = int(input("적분의 아래끝을 입력하세요: "))
    x2 = int(input("적분의 위끝을 입력하세요: "))
    divisor = int(input("사각형을 얼마나 나눌지 입력하세요: "))
    mode = input("어떤 리만합을 사용할까요? (left/right): ")

    start = time.time()
    a = Integral(expression, x1, x2, debug=True)
    a1 = a.integral_expression()
    a2 = a.square_integral(divisor,mode)
    elapsed_time = round(time.time() - start,3)
    print("="*20)
    print(f"수식: y={expression}")
    print(f"범위: {x1}, {x2}")
    print(f"리만 합: {mode}, {divisor}로 나눔")
    print("="*20)
    print(f"리만 합을 이용한 답: {a2}")
    print(f"정적분을 이용한 값: {a1}")
    print(f"두 값의 차: {abs(a2-a1)}")
    print("="*20)
    print(f"소모 시간: {elapsed_time}초")

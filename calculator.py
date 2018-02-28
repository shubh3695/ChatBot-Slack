class Calculator(object):
    def __init__(self, a, b, op):
        self.a, self.b, self.c = a, b, op
    def solve(self):
        try:
            ans = "To be added soon.. :("
            if self.c == "+":
                ans = self.a + self.b
            elif self.c == "-":
                ans = self.a - self.b
            elif self.c == "*":
                ans = self.a * self.b
            elif self.c == "/":
                if self.b == 0:
                    ans = "Cannot Divide by Zero"
                else:
                    ans = self.a/self.b
            elif self.c == "%":
                if self.b == 0:
                    ans = "Cannot Divide by Zero"
                else:
                    ans = self.a%self.b
            return str(ans)
        except Error as e:
            return "Some Error Occured"
        
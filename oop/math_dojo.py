class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        return self
    def reset(self):
        self.result = 0
# your code here



# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
md.reset()

y = md.add(1).add(2,3,4,5).add(1,2).subtract(3).subtract(7,6,5).result
print(y)

md.reset()

z = md.add(12,13,14).subtract(10).result
print(z)
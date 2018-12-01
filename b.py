class Cat:
	#方法
	def __init__(self):
		print('hhaha.....')

	def eat(self):
		print('111')

	def drink(self):
		print('222')

	def introduce(self):
		print('%s的年龄是：%s' % (self.name, self.age))

tom = Cat()
#调用方法有()
tom.eat()
tom.drink()
#添加属性
tom.name = '汤姆'
tom.age = 40
tom.introduce()

lanmao = Cat()
lanmao.name = '蓝猫'
lanmao.age = 10
lanmao.introduce()

def function():
	pass
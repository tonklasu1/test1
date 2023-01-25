class AIChatBot:
	def __init__(self, std_id, op,a,b):
		self.std_id = std_id
		self.op = op
		self.a =a
		self.b= b
	def showSubjectName(self):
		print('AI for robot system')
	def showStudentYear(self):
		print(self.std_id[0])
	def calculator(self):
		if self.op == '+':
			o = self.a+self.b
		elif self.op=='-':
			o = self.a-self.b
		print(o)
while(1):
	i = input()
	if i == 'subject':
		AI = AIChatBot(1,2,3,4)
		AI.showSubjectName()
	if i == 'year':
		j=input()
		AI = AIChatBot(j,'a','b','c')
		AI.showStudentYear()
	if i == 'calc':
		j=input()
		a=int(input())
		b=int(input())
		AI = AIChatBot('a',j,a,b)
		AI.calculator()

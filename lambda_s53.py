# a="j'ai soif"
# def s(arg):
	# print(arg)
# s(a)
#------------------------Avec lambda--------------------#
s = lambda arg: print("Bonjour "+arg)
s("j'ai soif")

print((lambda arg: "Bonjour "+arg)("j'ai soif"))

(lambda arg: print("Bonjour "+arg))("j'ai soif")

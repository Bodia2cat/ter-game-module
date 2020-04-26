class 


game_title = "none"
game_name = "none"

def gameplay():
	#write your gameplay here!!!
	print("test is ok! \nSo delete this text in 'gamepy.py' ")
def SetName(name_g):
	game_name = name_g
def SetTitle(title):	 
	global game_title
	game_title = title
def gameMenu():
	print("1) Start")
	print("2) exit")
	menua = input(game_title + ">_")
	if menua == "1":
		gameplay()
	if menua == "2":
		exit()

def Creators():
	print("Bodia_2cat")
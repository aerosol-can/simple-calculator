import os, sys
def get_platform():
	platforms = {
		'linux1' : 'Linux',
		'linux2' : 'Linux',
		'darwin' : 'OS X',
		'win32' : 'Windows',
	}
	if sys.platform not in platforms:
		return sys.platform
	
	return platforms[sys.platform]

def clear():
	if platform == 'Windows':
		os.system('cls')
	else :
		os.system('clear')

def help():
	print('''
	help	: Print this help menu.
	clear	: Clear the screen.
	exit	: Exit the session.
	''')

def main():
	global platform 
	platform = get_platform()
	print("Enter the expressions to Evaluate. Type help for the Help menu.")
	while True:
		inpt = input(":")
		if inpt == "help":
			help()
		elif inpt == "exit":
			exit()
		elif inpt == "clear":
			clear()
		else:
			print(eval(inpt))

main()
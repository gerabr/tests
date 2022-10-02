import os

def list_dir(directory='.'):
	return os.listdir(directory)

def show_user():
	os.system('id')

def main():
	show_user()
	a = list_dir()
	for dir in a:
		print(f"Filename: {dir}")

if __name__ == "__main__":
	main()

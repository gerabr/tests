import os

def list_dir(directory='.'):
	return os.listdir(directory)

def main():
	print(list_dir())

if __name__ == "__main__":
	main()

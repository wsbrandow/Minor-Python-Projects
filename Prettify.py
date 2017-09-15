print("Enter HTML Text Below")
while True:
	from bs4 import BeautifulSoup

	inputdata = input("")
	soup = BeautifulSoup(inputdata, "html.parser")

	print(soup.prettify())


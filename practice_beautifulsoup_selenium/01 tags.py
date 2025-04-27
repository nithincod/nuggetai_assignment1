import requests
from bs4 import BeautifulSoup 
with open("sample.html") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())
# print(soup.title.string, type(soup.title.string))
# print(soup.div)

# print(soup.find_all("div"))

# for link in soup.find_all("a"):
#     print(link.get("href"))

#     print(link.get_text())

# print(soup.find(id="nithin")) 

# print(soup.select("div.italic"))

# print(soup.select("span#bold"))

# print(soup.span.get("class"))//first span me class melega

# print(soup.find(id="italic"))
# print(soup.find(class_="italic")) special keywod for class

# to find all children for class

# for child in soup.find(class_="container").children:
#     print(child)

#find parents of child

# for parent in soup.find(class_="box").parents:
#     print(parent) 
#     break       

# changiging existing tags

# cont=soup.find(class_="container")
# cont.name="span"
# cont["class"]="myclass class2"
# cont.string="This is a new string"
# print(cont)

# adding new tags

# uitag=soup.new_tag("ul")
# litag=soup.new_tag("li")
# litag.string="Home"
# uitag.append(litag)


# litag=soup.new_tag("li")
# litag.string="About"
# uitag.append(litag)

# soup.html.body.insert(0,uitag)

# with open("modified.html", "w") as f:
#     f.write(str(soup))

cont=soup.find(class_="container")
print(cont.has_attr("contenteditable"))




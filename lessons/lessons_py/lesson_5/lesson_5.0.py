text = "Hello"
print(id(text))

text = {}
print(id(text))

upper_text = "HELLO"
print(upper_text.lower())

lower_text = "hello"
print(upper_text.upper())

text = "hello"
print(upper_text.capitalize())

text_ = "hello, world"
print(id(text_))

text_title = text_.title()
print(id(text_.title()))

username = input()
print(username.rstrip())

username = input()
new_user_for_endpoin = username.strip()
BASE_URL = "ozon/api"

req_url = f"{BASE_URL}/{new_user_for_endpoin}"
print(req_url)

text = "appl:banana:orange"
fruits = text.split(":")
print(type(fruits))
print(fruits)
print(fruits[0])
new_text = ":".join(fruits)
print(new_text)
print(type(new_text))

text = "hello world"
result = text.replace("//", "")
print(result)

text = "Hello world"
print(text.find("o"))
print(text.count("l"))

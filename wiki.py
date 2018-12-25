import wikipedia

_input = input()
page = wikipedia.page(_input)

print(page.title)
print(page.content)

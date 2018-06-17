from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://python.org/')

print('links')
print(r.html.links)
print()
print('absolute links')
print(r.html.absolute_links)
print()

about = r.html.find('#about', first=True)
print('text of first #about element')
print(about.text)
print()
print('attributes of an element')
print(about.attrs)
print()

import time
#print(time.ctime())

def show_default(arg=time.ctime()):
    print(arg)

show_default()
show_default()

def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['bacon', 'eggs']
print(add_spam(breakfast))

dinner = ['sousarges', 'omlent', 'nugets']
print(add_spam(dinner))

print(add_spam())
print(add_spam())
print(add_spam())

def add_spam1(menu=None):
    if(menu is None):
        menu = []
    menu.append("spam")
    return menu

print(add_spam1())
print(add_spam1())
print(add_spam1())

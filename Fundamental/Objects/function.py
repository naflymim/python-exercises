def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue") 
print()

banner("Norwegian Blue", "*") 
print()

banner("Sun, Moon and Stars", border="*") 
print()

banner(border=".", message="Sun, Moon and Stars")
print()

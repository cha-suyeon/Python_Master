f = open('foo.txt', 'r')
new = f.read()
f.close()

new = new.replace('python', 'java')

f = open('foo.txt', 'w')
f.write(new)
f.close()
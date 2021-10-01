
sen1 = "Python is really 'fun'"
sen2 = "Python is really \"fun\""
print(sen1)
print(sen2)

multi = "It is kind of fun \nto do the impossible."
multi2 = """
        It is kind of fun
        to do the impossible.
        """
print(multi)
print(multi2)

want = 'I want to eat %d apples.' %3
print(want)

eat = 'I want to eat %s appples.' % 'three'
eat2 = 'I want to eat %s appples.' % 3
print(eat)
print(eat2)

percent = 'Error is %d%%' % 100
print(percent)

style = 'I eat {0} apples.'.format('five')
print(style)

style1 = 'I eat {0} apples.'.format(5)
print(style1)

style2 = 'I ate {0} apples. So I was sick for {1} days.'.format('five', 2)
print(style2)

name = "차수연"
age = 25
print(f'제 이름은 {name}이고, 나이는 {age}살 입니다.')

d = {'name':'차수연', 'age':25}
print(f'제 이름은 {d["name"]}이고, 나이는 {d["age"]}살 입니다.')
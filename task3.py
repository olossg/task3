n1 = 0
n2 = 0
n3 = 0
other = 0
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
for i in range(len(queries)):
    if len(queries[i].split())==1:
        n1+=1
    elif len(queries[i].split())==2:
        n2+=1
    elif len(queries[i].split())==3:
        n3+=1
    else:
        other+=1
print(n1,n2,n3,other)
b = n2*100/(n1+n2+n3+other)
print('поисковых запросов из одного слова ',"%.0f" % (n1*100/(n1+n2+n3+other)),'%')
print('поисковых запросов из двух слов ',"%.0f" % (n2*100/(n1+n2+n3+other)),'%')
print('поисковых запросов из трех слов ',"%.0f" % (n3*100/(n1+n2+n3+other)),'%')
print('поисковых запросов из более трех слов ',"%.0f" % (other*100/(n1+n2+n3+other)),'%')


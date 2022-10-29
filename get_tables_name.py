# Формирование списка таблиц
# Из иходного файла в файл 'names_tables.txt' копируется строка с фигурированием все таблиц в файле
# Да, можно было вытащить имена пропарсив весь файл, но так быстрее

from get_line import get_line

file_name = 'names_tables.txt'

fi_ = get_line(file_name)

out_ = ''
i = 0
while (res := next(fi_,False)):
    i+=1
    s_ = res.find('"')
    e_ = res.rfind('"')
    if s_ < e_:
        out_ += res[s_+1:e_-1] + '\n'

with open('tables.txt','w') as f:
    f.write(out_)
    
print(out_)
print(i)

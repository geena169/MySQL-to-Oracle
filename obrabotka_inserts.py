from os import listdir as get_names

from get_line import get_line
from get_title_obr import get_title
from func_del_sep import del_sep

path_in = 'out/siroe'
path_out = 'out/obrabotannoe'

find_line = '),('
find_s = '('



files = get_names(path_in)

for file in files:
    fi_ = get_line(path_in+'/'+file)
    
    i = 0
    title = get_title(file)
    
    with open(f'{path_out}\{file}','w',encoding='utf-8') as f:
        f.write(title)
        
    while (res := next(fi_,False)):
        i+=1

        # обрезание начала и конца строки #
        s_ = res.find(find_s) + 1
        res = res[s_:-3] + '\n'

        # разделение строки на строки для БД #
        res = res.replace(find_line,'\n')

        # удаление лишних запятых #
        res = del_sep(res,",'","'",",",";")
        
        
        with open(f'{path_out}\{file}','a',encoding='utf-8') as f:
            f.write(res)
        
    print(f'{file} done')
    

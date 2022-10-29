# Обрабтка файлов создания таблиц
# Приведение к виду для ввода в БД Oracle (удаление ключей, приведение типов данных)

from os import listdir as get_names

from get_line import get_line

path_in = 'out/create'
path_out = 'out/create_obr'

kav = '`'

f_r = {'tinyint':'varcha2','polygon':'varchar(1000)','text':'varchar2(1000)','varchar':'varchar2','datetime':'varchar2(30)','float':'varchar2(100)','int':'varchar2','timestamp':'vaechar2(15)','date':'vaechar2(30)','double':'varchar2(100)'}

rpl = 'varchar2'
rpl_i = 'varchar2(1000)'

files = get_names(path_in)

for file in files:
        
    fi_ = get_line(path_in+'/'+file)
    
    out_ = ''
    title = next(fi_)
    while (res := next(fi_,False)):

        if res[2] == kav:
            s_ = res.find(' ',3) + 1
            e_ = res.find(' ',s_)
            type_str = res[s_:e_]
            #input(type_str)
            if (l_ :=type_str.find('(')) == -1:
                out_ += res[:s_] + rpl_i + res[-2:]
            else:
                if type_str.find(',') == -1:
                    out_ += res[:s_] + rpl + res[s_+l_:e_] + res[-2:]
                else:
                    out_ += res[:s_] + rpl_i + res[-2:]
        else:
            out_ = out_.rstrip(',\n') + '\n)'
            
            break
    out_ = title.replace(kav,"") + out_.replace(kav,"'")
    print(f'{file} done')
    with open(f'{path_out}/{file}','w',encoding='utf-8') as f:
        f.write(out_)

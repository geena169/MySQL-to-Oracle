from get_line import get_line

out_path = 'out/siroe'
file_name = 'dump-pik-202209152122.sql'
find_ = 'INSERT INTO'
kav = '`'

fi_ = get_line(file_name)


out_ = ''
i = 0
while (res := next(fi_,False)):
    i+=1
    #input(res)
    if res.find(find_) != -1:
        s_ = res.find(kav) + 1 # для пропуска кавычки
        e_ = res.find(kav, s_)

        with open(f'{out_path}\{res[s_:e_]}.sql','a',encoding='utf-8') as f:
            #input(f'{i}    {len(res)} {type(res)}')
            f.write(res)
        #input(i)

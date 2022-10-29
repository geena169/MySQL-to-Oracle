from get_line import get_line

out_path = 'out\create'
file_name = 'dump-pik-202209152122.sql'
find_s = 'CREATE TABLE'
find_e = ')'

kav = '`'


fi_ = get_line(file_name)


i = 0
while (res := next(fi_,False)):
    i+=1
    #input(res)
    if res.find(find_s) != -1:
        # название таблицы #
        s_ = res.find(kav) + 1 # для пропуска кавычки
        e_ = res.find(kav, s_)
        out_name = res[s_:e_]

        out_ = res
        j = 0
        while res[0] != find_e:
            res = next(fi_)
            j+=1
            out_ += res

        with open(f'{out_path}\{out_name}.sql','w',encoding='utf-8') as f:
            #input(f'{i}    {len(res)} {type(res)}')
            f.write(out_)
        #input(f'start {i}\n end {i+j}')
        i+=j

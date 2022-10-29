# Создание шапки для конечного csv файла

from get_line import get_line

path_title = 'out/create_obr'
kav = "'"
stop_ = ')'

def get_title(file_name):
    fi_ = get_line(path_title+'/'+file_name)
    
    title = ''
    next(fi_)
    
    while (res := next(fi_,False)):

        if res == stop_:
            break
            
        
        s_ = res.find(kav) + 1
        e_ = res.find(kav, s_)

        title += res[s_:e_] + ','
        
        
    title = title.rstrip(',') + '\n'
    
    #print(f'{file_name} title done')
    return title

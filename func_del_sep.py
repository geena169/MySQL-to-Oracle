# удаление лишних символов разделения строки
# del_sep('исходная строка', 'начало поиска', 'конец поиска',
#       'что меняем', 'на что меняем')
# начало поиска 2 символа (с символом предшествующим необходимому)
# Ex: если ищем ',' внутри строки:
#      50000,NULL,'[{\"lastname\":\"Сочнов\",\"name\":\"Сергей\",3240,545
# то вид вызываемой func:  line = del_sep(line,",'","'",",",";")

def del_sep(line, find_s, find_e, sep, sep_change):
    s_ = line.find(find_s) + 1    
    while True: 
                        
        e_ = line.find(find_e,s_+2)
        if (line[s_:e_+1].find(sep) != -1):
            #input(f'{i=}  {s_}  {e_} \n {line[s_:e_+1]}')
            kusok = line[s_+1:e_]
            line = line[:s_+1] + kusok.replace(sep,sep_change) + line[e_:]
            
            # необходимо узнать кол-во убранных символов, чтобы
            # скорректировать поиск кавычек (инче собьются)
            e_ -= len(kusok) - len(kusok.replace(sep,sep_change))
                                
        s_ = line.find(find_s,e_) 
        
        # выход по окончанию стоки
        if (s_ == -1):
            break

    return line
        
        
    
        



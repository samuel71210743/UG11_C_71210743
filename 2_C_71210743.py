def check_data_type(kata, type_data): 

    if (type(kata).__name__.lower() == type_data.lower()):
        
        result = print('Jawaban Anda benar\n'
                        'True')
    else : 
         result = print('Jawaban Anda salah, seharusnya adalah: ', type(kata).__name__,'\n'
                         'False')
                        
   
    return result 

check_data_type(True,'Bool') 
check_data_type(True,'bool')
check_data_type({},"TUPLE") 
check_data_type({},"DIct")
check_data_type([],"")

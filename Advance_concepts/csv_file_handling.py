
''' Csv file creation and writing content into csv file'''

# # import csv
# # file = open('emp.csv','w')
# # writer_obj=csv.writer(file)
# ''' writing field name into emp.csv file'''
# # writer_obj.writerow(['empno','ename','job','mgr','sal','deptno'])
# # file.close()

# ''' adding multiple records into emp.csv file'''
# # import csv
# # file = open('emp.csv','a',newline='')
# # writer_obj=csv.writer(file)
# # writer_obj.writerows([['0123','asha','developer','007',1500,30],['0121','raishan','developer','007',1500,30],['0420','rahul','tester','010',1200,10],['0400','ram','devops','020',1100,40],['0303','vyshu','analytics','050',1000,70]])
# # file.close()

# '''1.wap to get the records of employees whose salary is morethan 1000'''

# import csv
# def get_records_emps_sal_grtn(sal):
#     file=open('emp.csv')
#     reader_obj=csv.reader(file)
#     records=[]
#     for record in reader_obj:
#         if record[4]>1000:
#             records.append(record)
#     file.close()   
#     return records
    
# ''' wap to get the record of a particular line mentioned by user'''
# def get_record_at_line_num(num:int):
#     file=open('emp.csv')
#     reader_obj=csv.reader(file)
#     for record in reader_obj:
#         if reader_obj.line_num==num:
#             file.close()
#             return record
       
#     else:
#         file.close
#         return 'not found'

# def get_records_emps(department):
#     file=open('emp.csv')
#     reader_obj=csv.reader(file)
#     records=[]
#     for record in reader_obj:
#         if record[2]==department:
#             records.append(record)
#     file.close()   
#     return records 

# def get_ename_having_min_vowels(num:int):
#     file=open('emp.csv')
#     reader_obj=csv.reader(file)
#     records=[]
#     next(reader_obj)
#     for record in reader_obj:
#         name=record[1]
#         count=0
#         for char in name:
#             if char in 'aeiouAEIOU':
#                 count+=1
#         if count==num:
#             records.append(name)

#     file.close()   
#     return records 
# print(get_ename_having_min_vowels(3))

# def add_record():
#     file=open('emp.csv','a')

#     writer_obj=csv.DictWriter(file,['empno','ename','job','mgr','sal','deptno'])

#     writer_obj.writerow({'empno':'0234','ename':'kalyan','job':'developer','mgr':'0100','sal':1500,'deptno':30})
    
    
#     file.close()   
# add_record()

import csv
def get_even_records():
    file=open('emp.csv')
    file.seek(0)
    reader_obj=csv.reader(file)
    records=[]
    count=0
    next(reader_obj)
    for record in reader_obj:
        if count%2==0:
            records.append(record)
            count+=1
        else:
            count+=1
        
    file.close()
    return records
       
print(get_even_records())

def get_even_records():
    file=open('emp.csv')
    file.seek(0)
    reader_obj=csv.reader(file)
    records=[]
    count=0
    next(reader_obj)
    for record in reader_obj:
        if reader_obj.line_num%2==0:
            records.append(record)
            count+=1
        else:
            count+=1
        
    file.close()
    return records
       
print(get_even_records())
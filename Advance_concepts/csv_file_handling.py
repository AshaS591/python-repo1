
''' Csv file creation and writing content into csv file'''

# import csv
# file = open('emp.csv','w')
# writer_obj=csv.writer(file)
''' writing field name into emp.csv file'''
# writer_obj.writerow(['empno','ename','job','mgr','sal','deptno'])
# file.close()

''' adding multiple records into emp.csv file'''
# import csv
# file = open('emp.csv','a',newline='')
# writer_obj=csv.writer(file)
# writer_obj.writerows([['0123','asha','developer','007',1500,30],['0121','raishan','developer','007',1500,30],['0420','rahul','tester','010',1200,10],['0400','ram','devops','020',1100,40],['0303','vyshu','analytics','050',1000,70]])
# file.close()

'''1.wap to get the records of employees whose salary is morethan 1000'''

import csv

class EmpInfo:

    def get_records_emps_sal_grtn(self,sal):
        file=open('emp.csv')
        file.seek(0)
        reader_obj=csv.reader(file)
        records=[]
        next(reader_obj)
        for record in reader_obj:
           
            if int(record[4])>sal:
                records.append(record)
        file.close()   
        return records
        
    ''' wap to get the record of a particular line mentioned by user'''
    def get_record_at_line_num(self,num:int):
        file=open('emp.csv')
        reader_obj=csv.reader(file)
        for record in reader_obj:
            if reader_obj.line_num==num:
                file.close()
                return record
        
        else:
            file.close
            return 'not found'

    def get_ename_where_job_is(self,job):
        file=open('emp.csv')
        reader_obj=csv.reader(file)
        records=[]
        next(reader_obj)
        for record in reader_obj:
            if record[2]==job:
                records.append(record[1])
                
        file.close()
        return records 

    def get_ename_having_min_vowels(self,num:int):
        file=open('emp.csv')
        reader_obj=csv.reader(file)
        records=[]
        next(reader_obj)
        for record in reader_obj:
            name=record[1]
            count=0
            for char in name:
                if char in 'aeiouAEIOU':
                    count+=1
            if count==num:
                records.append(name)

        file.close()   
        return records 

    def add_record(self):
        file=open('emp.csv','a')

        writer_obj=csv.DictWriter(file,['empno','ename','job','mgr','sal','deptno'])

        writer_obj.writerow({'empno':'0234','ename':'kalyan','job':'developer','mgr':'0100','sal':1500,'deptno':30})
        
        
        file.close()   
    
    def get_even_records1(self):
        file=open('emp.csv')
        # file.seek(0)
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
        
    
    print()
    def get_even_records(self):
        file=open('emp.csv')
        # file.seek(0)
        reader_obj=csv.reader(file)
        records=[]
    
        next(reader_obj)
        for record in reader_obj:
            if reader_obj.line_num%2==0:
                records.append(record)      
        file.close()
        return records
        

    def get_avg_sal_of_emps(self):
        file=open('emp.csv')
        # file.seek(0)
        reader_obj=csv.reader(file)
        count=0
        next(reader_obj)
        sum=0
        count=0
        for record in reader_obj:
            sum+=int(record[4])
            count+=1
        avg=sum/count
            
        file.close()
        return avg
        

    def get_max_sal_emp(self):
        file=open('emp.csv')
        # file.seek(0)
        reader_obj=csv.reader(file)
        records=[]
        
        next(reader_obj)
        for record in reader_obj:
            records.append(int(record[4]))
        else:
            max_sal=max(records)
        file.seek(0)
        for data in reader_obj:
            if data[4]==str(max_sal):
                file.close()
                return data[1]
                

    def get_records_deptwise(self):
        file=open('emp.csv')
        # file.seek(0)
        reader_obj=csv.reader(file)
        records={}
    
        next(reader_obj)
        for record in reader_obj:
            if record[2] in records:
                records[record[2]]+=1
            else:
                records[record[2]]=1
            
        file.close()
        return records
        

    def get_record_of_emp_mng_to_emp(self,name):
        file=open('emp.csv')
        file.seek(0)
        reader_obj=csv.reader(file)
        records=[]
        next(reader_obj)
        for record in reader_obj:
            if record[1] == name:
                mgr=record[3]
        else:
            file.seek(0)
            for data in reader_obj:
                if data[0]==mgr:
                    records.append(data)
            
        file.close()
        return records
        
record=EmpInfo()
print(record.get_records_emps_sal_grtn(1500))
print(record.get_record_at_line_num(6))
print(record.get_ename_where_job_is('developer'))
print(record.get_ename_having_min_vowels(3))
# print(record.add_record())
print(record.get_even_records())
print(record.get_avg_sal_of_emps())
print(record.get_max_sal_emp())
print(record.get_records_deptwise())
print(record.get_record_of_emp_mng_to_emp('asha'))
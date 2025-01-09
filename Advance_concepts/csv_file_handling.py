import csv
file = open('emp.csv','w')
reader_obj=csv.writer(file)
reader_obj.writerow(['empno','ename','job','mgr','sal','deptno'])
file.close()

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
"""
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if  col<=n//2 or row>=n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

#######################################################

'''
* * * * * * * * * 
  * * * * * * * *
    * * * * * * *
      * * * * * *
        * * * * *
          * * * *
            * * *
              * *
                *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if   row<=col:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

####################################################

'''
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if   row>=col:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#########################################################

'''
* * * * * * * * * 
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if   row+col<=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#########################################################

'''
* 
              * *
            * * *
          * * * *
        * * * * *
      * * * * * *
    * * * * * * *
  * * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if  row+col>=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

#######################################################

'''
* * * * * * * * * 
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if   row==0 or row==n-1 or col+row==n-1 or col==row or (row<col and row+col<=n-1) or(col<row):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

############################################################

'''
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if  row<=col and row+col<=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

####################################################

'''
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if  (row<=col and row+col<=n-1) or (row>=col and row+col>=n-1):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

######################################################

'''
* * * * * * * * * 
* * * * * * * *
* * * * * * *
* * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col<=n//2 or row>=n//2 or row+col<=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

#################################################

'''
* * * * * * * * * 
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row<=col or row>=col:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

#######################################################

'''
* * * * * * * * * 
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row<=col or col+row<=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

################################################

'''
        *
      * * *
    * * * * *
  * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row<=col or col+row<=n-1:
            print(' ',end=" ")
        else:
            print('*',end=" ")
    print()  

###################################################

'''
*
* *
* * *
* * * *
* * *
* *
*
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col>=row or col+row>=n-1:
            print(' ',end=" ")
        else:
            print('*',end=" ")
    print()  

##################################################

'''
        *
       * *
      * * *
     * * * *
      * * *
       * *
        *

'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col<=row or col+row<=n-1:
            print('',end=" ")
        else:
            print('*',end=" ")
    print()  

########################################################

'''
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row>col and row+col<=n-2) or (col>row and row+col>=n):
            print(' ',end=" ")
        else:
            print('*',end=" ")
    print()  

#######################################################

'''
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==n//2 ) or col==n//2 or row+col==n//2 or row+col<n//2  or row-col==n//2 or col-row<=n//2 or row+col==(n//2)*3:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()  

#########################################################

'''

'''
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row+col<n//2  or row+col>n//2
            ):
            print(' ',end=" ")
        else:
            print('*',end=" ")
    print()  

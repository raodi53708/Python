# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:26:52 2020

@author: Dilpa Rao 1906319
"""


"""
The load_from_csv function takes one parameter-filename(which is the name of the csv file)
and it returns the output as a matrix, where each row of the file is a row in the matrix
and the length of the matrix is the number of rows in the file.
"""
def load_from_csv(filename):
    import os
    import csv
    filelist=[]
    # checking whether the file exists
    if os.path.isfile(filename):
        file1=open(filename)
        filelist = [[float(x) for x in rec] for rec in csv.reader(file1, delimiter=',')]                 
    else:
        print('File does not exist..... Please enter the exact path')        
    return filelist

"""
The get_distance function takes two lists as its parameters and it returns the sum of
absolute distance between the two list i.e the Manhattan distance
"""
def get_distance(list1,list2):
    sum=0
    for i in range(len(list1)):
        result=list1[i]-list2[i]
        #checks if the distance is negative, then makes it absolute
        if result<0:
            result=-result
        sum=sum+result
    return sum

"""
The get_max function takes two arguments one is data matrix (list of list) and the other 
is the column number,it returns the maximum value of the specified column number 
in the matrix.
"""   
def get_max(matrix1,colno):
    collist=[]                     
    #colno=colno-1                           # as the index starts from 0 so we deduct-1
    max_col_value=0
    for i in range(len(matrix1)):
        collist.append(matrix1[i][colno])
    max_col_value=max(collist)              # stores the maximum column value in max_col_value
    return max_col_value
    
"""
The get_min function takes two arguments one is data matrix(list of list) and the other 
is the column number,it returns the minimum value of the specified column in the matrix.
"""   
def get_min(matrix1,colno):
    collist=[]
    #colno=colno-1
    min_col_value=0                         ## as the index starts from 0 so we deduct-1 
    for i in range(len(matrix1)):
        collist.append(matrix1[i][colno])
    min_col_value=min(collist)              # stores the minimum column value in min_col_value
    return min_col_value
    
"""
The get_avg function takes two arguments one is data matrix(list of list) and the other 
is the column number,it returns the average value of the specified column in the matrix using 
the  mean function of the library statistics.
"""      
def get_avg(matrix1,colno):
    from statistics import mean             # import the library statistics to find the average
    collist=[]
    #colno=colno-1
    avg_col_value=0
    for i in range(len(matrix1)):
        collist.append(matrix1[i][colno])
    avg_col_value=mean(collist)
    return avg_col_value
    
"""
The get_median function takes two arguments one is  matrix(list of list-
 containing all values of the column number specified) and the other 
is the column number, it appends all the values of a particular column in collist
it returns the median value of the specified column from the collist using 
the median function of the library statistics
"""    
def get_median(matrix1,colno):
    import statistics
    collist=[]
    colno=colno-1
    median_value=0
    for i in range(len(matrix1)):
        collist.append(matrix1[i][colno])
    median_value=statistics.median(collist)
    return round(median_value,2)
          
"""
The get_standardised_matrix function takes one arguments that is a matrix (data file csv in the form of a list of list)  
It standardises each and every element of the lists of lists  by using the average(get_avg),
maximum(get_max) and minimum(get_min) function and rounding it of to two decimal places.
It appends every element of the row to the newlist1 and after that it appends each row to the finallist1.
It uses the formula provided in the appendix:
   
""" 
def get_standardised_matrix(matrix1):
    mymatrix=matrix1.copy()
   
    
    for j in range(len(matrix1[0])):
        col_avg= get_avg(matrix1,j)
        col_max=get_max(matrix1,j)
        col_min=get_min(matrix1,j)
        #print(col_avg)
        #print(col_max)
        #print(col_min)
        
        for i in range(len(matrix1)):
             mymatrix[i][j]=round((matrix1[i][j]-col_avg)/(col_max-col_min),2)
    #print(mymatrix)            
    return mymatrix



"""
The get_groups function takes two arguments one is data matrix(list of list which contains random centroids)
and the other is  number of groups,it takes the standardise matrix which is stored in mymatrix 
and it calculates the distance between each data point and the centroid .
It stores the value of the distances in the dicionary dict1 and then calculates the
minimum value  and stores it in key_min variable.
After that it appends the current index to the lsit S.

""" 
def get_groups(mycentroid,k):
   centroids=mycentroid
   S=[]
   dist=0
   dict1={}
   #mymatrix=load_from_csv('data.csv')        
   #mymatrix=get_standardised_matrix(mymatrix)
   mylist1=[]
       
   for i in range(len(mymatrix)):
       for j in range(k): 
           dist=get_distance(centroids[j],mymatrix[i])
           dict1.update({j:dist})
           key_min = min(dict1.keys(), key=(lambda k: dict1[k]))
           #print(j,dist)
       mylist1.append(mymatrix[i])
       S.append(key_min+1)          # as the index starts from 0 , so we add 1 
   return S   


"""
The get_centroid function takes three arguments one is centroids(list of list) and the other 
is the list (S), and third the number of groups K.
"""    
def get_centroids(mycentroid,mylist,k):
    centroids=mycentroid
    #mymatrix=load_from_csv('data.csv')        
    #mymatrix=get_standardised_matrix(mymatrix)
    new_centroids=[]
    final_centroid=[]
    
    mylist1=[]
    for i in range(k):
        mylist1=[]
        ctr=i+1
        # appending the values to mylist1
        mylist1=[]
        for j in range(len(mylist)): 
            if mylist[j]==ctr: 
                mylist1.append(mymatrix[j])      
                
        # checking if the each of the centroid column is equal to the median value if not update it  
        for l in range(len(mymatrix[0])):                   
            if centroids[i][l]!=get_median(mylist1,l+1):
                new_centroids.append(get_median(mylist1,l+1))
            else:
                new_centroids.append(get_median(mylist1,l+1))
                
    ctr=0
    #calculating the number of rows and initialising the final_centroid matrix
    no_rows=int(len(new_centroids)/len(mymatrix[0]))
    final_centroid=[[0 for x in range(len(mymatrix[0]))] for y in range(no_rows)]
    # from the list new_centroid adding each element to the 
    #matrix final_centroid of no_rows and len(mymatrix[0]) columns
    for i in range(no_rows):
        for j in range(len(mymatrix[0])):
            final_centroid[i][j]=new_centroids[ctr]
            ctr=ctr+1
    return final_centroid


"""
The run_test function loads the data.csv file and then with random.seed(101) selects k Clusters
.Calls the get_group function passing the matrix centroid and k as parameters and returns list
which is stored in new_list.
new_centroids stores the value of the updated centroids which are returned 
by the get_centroids function

 
""" 
    
def run_test():    
    import random 
    global mymatrix
    mymatrix=load_from_csv('data.csv')  
    mymatrix=get_standardised_matrix(mymatrix)
    old_list=[]
    new_list=[]
     
    random.seed(101)
    centroids=[]
    new_centroids=[] 
    
    for k  in range(2,7):    
        for i in range(k):
            centroids.append(random.choice(mymatrix))
           # print(centroids[i])
         
        new_list = get_groups(centroids,k)    
        new_centroids=get_centroids(centroids,new_list,k)
    # it will compare the previous list values(S) and the new list(S)values and keep on calling the get_group and get_centroid
        while True:   
            # old_list stores the value of the previous list
            old_list=new_list
            # new_list stores the value of the new list which is returned by the get_group()            
            new_list=get_groups(new_centroids,k)
            
            new_centroids=get_centroids(new_centroids,new_list,k)
            if old_list == new_list:
                break
        print(new_list)
        
        # counting the number of individual wine entities in each cluster and for each K groups (2,3,4,5,6)
        ctr=0
        for a in range(max(new_list)):
            for b in range(len(new_list)): 
                if a+1==new_list[b]:
                    ctr=ctr+1
            print('The number of elements in group '+str(a+1) +' when k = '+str(k) + ' is '+ str(ctr))
            ctr=0 
        print()    
        centroids=[]
        new_centroids=[]
  
            
 



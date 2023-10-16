import numpy as np  

"""
The problem of converting a matrix to row echelon form requires four major step
 1- Check for None_zero row in a matrix if pivot element is 0
 2- Swap the pivot element row with non zero row
 3- Make every pivot element 1
 4- Below every pivot element 1 , make every number to 0
""" 

"""
The following code will check whether a given matrix is in echelon form or not.
"""

def check_row_echelon(matrix):
    
    if not matrix.any():
        return False
    
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    
    prev_leading_col = -1
    
    for row in range(rows):
        leading_col_found = False
        
        for col in range(cols):
            if (matrix[row,col] != 0):
                leading_col = col
                
                if(leading_col <= prev_leading_col):
                    return False
                
                prev_leading_col = leading_col
                leading_col_found = True
                break
        
        if not leading_col_found and any(matrix[row,col] != 0 for col in range(cols)):
            return False
        
    return True    


"""
The following function will check for the first nonzero row in a matrix,
in case the first-row pivot-element is 0 it will return the non_zero row.
"""

def get_nonzero_row(matrix, pivot_row, col):
    xrows = matrix.shape[0]
    
    for row in range(pivot_row, xrows):
        if (matrix[row,col] != 0):
            return row       
    return None


"""
In case the first-row pivot-element is 0 and we found a non_zero row,
the following function will swap the non_zero row with the row having 0 as 
a pivot,so that we will have a nonzero element as a pivot.
"""

def swapping_rows(matrix, pivot_row, non_zero_row):
    matrix[[pivot_row, non_zero_row]] = matrix[[non_zero_row, pivot_row]]


"""
The following Function will make the pivot element of pivot_row(in which we
are currently working) equals to 1 by dividing the pivot_row with pivot_element
"""

def make_1_at_pivot(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row, col]
    matrix[pivot_row] //= pivot_element



"""
The following function will make every element below the pivot_element which is
1, equals to 0.
"""

def make_0_below_pivot(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row, col]
    xrows = matrix.shape[0]
    
    for row in range(pivot_row + 1, xrows):
        Number = matrix[row, col]
        matrix[row] -= Number * matrix[pivot_row]      


"""
The main function which starts converting a given matrix to an row echelon form
by perfomring all the operations which are defined above in the form of functions
by calling them at their time
"""

def Convert_To_Echelon(matrix):
    
    xrows = matrix.shape[0]
    xcols = matrix.shape[1]
    
    pivot_row = 0
    
    for col in range(xcols):
     
        non_zero_row = get_nonzero_row(matrix, pivot_row, col)
        
        if non_zero_row is not None:
            swapping_rows(matrix, pivot_row, non_zero_row)
            make_1_at_pivot(matrix, pivot_row, col)
            make_0_below_pivot(matrix, pivot_row, col)
            pivot_row += 1
    
    print(matrix)
    return matrix

"""
INPUT For a matrix which you want to convert into an row echelon form
"""

matrix = np.array([[0,1,0], [1,0,0], [0,0,1]])
result = Convert_To_Echelon(matrix)

if check_row_echelon(result):
    print("The given matrix is in the echelon form")
else:
    print("The given matrix is not in the echelon form")

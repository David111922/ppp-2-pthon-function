# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(x, y, z):
 return max([x,y,z])

print(max_num(29,30,31))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def multi_list(lst): 
   return [x * 5 for x in lst]
print(multi_list( [8, 9, 6]))


#Write a Python function called rev_string() to reverse a string. 
def rev_string(any_string):
  return any_string[::-1]
my_string = "abccba"
my_string = "reverse"
reverse_string = rev_string(my_string)
print(reverse_string)  # Outputs: "abccba

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(number, start, end):
    return start <= number <= end

# Example usag
print(num_within(24, 77, 3))  
print(num_within(10, 2, 5)) 
print(num_within(10, 8, 15)) 
print(num_within(130, 121, 150)) 

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)
# 20221024 - Python OOP - First Steps in OOP
# 01 - Rhombus of Stars


print('\n--------------------- ex. 1 ------------------------\n')


n = int(input("Enter an integer, representing the number of rows you want the triangle to have: "))

for row in range(1, n + 1):
    print(' ' * (n - row), end='')

    for col in range(1, row + 1):
        print('* ', end='')
    print()


"""


input:
------
5


result:
------
    * 
   * * 
  * * * 
 * * * * 
* * * * * 


"""


print('\n--------------------- ex. 2 ------------------------\n')


n = int(input("Enter an integer, representing the number of rows you want the trapezoid to have: "))

for row in range(1, n + 1):
    print(' ' * (n - row), end='')

    for col in range(1, row + 2):
        print('* ', end='')
    print()


"""


input:
------
5


result:
------
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 


"""


print('\n--------------------- ex. 3 ------------------------\n')


n = int(input("Enter an integer, representing the number of rows you want the triangle to have: "))

for row in range(1, n + 1):
    print(' ' * (n - row + 10), end='')

    for col in range(1, row + 1):
        print('* ', end='')
    print()


"""


input:
------
5


result:
------
              * 
             * * 
            * * * 
           * * * * 
          * * * * * 


"""


print('\n--------------------- ex. 4 ------------------------\n')


n = int(input("Enter an integer, representing the number of columns you want the longest row of the triangle to have: "))

for row in range(1, n + 1):
    print('* ' * row)

for row in range(n - 1, -1, -1):
    print('* ' * row)


"""


input:
------
5


result:
------
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


"""


print('\n--------------------- ex. 5 ------------------------\n')


n = int(input("Enter an ODD integer, representing the number of rows you want the diamond to have: "))
n = int(n / 2) + 1

for row in range(1, n + 1):
    print(' ' * (n - row), end='')

    for col in range(1, row + 1):
        print('* ', end='')
    print()

for row in range(n - 1, -1, -1):
    print(' ' * (n - row), end='')

    for col in range(1, row + 1):
        print('* ', end='')
    print()


"""


If you enter ODD number everything will work correct.
If you enter EVEN number you will get a diamond with number of rows - next ODD number after the EVEN number you entered.


input:
------
5


result:
------
  * 
 * * 
* * * 
 * * 
  * 


"""

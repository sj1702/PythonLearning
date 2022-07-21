tr = int(input("enter number of rows: ")) # total number of rows
sym = input("Enter the symbol to print: ")
r = 1  # row number initial
while r <= tr:
    s = tr - r  # calculating number of space to leave before printing symbol
    n = (2 * r) - 1  # how many times to print symbol
    print(" " * s, sym * n)
    r += 1

""" Output:
enter number of rows: 5
Enter the symbol to print: *
     *
    ***
   *****
  *******
 *********

"""
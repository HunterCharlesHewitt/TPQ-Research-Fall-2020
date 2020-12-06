# TPQ-Research-Fall-2020
Exploration of solutions to the Yang Baxter Equation in twisted tensor product representations of finite groups, with a focus on discovering solutions to the dihedral group of order 8.

# Getting Started
1. Read through [BRAID GROUP REPRESENTATIONS FROM TWISTED TENSOR PRODUCTS OF ALGEBRAS](https://arxiv.org/pdf/1906.08153.pdf) (code is at the end)
2. Reference [MAGMA documentation](http://magma.maths.usyd.edu.au/magma/pdf/first.pdf)
3. Try out code with [MAGMA Calculator](http://magma.maths.usyd.edu.au/calc/)

# The Process
## MAGMA Code
As outlined in Dr. Rowell's paper, we will be working with MAGMA in order to find solutions to the Yang-Baxter equation in twisted tensor products of finite groups. The general structure of the code follows the format
1. Create a cyclotomic field (rational numbers adjoined with root of unity)
2. Create a free algebra from this field with n variables. These variables will be our group generators as well as our coefficients, and any other necessary variables. In my code, z is used to represent the inverse of the determinant of the r1 matrix described in the maple section. The free algebra is essentially the non-commutative version of a polynomial ring. This is useful for defining variables in the dihedral group since they aren't commutative. 
3. Define a commutator function. When variables are passed to this function, and then included in our ideal generation later, we essentially are telling MAGMA "make these two variables commute with each other". The "z" function argument if +1 will make the variables commute and if -1 will make them anti-commute. 
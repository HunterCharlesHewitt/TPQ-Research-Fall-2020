# TPQ-Research-Fall-2020
Exploration of solutions to the Yang Baxter Equation in twisted tensor product representations of finite groups, with a focus on discovering solutions to the dihedral group of order 8.

# Getting Started
1. Read through [BRAID GROUP REPRESENTATIONS FROM TWISTED TENSOR PRODUCTS OF ALGEBRAS](https://arxiv.org/pdf/1906.08153.pdf) (code is at the end)
2. Reference [MAGMA documentation](http://magma.maths.usyd.edu.au/magma/pdf/first.pdf)
3. Try out code with [MAGMA Calculator](http://magma.maths.usyd.edu.au/calc/)

# The Process
### MAGMA Code Explanation/Walkthrough
As outlined in Dr. Rowell's paper, we will be working with MAGMA in order to find solutions to the Yang-Baxter equation in twisted tensor products of finite groups. The general structure of the code follows the format
1. Create a cyclotomic field (rational numbers adjoined with root of unity)
2. Create a free algebra from this field with n variables. These variables will be our group generators as well as our coefficients, and any other necessary variables. In my code, z is used to represent the inverse of the determinant of the r1 matrix described in the maple section. The free algebra is essentially the non-commutative version of a polynomial ring. This is useful for defining variables in the dihedral group since they aren't commutative. 
3. Define a commutator function. When variables are passed to this function, and then included in our ideal generation later, we essentially are telling MAGMA "make these two variables commute with each other". The "z" function argument if equal to +1 will make the variables commute and if equal to -1 will make them anti-commute.
4. X and B are used as helpful sequences where we can define the relations between our variables and where we can call the commutator function. The following relations are the ones from the twisting: 
1. commutator_function(u1,u2,-1),commutator_function(v1,v2,-1)]
2. [commutator_function(u1,v2,1),commutator_function(u2,v1,1) 
5. R1:= 1 + a*u1 + b*u1^2 + c*u1^3 + d*v1 + e*v1*u1 + f*v1*u1^2 + g*v1*u1^3 is simply using the coefficients with each element of the dihedral group and adding 1. This is where we get our R1*R2*R1 for the YBE
6. NormalForm(R1*R2*R1-R2*R1*R2,I) is what we use for the YBE and thus we are trying to get this to be 0
### Running the MAGMA code 
1. Head over to the [MAGMA Calculator](http://magma.maths.usyd.edu.au/calc/)
2. Copy and paste the code from [here](https://github.com/HunterCharlesHewitt/TPQ-Research-Fall-2020/blob/main/magma_code/first_run_D4_twist.mag) into the box and hit submit
3. You should see a very long string of polynomials as output. We will need to copy and paste these into a text file, and use that text file as input for [this python program](https://github.com/HunterCharlesHewitt/TPQ-Research-Fall-2020/blob/main/simplify.py)
### Python Code 
1. Download [this python program](https://github.com/HunterCharlesHewitt/TPQ-Research-Fall-2020/blob/main/simplify.py)
2. Change the filename variable to be a string of the filename where you copied your MAGMA output, you can see that the file I used was called "D4_YBO_NoTwist_Output.txt"
3. Make sure the variable and coefficient lists match MAGMA's output, hence I used coefficients = \["a","b","c","d","e","f","g"\]
variables = \["u1","v1","u2","v2","u1^2","u2^2","v1^2","v2^2","u1^2","u2^2"\] since those were the variables and coefficients in my output. It is important that for the variables list it contains the generators for the group you are using (and also their squares, cubes, etc. is they show up in the output) and the coefficients are their coefficients in the definition for R1.
4. The final output after "COEFFICIENT SEQUENCE" will be what you can use in the MAPLE code
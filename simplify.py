#The purpose of this program is to strip coefficients off of polynomials received from MAGMA output

#uncomment for S3
coefficients = ["a","b","c","d","e"] #this list is the list of coefficients you are using
variables = ["u1","v1","u2","v2","v1^2","v2^2","u1^2","u2^2"] #this is the list of variables output by MAGMA, be sure to include squares if present
filename = "S3_YBO_1_Output.txt"

#uncomment for D4
# coefficients = ["a","b","c","d","e","f","g"]
# variables = ["r1","r2","m1","m2","r1^2","r2^2"]
#filename = "D4_YBO_NoTwist_Output.txt"

class Term:
  def __init__(self, isPositive, term):
    self.isPositive = isPositive
    terms = term.split("*")
    self.coefficient_term = ""
    self.variable_term = ""
    for i,term_var in enumerate(terms):
        print(term_var)
        if term_var in variables:
            self.variable_term += (term_var + "*")
        else:
            self.coefficient_term += (term_var + "*")
    
    self.coefficient_term = self.coefficient_term[:-1]
    self.variable_term = self.variable_term[:-1]    

def get_sign(isPositive):
    return "+" if isPositive else "-"
  

with open(filename, 'r') as file:
    expr = file.read().replace('\n', '')

add_split_terms = expr.replace('\n','').replace(' ','').split("+")
final_terms = []
for term in add_split_terms:
    neg_terms = term.split("-")
    final_terms.append(Term(True,neg_terms[0]))
    for i in range(1,len(neg_terms)):
        final_terms.append(Term(False,neg_terms[i]))
        

print("******* ORIGINAL TERMS ***********")
for i,term in enumerate(final_terms):
    print("{}: ({}{})({})".format(i,get_sign(term.isPositive),term.coefficient_term,term.variable_term))
i = 0
j = 0
while(i < len(final_terms)):
    j = 0
    while(j < len(final_terms)):
        if( i != j and (final_terms[i].variable_term == final_terms[j].variable_term)):
            sign = "+" if final_terms[j].isPositive else "-" 
            final_terms[i].coefficient_term += (sign + final_terms[j].coefficient_term)
            final_terms.pop(j)
        else:
            j += 1
    i += 1


print("\n******* GROUPING COEFFICIENTS ********")
for i,term in enumerate(final_terms):
    print("({}{}),".format(get_sign(term.isPositive),term.coefficient_term))

print("\n****** COEFFICIENT SEQUENCE ********")

print_str = "{"
for i,term in enumerate(final_terms):
    line = "{}{}".format(get_sign(term.isPositive),term.coefficient_term)
    if(len(line) > 0 and line[0] == "+"):
        line = line[1:]
    print_str += (line)
    if(i != len(final_terms)-1):
        print_str += (",\n")
print_str += "};"

print(print_str)
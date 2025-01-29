n = int(input("Enter  n: "))

var = n
fact_n = 1

for x in range(n):
    fact_n = fact_n * var
    var = var-1
    
print()





r = int(input("Enter  r: "))
var = r
fact_r = 1

for x in range(r):
    fact_r = fact_r * var
    var = var-1

print()




fact_nr = 1
hold = n-r
var = hold
for x in range(hold):
    fact_nr = fact_r * var
    var = var-1








porc = input("P or C : ")

print()
print()


if porc == "P":
    p = fact_n/fact_nr
    print("     Permutation of ", n , " and ", r, " is --> ", p )
    
elif porc == "C":
    c = fact_n/(fact_r * fact_nr)
    print("     Combination of ", n , " and ", r, " is --> ", c )

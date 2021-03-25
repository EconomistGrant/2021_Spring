# Recurrences
example: T(n) = 2T(n/2) + n^2
1. substitution: guess, substitute, see if it holds
2. recursion trees: draw a tree, sum work at each node
3. Master Theorem: general formula to solve recurrence
   
solving T(n) = a * T(n/b) + f(n):\

if f(n) >> $n^{log_b^a}$ -> root dominates\
if f(n) << $n^{log_b^a}$ -> leaves dominates\
o/w evenly split

T(n) = a * T(n/b) + $\theta(n^c)$  
case 1: c < $log_b^a$, T(n) = $\theta(n^{log_b^a})$\
case 2: c > $log_b^a$, T(n) = $\theta(n^c)$  \
case 3: c =  $log_b^a$, T(n) = $\theta(n^c * logn)$ essentially work at each level * height\



Notations: Omega, T, Theta, O
# Set Interface
interface vs implementation

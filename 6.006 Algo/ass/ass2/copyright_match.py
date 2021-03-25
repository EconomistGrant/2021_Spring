##################################################
##  Problem 2.4 TubeYou
##################################################
PRIME = 2 ** 31 - 1
def compute_mod(S, p):
    n = len(S)
    cur = 0
    for i in range(n):
        cur = (cur*128 + ord(S[i]))%p
    return cur

def copyright_match(T, S):
    """
    Input: T | an ASCII string 
    Input: S | an ASCII string where |S| < |T|
    
    Return `True` if S appears inside the transcript T and `False` otherwise.
    """
    f_prime = 1
    for i in range(len(S)):
        f_prime = (f_prime * 128) % PRIME
    
    if S == T[:len(S)]: 
        return True
    R_S = compute_mod(S,PRIME)
    R_T = compute_mod(T[:len(S)],PRIME)
        
    for i in range(len(T) - len(S)):
        R_T = (R_T*128 - ord(T[i])*f_prime + ord(T[i+len(S)])) % PRIME
        if R_T == R_S:
            if T[i+1:i+1+len(S)] == S:
                return True
    return False
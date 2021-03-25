import unittest

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

tests = (
    (
        (
            "Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark",
            "shark",
        ),
        True,
    ),

    (
        (
            "Who ever said money can't solve your problems, Must not have had enough money to solve 'em",
            "Who",
        ),
        True,
    ),

    (
        (
            "VVS my diamonds, I don't need no light to shine Iced out both my wrists, now I can barely see the time",
            "time",
        ),
        True,
    ),

    (
        (
            "There's one hundred and four days of summer vacation And school comes along just to end it",
            "Agent B",
        ),
        False,
    ),

    (
        (
            "Are you cheating on this code submission?",
            "u cheat",
        ),
        True,
    ),

    (
        (
            "sdiovsensriobnskbnseurnflvsuenvlijriodznvbfkurzks",
            "bnseurnflvsu",
        ),
        True,
    ),
    (
        (
            "dnwfgdosnionawiosnvioanviankrnbklsgjvilbnskrvbnklshznkjalhvanjksnksnsuinsleurhglukrngseg",
            "kxbndibfro",
        ),
        False,
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = copyright_match(*args)
    return staff_sol == student_sol


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))

    def test_06(self):
        self.assertTrue(check(tests[5]))

    def test_07(self):
        self.assertTrue(check(tests[6]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)

# SquareCB algorithm
get reward estimate f(x,a) from learning
assign p to each action based on f(x,a)
sample from p distribution
 - Inverse Gap Weighting(IGW): b as the best action
        p = 1 / (A + gamma (ft(x,b) - f(x,a))) -> normalize
        A = # actions
        gamma = learning rate

# Limits of Contextual Bandits
actions dont change the future -> REINFORCEMENT LEARNING!!!

# When to us RL
can be thought as finding the "shortest path"
online decisions; knowledge sythesis; control non linear systems; improve existing solutions

## sequential decision making
dynamic programming
principle of optimality, tail subproblems, Bellman

## Sequential Decision Making can get hairy
Shortest Tour (every city exactly once)
the curse of dimensionality

# Stochastic Problems
uncertainty in rewards, dynamics, horizon
Dynamic programming is insufficient

Goal: at = pai(s0:t, theta) policy
p(a|red); p(a|red,green) (previous two states)(data sparsity problem, if you conditioned too much states?)

markove assumption: 
st+1 = f(st, at)
at = pai (st; theta)
rt = g(st, at)
Markov Decision Process (MDP)

expand the state space to make any problem markov

Value function: expected sun of rewards, with discount factor gamma

## Tabular Setup
Bellman Equation

iterate until convergence
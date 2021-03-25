# overview of RL
xt -> policy -> at -> xt+1 , rt+1, max sum r
sequence of complex behaviors: red team killing blue, reward function very simple

how does this work?
reinforcement learning, bandits, contextual bandits...

starts with the most general way, RL!

# RL basics
state(s1, s2, ...)
- location / rotation of joint
- or, the image, or both

action(a1, a2,...)
torques on each joint

reward(r1,r2,...)
speed of cheetah

agent, action, environment, reward!

environmentn model: st+1 = f (s,a) mofrl based
policy: at = pai (s0:t;theta), model free methods

dataset generation: trajectories
supervised: dataset is given
exploration - exploitation dilemma: can learn sub-optimal behavior

spotify: want to recommend
explore lady gaga, but you hate her, so exploration is not a good idea...
robot failure is expensive so you dont want that also...

selling products: exploration is very important, as you want to find the best product

# Multi-arm bandits problem
return of ith arm: average return
goal: maximize reward over time

if deterministic: explore all and then choose

1: Explore-First for k rounds, and choose the best for the remaining T-k rounds

**Oracle**: sum of the best arm return...
how good I am compared with oracle? **regret** ||R* - R||
how fast we reach! 

online decision making: (compared with supervised learning) you dont have a data set, but you are creating a dataset 

2. Upper Confidence Bound (UCB) algorithm
Explore phase and Exploit phase
Explore phase: not using available info
Exploit and Explore simultaneously!

at+1 = argmax_i 

# contextual multi-arm bandits
how to make use of features in decision making? 
naive approach: independent bandit problems, categorical, no continous features 

LinUCB: expected rewards are linear in context
disjoint linear models: algorithm
cons: 
1. cannot share information across different features (theta)
2. new article, initialize

Homework one: UCB and linUCB

regularization term: some features are very small and not gonna work out, regularize to make sure the optimization is stable? "Feature Selection"


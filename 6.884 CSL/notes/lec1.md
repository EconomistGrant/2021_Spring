# introduction
Computational Sensorimotor Learning

Language models(gpt2/3): condense information from lots of text data
sometimes it may work...

but language models dont tell you to take potatoes out of the box or keep table clean

superhuman performance, atari, learn to dig a tunnel

# Atari as an example 
picture -> image encoder-> action predictor
cat -> image encoder -> class predictor

difference: 
1. someone tells you it is a cat or not: supervised learning
2. sequential nature, action affects future states

first robots: repeat human commands

self-learnt behavior  -------  hard coded behavior

## STRIPS Plan
how the system adapts to changing environment? stanford robots
hard-coding human intuition/decision making process, STRIPS Plan

## Physics models, trajectory optimization
Planning as search: tic tac toe game, limited discrete states
"planing actions": enumerate, simulate, choose best
Model-based control, min ||sT - SG|| ^ 2

limitation: predicting object motion is hard, same push will result in different motions...
block is not a stable surface, you cant measure the state of the system perfectly, things are not point mass, things that do matter in real world

model based methods are good as the specified models

system identification? mass friction shape, stiffness, simulate physics...

how to estimate parameters? computer vision, networks, very hard to predict from pixels

you cant find someone to label the friction....like labeling cats. Cant generate data

think about feather and stone falling, feeding in physics engine....

the bridge between computer vision and physics 

ENUMERATING ALL POSSIBLE CONDITIONS ARE HARD

Let the system determine what states/information to extract, end-to-end

forward model in pixel space
f(xt, at; theta_f), predict x_t+1
you want to focus on the object but your loss function might focus on predicting arm?

predicting location of glass when bottle falls

how to learn appropriate featrure space

## Intuitive Models
## Behavior Cloning (learning from demonstrations)
demonstration?

new task: trajectory transfer? some cases are non-trivial
how to generalize? self-supervised learning? 
limited by human performance?

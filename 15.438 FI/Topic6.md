# Continuous time models
BSM for interest rate options: shortcomings, majorly due to constant volatility

# Black's Model:
bond option
the option payoff depends only on the value of a variable at a particular time
assume the distribution at payoff-depending time is normally or log-normally distributed

Only forward price & strike price

estimate forward price: P = PV of coupons + PV of future

## For caps and floors
F = Forward rate covering period of caplet
X = rate cap

different volatility over different horizons

# One factor model in the short rate
dr = a(r,t)dt + b(r,t)dZ

## Vasicek Model
dr = a(b-r)dt + sigma dZ
parameters: b, a, sigma
strengths: rates are mean reverting

page 16

## CIR
dr = a(b-r)dt + sigma sqrt(r) dZ

weakness: does not capture yield curve dynamics
convex term structure?

higher vol: two models are really different


## Implementation of continuous time models: monte carlo
simulate short term rate paths -> implied term structure of interest rates -> price options on each path, and take average


## Black & Karasinski model
$d(\ln (r))=\phi(t)(\ln (\mu(t))-\ln (r)) d t+\sigma(t) d z$

# Multi-factor models
3 factors: level, slope, curvature
## multi-factor CIR
sum of several zi(t), each is a mean reverting square root process

## other models:
HJM: describing full instataneous yield curve
df(t,T)

Libor Market Model

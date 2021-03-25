# Risk Measurement for credit risk asset
Risky debt + guarantee of debt = risk free debt
risky debt = risk free debt - guarantee of debt

Assets = Bond + Equity
at exercise: guarantee = max[0,B-A]
Value of guarantee = put option on the assets of borrower

payoff of equity = call on firm, max[0,V-B]

value of debt as non-linear function of assets: option models, concave, approaching to full value as asset going to inf


# Payoff structure of debt with default risk
V(t) = D(t) + E(t)

if V <= M, D(t) = V, E(t) = 0
if V > M,  D(t) = M

dynamically replicate?
binomial model, look at slope of the bond and equity value? hold the same ratio?
kind of total slope = 0???(delta neutral)

# Relation Among asset, equity, and debt expected return
CAPM model, beta_V, beta_D, beta_E

w_D = beta_D/beta_V: essentially the shape you have using "option" model

expedted R_D = R_f + [beta_D/beta_V] [R_V-R_f]

# Promised Bond Yield and Credit Guarantee 

Expected return on equity: goes up with leverage but grows up slowier(flatter)
if straight line: all risk is in leverage, actually more risk is hold by equity holders

Expected return on asset remains constant! weight explains

Factors influence Debt and Equity value: look at black scholes model!
variance of firm value increase: D down and E up

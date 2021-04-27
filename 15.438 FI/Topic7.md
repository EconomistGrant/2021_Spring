# Credit Risk
Basics: corporate debt, statistics, loss drivers
understand and interpret credit spreads (technical)

IG: investment grade, 75%
HY: high yield, 18%

2020: a lot of corporate bond issurance
governments all over the world has been buying bonds
interest rate very low

foreign currency borrowing: exposed to exchange risk

# Coporate Debt
Collarteralization
Priority
Indentures and covenants? binding terms
skinding funds

## IG vs HY
HY: original issue vs fallen angels
strong historical return performance

## Default risk
downgrade risk
event risk: RJR Nabisco LBO, WPPSS(muni)
liquidity risk

default rate: pretty small

## recovery rate
page 14
bank loans: 80%+
senior secured bonds: 60-70%
senior unsecured: 50%
subordinated: 40%-

recovery rates low when default rates are high

# Credit spread
ytm - treasury bond of similar maturity

given credit rating: spread increase with maturity

## Decomposition of credit spreads
conceptually: 
1. expected losses
2. premium for market risk(beta)
3. liquidity premium
4. non credit features: tax, options

## credit spread puzzle: expected loss explains only a small proportion of historical spread
beta: -0.4 for AAA, -0.2 for AA, 0 for Baa, 0.3 for Ba, 0.5 for B... 

## Simple model
T, c, F = 1
assumptions: 
constant default risk each period, d
constant recovery rate g
$P=\sum_{i=1}^{T}\left((1-d)^{i-1} \frac{(d g(1+c)+(1-d) c)}{(1+r)^{i}}\right)+\frac{(1-d)^{T}}{(1+r)^{T}}$

## Hazard Model
models where default risk is described and valued as a put option

Merton/KMV model
risky zero coupon bond = long position in risk-free + short put option

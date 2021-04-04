# Topic 2: conceptual goals for this topic
duration and convexity (basic nad more advanced definitions)
delta/gamma hedge?
# Duration
p = f(y;other factors)
duration = partial f / partial y
convexity: second 

short-term yield more volatile than long-term

## fators affecing duration
remaining maturity: higher coupon, higher duration
coupon rate: higher coupon, lower duration
level of interest rate
credit risk, attched options

## Conceptual Definitions
Primary: duration is the elasticity of bond prices with respect to changes in yield
secondary: duration is the holding period horizon at which price risk and reinvestment risk approximately cancel

## Macauley 
D = (-dP/dY) * (1/P) *(1+Y/k)
third term: 1 + coupon rate 
derivation: simple taking derivative of Price
weighted average time

D = (1/k) * PVCF1 / PVTCF + (2/k) *PVCF2 / PVTCF ...
think about 1/k as "1/k yr away from first payment"...

For zero coupon option-free bond: duration = maturity

## Modified Duration
dPB / pB = MD
MD = D / (1+Y/k)

Duration is only good for small price change: 

## Dollar Duration
Dd = DM * Price
Portfolio duration: sum of dollar duration, weighted of modified duration

# Limitation of DUration measures
assume flat yield curve/parralel shifts
steepness/curvature shifts

# GEneralized Measures of Duration
total change in bond price as sum of partial effects
total derivative
??? factors are rates along the yiled curve? key rate durations?
## effective duration
true price sensitivity of the sucurity to changes in yield
from data?
smaller than modified duration when the cash flows are regarded as certain
# Interpretation of duration as a break even point for future value
accumulated value: reinvest coupon proceeds, plus liquidate (sell bond) value
start with 7%, if right after you buy rate > 4% and stay there
duration: the time that the accumulated value is about the same
algebra 

duration of IG credit index is near all time high
# Convexity and its properties
Calculating convexity: second derivative

convexity increases with squared maturity - duration is linear
duration approximation: slide along the tangent line
convexity is positive, a increase in rate -> duration decrease the price and convexity increase the price

negative convexity: second order reinforces first order change ...

dP / P = -D_M* dy + 1/2 C * (dy)^2

# Bullet and Barbell
Bullet: single payment?
Barbell: cash flows spaced in time

Bullets have a smaller convexity than barbells: barbells are better than bullets

portfolio manager is expected to do better if rates change with the barbell portfolio

think about two convex graph that tangent to each other at a point... any change makes barbell better!

# Immunization
"cash matching" + duration matching

use 20-year 7% coupon bond to immunize 10-year zero coupon 

reimmunize: sell the bond, rebalance to have a portfolio with new duration

# Delta and Gamma Hedging
Delta neutral: dollar duration of asset = liability
Gamma neutral: equates 

3 yr or 10 yr more convex? 10 yr, for the quadratic rule
If hedge - prefer the 3 yr
If long - prefer the 10 yr

immunization vs delta hedging: immunization includes PV matching


# The treasury market
$21.7 trillion public +  $6.1 trillion intragovernmental

Growth of fed balance sheet: growing to lower interest rate

fed: borrow short term and lend long term, carry, regard as profit?

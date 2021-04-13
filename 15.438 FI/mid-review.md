# Topic 1
## b.e.b vs Effective Annual Yields
assume return of y/2 every six months, y
effective: r = (1+y/2)^2 - 1

```py
RATE(nper = 10, pmt = 70, pv = -1300, fv = 1000) * 2
PV(rate = 0.04, nper = 20, pmt, fv)
PV(rate = 0.03, nper = 20, pmt)
```
## dirty vs clean price
quoted price: clean price, assume next coupon six months away
dirty price = clean + accrued interest

ACCRINT = [percent of time since last coupon payment] C
## Yield to first call
call option: issuer the right to repurchase at repurchase price
yield to fisrt call: assume issuer will excercise
yield to call < YTM <=> Q < F, "in money", will likely to exercise
yield to worst: lowest yeild
## Discount Securities vs Simple interest securities
DS: P = F(1 - d*t / 360) 
d: quoted discount rate

SI: P = F / (1+i*t/360)
i: quoted simple interest 

## Total Return Analysis
reinvest coupon, interest on interest
1. coupon interest + interest on interest = annuity calculation
2. coupon payment, interest on interest
3. capital gain? face value - par?
## Other concepts:
rise of SOFR, fall of LIBOR


# Topic 2
## Macauley, Modified
Macauley: weighted average of time, weights = PV
Modified: Macauley / (1+y/k) 

$D=\frac{\left(\frac{1}{k}\right) \times P V C F_{1}}{P V T C F}+\frac{\left(\frac{2}{k}\right) \times P V C F_{2}}{P V T C F}+\ldots+\frac{\left(\frac{T}{k}\right) \times P V C F_{T}}{P V T C F}$

effective: from data, true sensitivity
## interpretation: break even point
when different coupon bonds have the same value (page 25) 
## Convexity
good for holders with either direction of price change 

dP / P = -DM(dy) + 0.5 C (dy)^2

higher coupon rate -> higher convexity
## Strategies: Bullet, Barbell, Immunization, Hedge
bullet: single payment
barbell: spaced in time, higher convexity
immunization: MD + PV match
- once the rates shift, sell the bond and reimmunize
Delta and Gamma Hedge

# Topic 3
## Yield Curve models
1. Bootstrapping
one by one, nearest -> furthest
2. Nelson Siegal Model
$r(0, T)=\theta_{0}+\left(\theta_{1}+\theta_{2}\right) \frac{1-e^{-T / \lambda}}{T / \lambda}-\theta_{2} e^{-T / \lambda}$

Static: term structure
Dynamic: statistical distribution of yield curve at a time of future

## Implied forward rates
page 24
$\left(1+f_{1}(0, m, m+n)\right)=\left[\frac{\left(1+Y_{m+n}\right)^{m+n}}{\left(1+Y_{m}\right)^{m}}\right]^{1 / n}$
## Interpret y/c
1. market segmentation, preferred habitat
2. expectation hypothesis: forward rate = expected future spot rate
3. predicted business cycle conditions: y/c slop up at the start of expansion and slope down at end
4. liquidity preference theory: premium for long term
5. modified expectation hyop

## Inflation
TIPS: treasuty inflation protected securities
international yield curves?
covered: (1+R) = (1+R_foreign)/S * F, both side start with 1 dollar 
uncovered: E(S) instead of F

# Topic 4
## Forward
what, how much, when, price
p = f / (1+y)^t
pricing: directly discount / use forward rates (see page 11)
## RPs
short term bond with collateralized securities
borrower: sell securities to lender, agreed to buy back

reverse RP: "long" securities
**synthetic forward**: borrow money, buy bond, enter RP to borrow money with bond
t1: pay money, receive bond (same structure as forward)

## Future contracts
1. 3-month eurodollar deposites
each contract 1m fv, three monts deposits paying 90-day libor, quote 100 - i
1 basis = $25, rate up, quote down, long lose money
use of this: page 35

2. 3-month SOFR futures contract, backward looking, no term structure
3. US treasury bond futures contract
physically delivered, each contract for 100,000 face value of any 15-25 yrs bond
conversion factor
options: benefit sellers, cheapest to deliver: (maximizes settlement price * conversion factor - spot bond price)

## Durations of futures
duration of f(0,3,4): equivalent to long 4 year and short 3 year, both having same PV

#TODO: p47 example
## Swaps
fixed for floaing, long side = fixed rate payor, gain when rate going up
### Pricing
float bond always at par at reset dates
initialization: fixed rate is determined by setting swap PV 0
implementation: use LIBOR futures rates -> yeild -> price fixed rate
### Duration
fixed duration: trivial
floating duration: time until next reset / (1+Y/k)
## Use of Swap 
1. Maturity/duration restructuring
2. Forward rate agreement?
3. Hedge Balance Sheet Risk
nonperfect: page 25
4. Seeking better borrowing terms: relative advantage, trade
5. Speculation: 
- rising rate -> enter swap, shorten duration
- spread: long in undervalued, long <=> enter RP as lender to receive bond



# Quick Check
synthetic short: sample Q4 Q5

clean dirty price: ass1 Q1 Q2
simple vs discount Q3
Total returns Q5
Yield to first call Q6

forward rates Ass2 Q4
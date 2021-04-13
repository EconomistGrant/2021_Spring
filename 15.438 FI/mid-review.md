# Topic 1
## b.e.b vs Effective Annual Yields
assume return of y/2 every six months, y
effective: r = (1+y/2)^2 - 1
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
short term bond with collateralized seccurities 
## Future products

## Durations of futures

## Swaps

## Speculative Strategies
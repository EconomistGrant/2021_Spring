# Objectives:
primary: master fixed income analytics
secondary: familiar with major fixed income 

Midtern             30%
Final               45%
Assignment          20%
Homework Assignment 20%
Participation        5%

## Conceptual Goals
Cash Flows are fundamental, present values of future cfs
risk associated depends on investment horizon
## Acquired Skills

# Fixed Income status
outstanding in US, 45 trillion
insurance, 11.7 trillion in US 2020, huge in MBS

Global debt 215t, equity 73t
derivatives: 1 quadrillion

# Cash Flow basics
shared characteristics: promise a series of pre-specified payments at pre-determined points in time
Price                    P
Face Value               F
Coupon rate              c
Coupon payment           cF (cF/2 if semiannual)
Payment frequency        semiannual most commonly
Amortization schedule

options, default risk, etc... abstract for now

Yield to Maturity or IRR

Excel IRR

# Quotation Conventions
## APR
nominal rate, coupon payment = APR/# periods
## Bond Equivalent Yield
p = C1 / (1 + y/2) + C2 / (1+y/2)^2 + ...
assuming a return of y/2 every six months, and semiannual compounidng
## Effective Annual Yields, R
(1 + Y/2)^2 - 1
## Continuous basis, r
e^r = 1+R
## other conventions
quoted on a quarterly basis, but with semiannual payments
p = C1 / (1 + y/4)^2 + C2/(1+y/4)^4

Excel RATE(-Price, Periods, Payment, Face) = rate per payment
b.e.b. = rate*2

# Risk in the fixed income marketplace
interst rate risk
default risk
marketablitily/liquidity risk
timing/call risk
vol risk

# What happends when a bond is sold between coupon periods?
formula, coupon payment is split, clean price
dirty price = present value of the remaining cash flows
quoted/clean price = as if next coupon payment is 6 weeks away

clean price = dirty price - accrued interest
accured interest = (1-w)C, w = next coupon / coupon period 

# First Call
issuer the right to repurchase at a fixed price at a fixed date
yield to first call, assume the issuer will execise and calculate cfs and yield
yield to worst (lowest yield on all call prices)

if yield to call < ytm, essentially Q < F(or price at exercise time), in money, exercise
so its a conservative and better estimate of returns

quoted yield a sure thing: risk free, no default risk, hold until maturity

# Money Market
short term instruments, safe, liquid, shadow banking
auction market, OTC markets

spike up since 2019: Fed balance sheet expanding, reserve paying rate...

## Commercial Paper
Risks: price, default, liquidity(rollover)

## Discount Securities
P = F(1 - d*t / 360)
d: quoted discount rate
including treasury bills, bankers acceptancers, commercial papers, government agency issues
dollar discount = d*t*F/360

## Simple Interest Securities
P = F / (1+i*t/360)
i: quoted simple interest 
including CDs, Eurodollar Doposits, Municipal Securities(Munis), Fed Funds

## Developments:
Require marking to market for prime funds and limit liquidity if crisis
*picking up a few basis point but will be marked to market...*

## rise of SOFR, the fall of LIBOR.
Secured Overnight Funding Rate, based on market Repo rates
LIBOR: London Interbank Offer Rate, based on bank reported rates
LIBOR reporting will no longer be required after 2021

Repo means actual transaction rates
LIBOR: based on survey, incentive to lie(underreport rate) in crisis1
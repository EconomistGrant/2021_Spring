
# TOPIC 4: 
Part 1:  forward, futures, and RPs
1) Forward Contract
specifies a future transaction: what, quantity, when, price
2) forward rate
the rate(YTM) impled in a future contract

3) buyer: long position
4) hedge: reduces the risk
5) futures contract is a special kind of forward contract
standardized, subject to special rules, liquidity!

Forward price and spot price for bonds:
$$
P_{0}=F_{t} /\left(1+Y_{t}\right) t
$$

forward price approaching cash price
page 11 to see how the forward price is calculated
discount cash flows to the time of "delivery" using forward rate from delivery time to the cash flows

## Repurchase Agreements
short term loan
borrower: enter a repo
lender: reverse

fed: opposite vocabulary

borrower: sell(loan amount) securities to lender, and agreed to buy the same securities back from lender at a specified future date and price(face value)

lender can sell the sec! but she has to "return" at the specidied time

best sec: US treasury

"haircut"
> borrower risk: lender default and the security price gone up...

why there are episode that haircut is high and less liquid? could be regulation

### USE of RPs
short term borrowing and lending
invest short term idle cash
financing dealer inventories? obtainting 
obtaining securities to short!
>people paying money to lend cash in exchange for 10yr treasury to short the 10yr...

synthetic long position, page 26
borrow money in 6-month RP using 3.5 year zero coupon t bill
the bond is purchased with the borrowed money 0 cash flow

at 6 month: repay RP loan plus interst, receive the same bond

essentially: lock in future cash flows, delay cash to t1, and receive bond with maturity t2

## Future markets for fixed income securities
1. 3-month eurodollar depostis
2. 3-month SOFR futures
3. US treasury bond futures
all trade on chicago mercantile exchange

1. 3-month eurodollar depostis
each contract for 1mm fv, three month deposits paying the rate set in the futures contract
quoted on simple interest rate

"march contract"
![]"https://cdn.mathpix.com/snip/images/A6oA7hXK7HWGHzYfLB-hy_mZLYBcTftQK3ub7zPUIQM.original.fullsize.png"

everyday contracts are marked to marekt, and margin accounts are adjusted to reflect gain or loss
every basis change = $25 transfer (1m * 1% %1% *90/360)
long quoted at 97.35
if quotes go down, rate going up, long side losing money? (keep the same as bond)

bank afraid rate going up -> take short side to gain from that
January, commited to fund a lone in Sep, rate 5.85%
Take a short position
At september, rate 6.25%, additional gain is 40*25 = 1000
total proceeds: 1M + 1000 -> effective rate

2. 3-month SOFR futures contract
secured overnight financing rate
SOFR is backward looking geometric of overnight rates
no term structure, term premium, nor risk premium

low volume

3. US Treasury Bond Futres Contract
physically delivered
each contract is for 100,000 facr value of any 15-25 years maturity bond

Price = Quoted Price * Conversion factor(bond-specific) * 1000

options:
1) quality delivery option
2) delivery option
3) wildcard option

to the advantages of seller, so cheaper

## Duration of a Forward or Futures Contract
dollar duration: dP/dy = -Dm(P)
duration of security * prepaid forward price of the sec
prepaid forward price = present value of the forward price

one year bond delivered 3 years in future:
equivalued to long 4 year and short 3 year, both bond have the same current value

duration-based hedge





Topic 4 Part 2
Interest Rate Swaps
Speculative Strategies

# Interest Rate Swap
Vanilla: fixed for floating
long side = fixed rate payor
receive floating: gain when rate going up

# Swap pricing 
equivalent to long a fixed bond and short a floating bond (principle payment cancels outs)
traditionally priced using term structure for LIBOR

fact: floating rate bonds are always priced at par at reset dates (aassume no credit spreads)

at swap initialization: value zero - the fixed rate is determined by setting present value at par (par yield curve)
banks send out indication pricing schedules 

LIBOR yield curve <- euro dollar 

## Swap duration
effective duration of a floating rate bond = time until next rest / (1+Y/k)
what happens later will be adjusted

#TODO: how is floating rate bond "resets" practically? 
reset the interest rate (coupon paying rate) to be LIBOR


## Swap uses
1. Maturity or Duration Resructuring
switch from desired way of rate paying

reconstructure to be shoter term? long term liability -> pay fixed rates -> want to receive fixed payment, short side
why company want to do so?

2. Alternative to FRAs/Future contracts
FRA: commits one party to pay a preset forward rate in exchanged for realized one-period rate

3. Banks hegding balance sheet risk
Asset: long term mortgages
Liabilities: 3-month deposits + equity

duration does not match. Rate going up -> significant loss
interest rate swap to bring duration together
> in this case, they can pay fixed and receive floating to match liability

dont hedge long term with short term: parrallel shift is not that large?

### Not perfect hedge
1. mortgage amortized: principal balance declining
2. mortgage payments monthly, not semiannual
3. mortages can usually be prepaid

### Customized Swap Contracts
amortizing swaps(match amortization schedule)
basis swaps
swaptions

more expensive, more paperwork

### Swap use: better borrowing terms
a firm might have *relative* advantage in borrowing with one scheme, and use swap to achieve desired scheme (page 28)

page 32: maturity doesnot match, find a forward swap

# Basis risk
cash price and future price not move perfecctly?
cross hedge: hedge 9-month bond with 3-month contract
non-parallel shifts in interest curve

# Speculative Strategies
expect rate to rise:
shorten duration, short interest rate futures, enter swap as fixed rate payor, sell bond call, buy bond put

## Forward position using RPs
normal spread: 0.5, now 1
long AAA, short treasy

using RPs:
reverse RP with 18 months treasury as collateral
RP with 18 months corporate as collateral


1. remember you receive collateral
2. zero net cf
3. it is more commmon to rolling over shor term (overnight)

value of option: depend on the whole yield curve/dynamics
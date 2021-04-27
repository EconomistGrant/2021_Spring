1. Intro
2. Shortcomings of BSM
3. Pricing bonds using binomial approach
4. Deriving long-term yeilds from models of short terms
5. Pricing options using binomial
6. Calibrating binomial modesl with market price data

# Intro
American option / Euro option
call: negative convexity
put:  positive convexity

callable bond = bond - call option, less convexity
puttable bond = bond + put option, more convexity

# Pricing options on bonds with no-arbitrage logic
replicating portfolio

# Shortcoming of BSM:
page 12: as you look into future, vol of stock increase, but vol of bond increase and then decrease to zero at maturity
model interest rate instead

bond values is bounded (by the sum of CFs)

# Lattic model
evolution of the term structure over time when rates are stochastic

start with short rate -> ... -> calibrate step size and prob to match current price and volatility

d = sigma

pricing: backward calculation

more volatility: more downward sloping

# Binomial Interest Rate Tree -> callable / puttable bond
Callable: company can buy it back at a strike
Puttable: people who hold the bond can sell it to company at a strike


Callable Bond = Bond - Call option (benefit borrower)
Puttable Bond = Bond + Put option (benefit lender who owns the bond)

Pricing non-option bond:
at a specific node, value = discounted expectation of next time value + coupon payment
backward solve

pricing option: 
vanilla backward calculation

fair chance not to call because they still need to borrow

# Lattic Model calibration
1. observe current term structure
2. p_up = p_down = 0.5
3. r_H = r_L exp (2*sigma)        //two standard deviationm
degree of freedom: r0, r1, ...
Fit pirces...tree_fit...

# Muni Bond Market: 3.853 Trillion in US
Issued by state and local government 
coupon tax exempt, capital gains are not: R* = R/(1-T)

general obligation bonds / revenue bonds
Risk waries across issues


# PART 2
# Effective duration and effective convexity
$D_{\text {eff }}=\frac{1}{\text { price }_{\text {curent rate }}} \times \frac{\text { price }_{\text {rates fall }}-\text { price }_{\text {rate rise }}}{2 \mathrm{~s}}$

$C_{eff} = \frac{1}{\text { Price }} \times \frac{\left(\mathrm{P}_{\text {rates fall }}-\mathrm{P}_{\text {original }}\right)-\left(\mathrm{P}_{\text {original }}-\mathrm{P}_{\text {rates rise }}\right)}{(\mathrm{s})^{2}}$


model-dependent, not universal!

# Caps, Floors, Collar
cap: limit the maximum amount of interest paid
floor: limit the minimum amount of interest paid
collar: cap & floor

cap: strip of call option on interest payment

# Swaption
the option to swap
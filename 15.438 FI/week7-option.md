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

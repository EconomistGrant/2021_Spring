# Class 8: Measuring Performance of Systematic Dynamically Changing Risk Strategies: 
# Market Timing, Relative Value and Trend-Following Hedge Funds

if you dont know the risk, you dont know the excess return

# Measures:
Sharpe Ratio, ...

$M^{2}=E\left(R_{p *}\right)-E\left(R_{M}\right)$
with the same standard deviation

# Market Timing
Perfect market timing every month: 1927 - 1978, average annual return of 34.65%
you gotta be right twice
$$\begin{aligned} R_{p}-R_{f} &=\operatorname{Max}\left[O, R_{m}-R_{f}\right] \\ 
                              &=R_{m}-R_{f}+\operatorname{Max}\left[O, R_{f}-R_{m}\right] 
\end{aligned}$$

free call option on the market!\
value of timing is higher in high vol market

$R_{p}-R_{f}=a+b\left(R_{m}-R_{f}\right)+c \operatorname{Max}\left[O, R_{m}-R_{f}\right]+e_{p}$

is c statistically significant?

page 5 call return?
# Measure with call
hedge fund relative value strategy: 
higher return means better trade, if you believe your strategy
after making the pair trade: risk going down significantly because trades are done and no risk
risk level negatively correlated with return

if price going up/pisitive stock return: risk of call going down

$R_{p}-R_{f}=a+b\left(R_{m}-R_{f}\right)-c \text{Call Return} +e_{p}$

stop loss/momentum strategy: positive correlation with stock return

$R_{p}-R_{f}=a+b\left(R_{m}-R_{f}\right)+c \text{Call Return} +e_{p}$

structually the same!

# Measure with swaption
Perfect market timer: 
max[A,B] = A + max[0,B-A], return on A + a put option on A with striker price = B (not a constant!)
         = A{1 + max[0,B/A - 1]}, A as numeriare currency?

swaption: a call option on a swap contract with a strike price = 0         
payer = max[0,B-A]\
swaption model\
Value of exchange option at expiration $=\max \left\{0, V_{T}^{A}-V_{T}^{B}\right\}$
$$
\begin{array}{l}
\text { Value of Exchange Option }=\left(N\left(d_{1}^{\prime}\right) V_{0}^{\mathrm{A}}-N\left(d_{2}^{\prime}\right) V_{0}^{B}\right) =\left(N\left(d_{1}^{\prime}\right)-N\left(d_{2}^{\prime}\right)\right) \cdot V_{0} \\
\text { where } d_{1}^{\prime}=\frac{1}{\sigma^{\prime} \sqrt{T}}\left(\frac{\sigma^{\prime 2} T}{2}\right)=\frac{\sigma^{\prime} \sqrt{T}}{2} \text { and } d_{2}^{\prime}=d_{1}^{\prime}-\sigma^{\prime} \sqrt{T}=-\frac{\sigma^{\prime} \sqrt{\mathrm{T}}}{2}
\end{array}
$$
$\sigma^{\prime}=\sqrt{\sigma_{A}^{2}+\sigma_{B}^{2}-2 \rho \sigma_{A} \sigma_{B}}$

# Hedge Fund vs. CDP hedge fund
sell 30 day puts on SP, leverage
need to dig deep into the strategy, instead of looking at data

# Financial Service alpha
consider one single factor: no statistical significant alpha any more
financial service alpha



# Comparing Management Fee Expense: Performance vs. Fixed-Percentage AUM Fee
p = 20% above hurdle = 3% return on the portfolio over T = 1
$$
P F=p \times \operatorname{Max}\{0, V(T)-V(0) \exp [h T]\}
$$
call option!\
$$P F(V, T, V \exp (h), p \ldots)=p * C(S=V(0), T, K=V(0) \exp (h), \sigma, r, \delta=m)$$

you dont need to have expected return to valuate? not into the cost of the fund
dont need to agree on alpha...

>example: fund vol = 15%,risk free rate 5%, hurdle rate 0% -> 7.35% one year option price\
plus 2% AUM annual fee -> 2% + 0.2 * 7.35% = 3.47%

high watermark: 100 - 110 (fee) - 100 - 110 (no fee!)
hard to write in contract. Shut down the fund when drawdown

constant volatility implied in black scholes model
but you still need to tell your clients about anchored risk level?

## Performance fee relative to benchmark
V1 = fund value, V2 = bm value1
$$
P F(V_{1}, V_{2}, 0)=p * \max [0, V_{1}-\exp (h) V_{2}]\\
P F\left(V_{1}, V_{1}, T\right)=p \times C\left(V_{1}, T, K=V_{2} \exp (h), \sigma, r=0, \delta=0\right)\\
\sigma=\sqrt{\sigma_{1}^{2}+\sigma_{2}^{2}-2 \varphi \sigma_{1} \sigma_{2}}
$$
#TODO: How do you pass V2 to the function exactly?

## Different management fee sturctures
standard, with cap, convex, concave, squiggle
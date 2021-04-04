Type I vs Type II:
If null hypothesis is truly correct: type I error
If null hypothesis is wrong and you fail to reject: type II error
## Recall single test
$y_i = \beta_0 + \beta_1 x_{1i}$

$$H0: \beta_1 = 1$$

$$
\hat{\beta}_{1}-\beta_{1} \sim N\left(0, \hat{\sigma}_{1}^{2}\right)
$$

$$
\left|\frac{\hat{\beta}_{1}-1}{\hat{\sigma}_{1}}\right| \geq c=z_{1-\frac{\alpha}{2}}
$$

small sample size: t test

## Joint test
$$
H_{0}: \quad\left\{\begin{array}{l}
\beta_{1}=1 \\
\beta_{2}=0
\end{array}\right.
\\
\left[\begin{array}{c}
\hat{\beta}_{1}-1 \\
\hat{\beta}_{2}
\end{array}\right] \sim N(0, \hat{\Omega})

\qquad

\left[\begin{array}{c}
\hat{\beta}_{1}-1 \\
\hat{\beta}_{2}
\end{array}\right]^{\prime} \widehat{\Omega}^{-1}\left[\begin{array}{c}
\hat{\beta}_{1}-1 \\
\hat{\beta}_{2}
\end{array}\right] \sim \chi^{2}(2)$$


>recall that 
>$$
\begin{array}{l}
\hat{\beta}=\left(x^{\prime} x\right)^{-1} x^{\prime} Y \\
\beta-\beta \approx N\left(0, \sigma^{2}\left(x^{\prime} x\right)^{-1}\right)
\end{array}
>$$
>since we test beta1 and 2, we take the lower right 2*2 matrix as the omega matrix?


![](https://cdn.mathpix.com/snip/images/LqkC1_rZPuHM2seOVHsG0nyLpDnW8etxPAQKpX9qzjc.original.fullsize.png)

## Trade-off between type I and Type II
1. type I: null correct and you rejust, blue curve
at a specific point, beyond the test statistic: its highly unlikely that the null hypothesis is "truly" correct and you reject, which is type I error.
The blue shaded is what you allowed for type I error
2. Type II: the real beta is 5, you dont know, construct test as if the null. red curve
no rejection if falls between two blue bar: in this case, you might take type II error,  that the true case is red curve but you dont reject
p(type II error) = shaded red
making shaded blue smaller -> shaded red larger



## Economic Design of Hypo testing
Loss function L(m)
$$
\alpha^{*}(x)=\underset{\alpha}{\arg \min } p(m=I \mid x, \alpha) L(m=I)+p(m=I I \mid x, \alpha) L(m=I I)
$$

## Mini Case: Comparing Portfolio Managers
test the null hypothesis that having same Sharpe ratio
$$
H_{0}:\left\{\frac{\mu_{1}^{0}}{\sigma_{1}^{0}}-\frac{\mu_{2}^{0}}{\sigma_{2}^{0}}=0\right\}
$$

$$
h(\theta)=\frac{\mu_{1}}{\sigma_{1}}-\frac{\mu_{2}}{\sigma_{2}} \\
\widehat{A}=\left.\frac{\partial h(\theta)}{\partial \theta^{\prime}}\right|_{\widehat{\theta}}=\left
EE
(\begin{array}{cccc}
\frac{1}{\widehat{\sigma}_{1}} & -\frac{\widehat{\mu}_{1}}{\left(\widehat{\sigma}_{1}\right)^{2}} & -\frac{1}{\widehat{\sigma}_{2}} & \frac{\widehat{\mu}_{2}}{\left(\widehat{\sigma}_{2}\right)^{2}}
\end{array}\right)
$$

$$
\widehat{\operatorname{Var}}[h(\widehat{\theta})]=\left(\begin{array}{cccc}
\frac{1}{\widehat{\sigma}_{1}} & -\frac{\hat{\mu}_{1}}{\left(\widehat{\sigma}_{1}\right)^{2}} & -\frac{1}{\widehat{\sigma}_{2}} & \frac{\hat{\mu}_{2}}{\left(\widehat{\sigma}_{2}\right)^{2}}
\end{array}\right)[\widehat{\boldsymbol{\Omega}}]\left(\begin{array}{c}
\frac{1}{\widehat{\sigma}_{1}} \\
-\frac{\mu_{1}}{\left(\widehat{\sigma}_{1}\right)^{2}} \\
-\frac{1}{\widehat{\sigma}_{2}} \\
\frac{\mu_{2}}{\left(\widetilde{\sigma}_{2}\right)^{2}}
\end{array}\right)
$$

rejection criterion:
$$
\mathbb{A}=\left\{\left|\frac{h(\widehat{\theta})}{\sqrt{\widehat{\operatorname{Var}}[h(\hat{\theta})]}}\right| \geq z\right\}
$$

# Recitation
GMM has more assumptions? but best you can do given assumption right

estimating parameters: $\theta_p$
N dimensional (momentum) fuinction such that N >= P (overidentified)
minimize quadratic form of the sample mean of the moment condition $\hat{\theta}_{G M M}=\arg \min _{\theta} g_{T}(\theta)^{\prime} \hat{W} g_{T}(\theta)$

where g is 1 by N, W is N by N
W is the weighting matrix
if N = P, simply solve the equations! dont need to minimize

moment condition: E[f(x,theta)] = 0
finite sample: g function in page 9

先用GMM算四个参数的mean 和 covariance matrix V / Omega
再算A
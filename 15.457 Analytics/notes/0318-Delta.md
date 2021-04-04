# Pre-assumptions:

## Joint Normal
x is jointly normal: $x \sim \mathscr{N}(\mu, \Omega)$
Omega is the covariance matrix of x
#TODO how to estimate omega? in nature, $\Omega = E[xx^{\prime}]$

properties:
1. linear combinations of x: $A x \sim \mathscr{N}\left(A \mu, A \Omega A^{\prime}\right)$
2. $x \sim \mathscr{N}(0, \Omega) \Rightarrow x^{\prime} \Omega^{-1} x \sim \chi^{2}(\operatorname{dim}(x))$

## Derivatives

# Delta Method
derive the aymptotic distribution of a function on parameters:
$$
h(\widehat{\theta}) \approx h\left(\theta_{0}\right)+\left.\frac{\partial h(\theta)}{\partial \theta^{\prime}}\right|_{\theta_{0}}\left(\widehat{\theta}-\theta_{0}\right)
$$


$\widehat{\theta}-\theta_{0}$ is asymptotically normal, and multiplied by a linear combination: normal!

Define $A =\left.\frac{\partial h(\theta)}{\partial \theta^{\prime}}\right|_{\theta_{0}} \Rightarrow
h(\widehat{\theta})-h\left(\theta_{0}\right)  \sim \mathscr{N}\left(0, A \Omega A^{\prime}\right)$

Use consistent estimates:
$$\widehat{\Omega}?$$
Omega is the covariance matrix of the parameters -> going back to GMM to estimate
$\widehat{A}=\left.\frac{\partial h(0)}{\partial \theta^{\prime}}\right|_{\hat{\theta}} \Rightarrow h(\widehat{\theta})-h\left(\theta_{0}\right) \sim \mathscr{N}\left(0, \widehat{A} \widehat{\Omega} \widehat{A}^{\prime}\right)$

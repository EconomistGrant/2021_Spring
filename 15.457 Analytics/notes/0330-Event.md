# Where are "events"
corporate: mergers, acquisitions, splits, news patents
macro: macro annoucements
policy: bank regulation, FDA decisioins, SEC rulings
Natural: weather, epidemic, climate

Efficient reaction, overreaction and underreaction

# Challenges:
seperate price reactions to news from other unrelated movements?
how to test for significance？

# Anatomy
1. event definition and event window
2. selection criteria for firms/secs (market friction prevent information: penny stocks, illiquid)
3. model/estimate "normal" returns - abnormal returns
4. hypotest and interprete
   
stock split
post earnings annoucement drift(PEAD): maintain the same momentum as pre-earning-announcement
Index inclusion

Estimation Window + Underlying model
use the model to predict normal return in event window: normal return, abnormal return

Null Hypothesis: event does not change the distribution of abnormal returns
mean 0
variance: second moment

star: event window
no star: estimation window

# Methodology
## Simple Security
L1 = estimation window
L2 = event window
1. estimation: $R_{i, t}=x_{t}^{\prime} \theta_{i}+\varepsilon_{i, t}$
$$
\begin{aligned}
\widehat{\theta}_{i} &=\left(\mathbf{X}^{\prime} \mathbf{X}\right)^{-1} \mathbf{X}^{\prime} \mathbf{R}_{i} \\
\operatorname{Var}\left[\hat{\theta}_{i}\right] &=\widehat{\sigma}_{\varepsilon_{i}}^{2}\left(\mathbf{X}^{\prime} \mathbf{X}\right)^{-1} \\
\widehat{\varepsilon}_{i, t} &=R_{i, t}-x_{t}^{\prime} \widehat{\theta}_{i}, \quad \widehat{\sigma}_{\varepsilon_{i}}^{2}=\frac{\sum_{i} \widehat{\varepsilon}_{i, t}^{2}}{L_{1}-2}
\end{aligned}
$$

2. abnormal returns:$\widehat{\varepsilon}_{i}^{*}=\mathbf{R}_{i}^{*}-\mathbf{X}_{i}^{*} \widehat{\theta}_{i}$


$$
\begin{array}{c}
\widehat{\varepsilon}_{i}^{*} \sim \mathscr{N}\left(0, \mathbf{V}_{i}\right) \\
\mathbf{V}_{i}=\mathbf{I} \sigma_{\varepsilon_{i}}^{2}+\mathbf{X}_{i}^{*}\left(\mathbf{X}_{i}^{\prime} \mathbf{X}_{i}\right)^{-1} \mathbf{X}_{i}^{* \prime} \sigma_{\varepsilon_{i}}^{2} \\
\hline
\end{array}
$$
(proof in page 19)
non start x: from estimation window, star terms: from event window

3. Hypothesis Testing
$$
\widehat{S C A R}_{i}\left(\tau_{1}, \tau_{2}\right)=\frac{\widehat{C A R}_{i}\left(\tau_{1}, \tau_{2}\right)}{\widehat{\sigma}_{i}\left(\tau_{1}, \tau_{2}\right)}
$$
student t distribution with degrees of freedom L1 - 2

## Multiple secs/multiple events
$$
\bar{\varepsilon}^{*}=\frac{1}{N} \sum_{i=1}^{N} \widehat{\varepsilon}_{i}^{*}, \quad \operatorname{Var}\left[\bar{\varepsilon}^{*}\right]=\mathbf{V}=\frac{1}{N^{2}} \sum_{i=1}^{N} \mathbf{V}_{i}

\\

\overline{C A R}\left(\tau_{1}, \tau_{2}\right)=\gamma^{\prime} \bar{\varepsilon}^{*}

\\

\begin{array}{c}
\operatorname{Var}\left(\overline{C A R}\left(\tau_{1}, \tau_{2}\right)\right)=\bar{\sigma}^{2}\left(\tau_{1}, \tau_{2}\right)=\gamma^{\prime} \mathbf{V} \gamma 

\\
\overline{C A R}\left(\tau_{1}, \tau_{2}\right) \sim \mathscr{N}\left(0, \gamma^{\prime} \mathbf{V} \gamma\right)
\end{array}
$$

$$
\overline{S C A R}\left(\tau_{1}, \tau_{2}\right)=\frac{\overline{C A R}\left(\tau_{1}, \tau_{2}\right)}{\widehat{\bar{\sigma}}\left(\tau_{1}, \tau_{2}\right)}
$$
normal distribution


# Other interests
## 1 Heteroskedasticity / no mean change
we are assuming: the variance is different for event window and none-event window, but is the same across different events

Use cross-sectional variance of $\widehat{C A R}_{i}$
$$
\widehat{\operatorname{Var}}\left(\overline{C A R}\left(\tau_{1}, \tau_{2}\right)\right)=\frac{1}{N^{2}} \sum_{i=1}^{N}\left(\widehat{C A R}_{i}\left(\tau_{1}, \tau_{2}\right)-\overline{C A R}\left(\tau_{1}, \tau_{2}\right)\right)^{2}
$$
## 2 Clustering
Form a portfolio of simple average returns as one portfolio (perfect correlated)
## 3 Direct Regression
Is that only going to estimate the abnormal return on the event date?
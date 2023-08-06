
Introduction
------------

**Hatsya Hashboard** is a tool for estimating the profitability of bitcoin
mining ASICs.

The core of Hashboard is a **model-based simulator**, which rolls out many
(1250 by default) independent stochastic simulations of relevant variables
(including hashrate, difficulty, price, and block rewards) to obtain more
accurate estimates of the profitability of an ASIC.

This is used to update [this page](https://catagolue.hatsya.com/asics)
listing the available ASICs from [Compass Mining](https://compassmining.io/)
ordered in descending order of estimated probability of being profitable
over a five-year horizon.

Methodology
-----------

The salient ways in which Hashboard's methodology differs from other mining
calculators are summarised below:

 - **Uncertainty estimates**: predicting the future with certainty is
   impossible. By running many simulations, Hashboard obtains a distribution
   of outcomes instead of a single outcome, reflecting the uncertainty
   in the model.

 - **Joint distribution modelling**: it is often said that price drives
   hashrate, and hashrate drives price. Hashboard uses a **vector
   autoregressive (VAR)** model which jointly simulates these variables
   (and others such as transaction fees) together, rather than in isolation,
   for a more realistic simulation.

 - **Expressive model**: the VAR model is strictly more general than
   many approaches to modelling bitcoin's behaviour, including S2F(X),
   geometric Brownian motion, models with diminishing returns, and
   simple models based on technical and fundamental (on-chain) data. The
   model is trained on historic data (from Block 120960 to present) and
   minimises overfitting by incorporating a regularisation penalty that
   is optimised by cross-validation.

 - **Block time**: the simulator internally uses block height instead of
   wall-clock time, enabling the more accurate simulation of block subsidy
   halvings, difficulty adjustments, and computation of mining rewards.
   The simulator advances by steps of 48 blocks (an average of 8 hours)
   and treats wall-clock time as a dependent variable.

Moreover, Hashboard is free open-source software (MIT licenced), which
means that you can read and modify the source code. It is designed to
be modular and extensible, allowing you to add new data sources (such as
custom on-chain data) and customise the models.


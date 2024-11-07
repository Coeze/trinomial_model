# Trinomial Model Option Pricing in Python

This repository contains Python code to calculate the price of a European option (call or put) in a one-step trinomial model. The model uses closed-form expressions for risk-neutral probabilities and calculates the expected discounted payoff of the option.

## Files

- `main.py`: The main Python file with the function to compute the option price.
- `README.md`: Documentation explaining the code and usage.

## Overview

The trinomial model allows for three potential outcomes for the asset price in one time step:
1. The price can **go up** by a factor \( u \).
2. The price can **remain stable** (no change), represented by factor \( m = 1 \).
3. The price can **go down** by a factor \( d \).

The code calculates risk-neutral probabilities for these outcomes and uses them to determine the option's price.

### Risk-Neutral Probabilities

The code uses closed-form formulas for the risk-neutral probabilities:
1. **Middle Probability** \( p_m \):
   \[
   p_m = \frac{e^{r \Delta t} - d}{u - d}
   \]
2. **Up Probability** \( p_u \):
   \[
   p_u = \frac{m - d}{u - d} \cdot p_m
   \]
3. **Down Probability** \( p_d \):
   \[
   p_d = 1 - p_u - p_m
   \]

Where:
- \( u \), \( m \), and \( d \) are factors for price movement up, stable, and down.
- \( r \) is the risk-free interest rate.
- \( \Delta t \) is the time step.

## Code Usage

### Function

The `trinomial_option_price` function calculates the price of a European option.

#### Parameters
- `S0`: Initial asset price
- `K`: Strike price of the option
- `u`: Up factor
- `m`: Middle factor (should be 1 for the trinomial model)
- `d`: Down factor
- `r`: Risk-free interest rate
- `dt`: Time step size
- `option_type`: "call" for a call option, "put" for a put option

#### Example Usage

```python
# Parameters for the option and trinomial model
S0 = 100     # Initial stock price
K = 100      # Strike price
u = 1.1      # Up factor
m = 1.0      # Middle factor
d = 0.9      # Down factor
r = 0.05     # Risk-free rate
dt = 1       # Time step

# Calculate call option price
call_price = trinomial_option_price(S0, K, u, m, d, r, dt, option_type="call")
print("Call option price:", call_price)

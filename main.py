import math


def trinomial_option_price(S0, K, u, m, d, r, dt, option_type="call"):
    """
    Calculate the price of a European option in a one-step trinomial model.
    
    Parameters:
    - S0: Initial asset price
    - K: Strike price of the option
    - u: Up factor
    - m: Middle factor (should be 1 for trinomial model)
    - d: Down factor
    - r: Risk-free interest rate
    - dt: Time step size
    - option_type: "call" for a call option, "put" for a put option
    
    Returns:
    - Option price.
    """
    # Compute discount factor
    discount_factor = math.exp(-r * dt)
    
    # Calculate risk-neutral probabilities using closed-form expressions
    e_rt = math.exp(r * dt)
    p_m = (e_rt - d) / (u - d)
    p_u = (m - d) / (u - d) * p_m
    p_d = 1 - p_u - p_m
    
    # Calculate possible prices after one step
    S_u = S0 * u  # Price if asset goes up
    S_m = S0 * m  # Price if asset stays the same
    S_d = S0 * d  # Price if asset goes down
    
    # Calculate payoffs at each node
    if option_type == "call":
        payoff_u = max(S_u - K, 0)
        payoff_m = max(S_m - K, 0)
        payoff_d = max(S_d - K, 0)
    elif option_type == "put":
        payoff_u = max(K - S_u, 0)
        payoff_m = max(K - S_m, 0)
        payoff_d = max(K - S_d, 0)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    # Calculate the expected payoff under the risk-neutral measure
    expected_payoff = p_u * payoff_u + p_m * payoff_m + p_d * payoff_d
    
    # Discount the expected payoff to present value
    option_price = discount_factor * expected_payoff
    
    return option_price

# Example usage
S0 = 100     # Initial stock price
K = 100      # Strike price
u = 1.2      # Up factor
m = 1.0      # Middle factor (no change)
d = 0.8      # Down factor
r = 0.00     # Risk-free rate
dt = 1       # Time step

# Calculate option price
call_price = trinomial_option_price(S0, K, u, m, d, r, dt, option_type="call")
print("Call option price:", call_price)

def calculate_simple_interest(principal, rate, time):
    return principal * (1 + rate * time)

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def calculate_present_value(future_value, rate, time):
    return future_value / (1 + rate) ** time

def calculate_future_value(present_value, rate, time):
    return present_value * (1 + rate) ** time

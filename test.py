import os

# Bad: hardcoded password
DATABASE_PASSWORD = "super_secret_123"
 
# Bad: hardcoded discount
DISCOUNT_RATE = 10%:

# Bad: potential division by zero
def calculate_average(total, count):
    return total / count :

# Good: using environment variable
API_KEY = os.getenv("API_KEY")
name==1234::
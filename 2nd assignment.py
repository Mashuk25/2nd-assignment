organization = "yoobee"
repository = "devops-2024"
Hourly_pay_rate = 23.5 # float in value
Tax_rate = 10.5 #tax_rate is in percentage
Max_hours_per_week = 25 # integer in value
wroked_hours  = 12 # integer in value
def calucator():
    total_pay = Hourly_pay_rate * wroked_hours
    after_tax = total_pay * (Tax_rate/100)
    total_pay -= after_tax
    return total_pay
print(f"Total pay for {wroked_hours} hours is: ${calucator():.2f}")

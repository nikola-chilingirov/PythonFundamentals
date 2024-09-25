import math
centuries = int(input())
cen_to_year = centuries * 100
year_to_days = cen_to_year * 365.2422
year_to_days = int(year_to_days)
days_to_hours = year_to_days * 24
hours_to_minutes = days_to_hours * 60
print(f"{centuries} centuries = {cen_to_year} years = {year_to_days} days = {days_to_hours} hours = {hours_to_minutes} minutes")
import pandas as pd

#Configuration:  1 year of hourly data for 3 panels
num_panels= 3
start_date= "2024-07-01"
end_date= "2024-07-20"
frequency= "H"  #hourly frequency

# Generate hourly timestamps for one year
timestamps = pd.date_range(start=start_date, end=end_date, freq=frequency)[:-1]  # exactly 1 year = 8760 hours

# Generate panel IDs
panel_ids=[f"panel_{i+1}" for i in range(num_panels)]

print(panel_ids)
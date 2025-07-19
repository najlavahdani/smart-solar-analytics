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

# Generate weather condition column based on seasonal pattern:
# probabilities of different weather conditions per season
seasonal_weather_probs = {
    "Winter": {"snowy": 0.3, "cloudy": 0.4, "rainy": 0.2, "sunny": 0.1},
    "Spring": {"rainy": 0.3, "cloudy": 0.3, "sunny": 0.4},
    "Summer": {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.1},
    "Fall":   {"cloudy": 0.4, "rainy": 0.3, "sunny": 0.3}
}

# map each timestamp to a season
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"
    


#the dataset list
data = [
    {"timestamp": ts, "panel_id": pid} for ts in timestamps for pid in panel_ids   
]

#the base dataset: repeat each timestamp for each panel
base_data= pd.DataFrame(data) 

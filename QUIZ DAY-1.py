import pandas as pd

# Linking our data(csv file) with python using the given link
file_path = "https://raw.githubusercontent.com/Ranjit-Singh-786/laptop_pricePrediction/refs/heads/master/dataset/laptopPrice.csv"
data = pd.read_csv(file_path)

# Clearing the RAM column 
data['ram_gb_numeric'] = data['ram_gb'].str.replace(" GB", "").astype(int)

# Finding laptops which dont have 16GB of RAM.
laptops_16gb = data[data['ram_gb_numeric'] == 16]

# Checking if there are any laptops with 16GB RAM.
highest_price_16gb = laptops_16gb.loc[laptops_16gb['Price'].idxmax()] if not laptops_16gb.empty else "No laptops with 16GB RAM found"
print("1. Laptop with 16GB RAM and the highest price:\n", highest_price_16gb)

# Calculate the average price and find laptops price above the average
average_price = data['Price'].mean()
higher_than_avg = data[data['Price'] > average_price]
print("\nAverage Price:", average_price)
print("2. Number of laptops priced higher than the average:", len(higher_than_avg))

# Show how many laptops uses operating system.
print("\n3. Count of laptops by operating system:\n", data['os'].value_counts())

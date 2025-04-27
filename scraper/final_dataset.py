import csv
import os

# Updated restaurant details
restaurant_details = {
    'Chatori_Galli': {'Location': 'Lucknow, India', 'Operating Hours': '10 AM - 10 PM', 'Phone': '+91 9876543210', 'Special Features': 'Spicy, Vegetarian'},
    'Royal_Kitchen': {'Location': 'Indira Nagar', 'Operating Hours': '12 PM - 12 AM', 'Phone': '+91 8765432109', 'Special Features': 'Non-Veg, Spicy'},
    'Madras_Restaurant': {'Location': 'Hazratganj, Lucknow', 'Operating Hours': '11 AM - 11 PM', 'Phone': '+91 9998887777', 'Special Features': 'South Indian, Vegetarian'},
    'KFC': {'Location': 'Gomti Nagar, Lucknow', 'Operating Hours': '10 AM - 12 AM', 'Phone': '+91 9876543210', 'Special Features': 'Non-Veg, Fast Food'},
    'Terrace_Hotel': {'Location': 'Vishal Khand, Lucknow', 'Operating Hours': '9 AM - 9 PM', 'Phone': '+91 9988776655', 'Special Features': 'Vegetarian, Family Friendly'},
}

# Prepare output CSV
with open('Complete_Restaurant_Menu_Dataset.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Restaurant Name', 'Location', 'Menu Item', 'Veg/Non-Veg', 'Description', 'Cost', 'Rating', 'Special Features', 'Operating Hours', 'Phone Number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Read each restaurant file
    for restaurant_file in os.listdir('data'):
        if restaurant_file.endswith('.csv'):
            # Extract restaurant name properly
            restaurant_name = restaurant_file.replace('_products_extracted.csv', '')

            # Get corresponding manual details
            details = restaurant_details.get(restaurant_name, {})
            
            if not details:
                print(f"Warning: No manual details found for {restaurant_name}")

            with open(f'data/{restaurant_file}', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    writer.writerow({
                        'Restaurant Name': restaurant_name.replace('_', ' '),
                        'Location': details.get('Location', 'Not Available'),
                        'Menu Item': row['Product Name'],
                        'Veg/Non-Veg': row['Veg/Non-Veg'],
                        'Description': row['Description'],
                        'Cost': row['Cost'],
                        'Rating': row['Rating'],
                        'Special Features': details.get('Special Features', 'Not Available'),
                        'Operating Hours': details.get('Operating Hours', 'Not Available'),
                        'Phone Number': details.get('Phone', 'Not Available'),
                    })

print("✅ Complete dataset created successfully!")

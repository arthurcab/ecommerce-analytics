"""
This script generates fake customer data using the Faker library and saves it to a CSV file.

The generated customer data includes the following fields:
- id: Unique identifier for each customer.
- name: First name of the customer.
- last_name: Last name of the customer.
- email: Email address of the customer.
- registration_date: Date of customer registration.
- birth_date: Date of birth of the customer.
- street_address: Street address of the customer.
- city: City of the customer.
- state: State of the customer.
- prefered_device: Preferred device of the customer (Mobile, Desktop, or Tablet).
- email_opt_in: Boolean value indicating whether the customer has opted in for email communication.
- prefered_payment_methods: Preferred payment method of the customer (Credit Card, Paypal, Apple Pay, or Google Pay).
- gender: Gender of the customer (male or female).

Note: The Faker library is used to generate realistic fake data for testing and demonstration purposes.
"""

# Imports
import pandas as pd
from faker import Faker
import numpy as np 

# Create a Faker object
fake = Faker(use_weighting=True, locale='en_US', include_private=False)

# Set the seed
Faker.seed(4242)

# Generate customer data
customers = []
for _ in range(10000):
    customers.append({
        'id': fake.uuid4(),
        'name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'registration_date': fake.date_between(start_date='-5y', end_date='today'),
        'birth_date': fake.date_of_birth(minimum_age=18, maximum_age=65),
        'street_address': fake.street_address(),
        'city': fake.city(),
        'state': fake.state(),
        'prefered_device': fake.random_element(elements=('Mobile', 'Desktop', 'Tablet')),
        'email_opt_in': fake.boolean(chance_of_getting_true=40),
        # Make 'Credit Card' the most common payment method
        'prefered_payment_methods': fake.random_element(elements=('Credit Card' ,'Credit Card', 'Credit Card', 'Paypal', 'Apple Pay', 'Google Pay')),
        'gender': fake.random('male', 'female'),
        })

# Save the data to a DataFrame
customers_df = pd.DataFrame(customers)

# Generate sales data


if __name__ == '__main__':
    print('Customer data has been generated and saved to data/customers.csv')



    # Export the csv file 
    customers_df.to_csv('data/customers.csv', index=False)
    

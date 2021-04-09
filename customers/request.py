CUSTOMERS: [
    {
      "id": 1,
      "name": "Nathan Hamilton",
      "address": "0101 Hacker Ct",
      "email": "nate@nss.com",
      "password": ""
    },
    {
      "id": 2,
      "name": "Alexa Klein",
      "address": "1 Babes Way",
      "email": "babe@home.com",
      "password": ""
    },
    {
      "id": 3,
      "name": "Elliot Alderson",
      "address": "001 Mr. Robot Drive",
      "email": "",
      "password": ""
    },
    {
      "id": 4,
      "name": "Neo",
      "address": "1 Wall Street Court",
      "email": "",
      "password": ""
    }
  ]

  # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customerS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def get_all_customers():
    return CUSTOMERS
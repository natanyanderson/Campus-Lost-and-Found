"""
Project name : Campus Lost & Found
Team 1 - Natanya Anderson, Matthew Albuja, Demone Ball, Daniel Boateng
Due Date : 10/19/26
This is a Phase 1 prototype for Campus Lost & Found testing the core features. Campus Lost & Found allows users
to report a found item, search through found items reported, and show all items reported. The final version will be a web app.
"""

# Sample data for testing
water_bottle = {"name": "water bottle", "description": "pink 32oz owala with flower sticker",
                "date_found": "2026-10-18", "location": "classroom 42B", "claimed": False}
found_items = []
found_items.append(water_bottle)
found_items.append({"name": "calculator", "description": "texas instrument ti-84 plus ce",
                "date_found": "2026-09-05", "location": "classroom 307", "claimed": False})
found_items.append({"name": "id card", "description": "school id card with name stephanie lee",
                "date_found": "2026-11-17", "location": "3rd floor women's bathroom", "claimed": False})

while True:
    print("Type 1 to report a found item, 2 to search for found items, 3 to show all items, and 4 to Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        new_item_name = input("Name: ")
        new_item_description = input("Description: ")
        new_item_date = input("Date found (YYYY-MM-DD): ")
        new_item_location = input("Location: ")
        new_item = {"name": new_item_name, "description": new_item_description,
                    "date_found": new_item_date, "location": new_item_location, "claimed": False}
        found_items.append(new_item)
        print(f"Added {new_item_name}!")
        print(f"Total items: {len(found_items)}")
    elif choice == "2":
        keyword = input("Search for items: ").lower()
        match = False
        for item in found_items:
            if keyword in item["name"].lower() or keyword in item["description"].lower():
                match = True
                print(f"Found {item['name']}")
        if not match:
            print("No item found")
    elif choice == "3":
        for item in found_items:
            print(f"{item['name']} - found in {item['location']} and has description {item['description']}."
                  f" It was found on {item['date_found']} and has the claim status of {item['claimed']}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
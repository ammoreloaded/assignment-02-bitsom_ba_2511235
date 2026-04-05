import requests
from datetime import datetime

#-----------------------------------Task 1-----------------------------------
# Part A — Writing to a file


# Writing initial content. Create a file in same local directory
file = open("python_notes.txt", "w", encoding="utf-8")

file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
file.write("Topic 2: Lists are ordered and mutable.\n")
file.write("Topic 3: Dictionaries store key-value pairs.\n")
file.write("Topic 4: Loops automate repetitive tasks.\n")
file.write("Topic 5: Exception handling prevents crashes.\n")

file.close()

print("File written successfully.")


# adding more content to the File
file = open("python_notes.txt", "a", encoding="utf-8")

file.write("Topic 6: Functions help reuse code.\n")
file.write("Topic 7: Modules help organize programs.\n")

file.close()

print("Lines appended successfully.")



# Part B — Read. Reading from the same file created earlier


file = open("python_notes.txt", "r", encoding="utf-8")

lines = file.readlines()
file.close()

print("\nFile Content:\n")

# print numbered lines
count = 0
for line_item in lines:
    count += 1
    print(f"{count}. {line_item.strip()}")   # remove newline

# total number of lines
print("\nTotal lines:", count)



# Keyword Search


keyword = input("\nEnter keyword to search: ")

found = False

# Before searching ensure input and lines are in same case
for line_item in lines:
    if keyword.lower() in line_item.lower():
        print(line_item.strip())
        found = True

if not found:
    print("No matching lines found for the given keyword.")


#-----------------------------------Task 2-----------------------------------

BASE_URL = "https://dummyjson.com/products"


# Step 1 — Fire the API and Fetch and Display Products from the API response


try:
    #Limit to 20 to fetch first 20 records
    response = requests.get(f"{BASE_URL}?limit=20")
    response.raise_for_status()  # raises error if request fails

    data = response.json()
    products = data.get("products", [])

    print("\n===== Product List (Top 20) =====\n")
    print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<8} | {'Rating'}")
    print("-" * 80)

    for p in products:
        print(f"{p['id']:<4} | {p['title'][:30]:<30} | {p['category']:<15} | ${p['price']:<7} | {p['rating']}")

except requests.exceptions.RequestException as e:
    print("Error fetching products:", e)



# Step 2 — Filter and Sort
#Filtering products with rating of 4.5 or greater


try:
    filtered = [product for product in products if product["rating"] >= 4.5]
    sorted_products = sorted(filtered, key=lambda x: x["price"], reverse=True)

    print("\n===== Filtered (Rating ≥ 4.5) & Sorted by Price in Descending Order =====\n")

    for product in sorted_products:
        print(f"{product['title']} — ${product['price']} — Rating: {product['rating']}")

except Exception as e:
    print("Error processing products:", e)


# Step 3 — Search by Category (Laptops)


try:
    response = requests.get(f"{BASE_URL}/category/laptops")
    response.raise_for_status()

    data = response.json()
    laptops = data.get("products", [])

    print("\n===== Laptops Category =====\n")

    for p in laptops:
        print(f"{p['title']} — ${p['price']}")

except requests.exceptions.RequestException as e:
    print("Error fetching laptops:", e)



# Step 4 — POST Request (Simulated)


try:
    payload = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    response = requests.post(f"{BASE_URL}/add", json=payload)
    response.raise_for_status()

    print("\n===== POST Response =====\n")
    print(response.json())

except requests.exceptions.RequestException as e:
    print("Error in POST request:", e)


#-----------------------------------Task 3-----------------------------------


# Part A: Guarded Calculator

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


# Test cases
print(safe_divide(10, 2))      # Expected: 5.0
print(safe_divide(10, 0))      # Expected: Error
print(safe_divide("ten", 2))   # Expected: Error

# Part B: Guarded File Reader

def read_file_safe(filename):
    try:
        file_item = open(filename, "r", encoding="utf-8")
        content = file_item.read()
        file_item.close()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


# Test cases
print("\nReading python_notes.txt:")
print(read_file_safe("python_notes.txt"))

print("\nReading ghost_file.txt:")
print(read_file_safe("ghost_file.txt"))


# Part C: Robust API Calls

BASE_URL = "https://dummyjson.com/products"

def fetch_products():
    try:
        response_content = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        response_content.raise_for_status()
        return response_content.json()
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)


def fetch_laptops():
    try:
        response_content = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
        response_content.raise_for_status()
        return response_content.json()
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)


def create_product():
    try:
        payload_data = {
            "title": "My Custom Product",
            "price": 999,
            "category": "electronics",
            "description": "A product I created via API"
        }

        response_content = requests.post(f"{BASE_URL}/add", json=payload_data, timeout=5)
        response_content.raise_for_status()
        return response_content.json()

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)


# Example usage
print("\nFetching Products:")
print(fetch_products())

print("\nFetching Laptops:")
print(fetch_laptops())

print("\nCreating Product:")
print(create_product())



# Part D: Input Validation Loop
#Fire API by taking inputs from the User and display results if match found with that Product ID


while True:
    user_input = input("\nEnter a product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        print("Exiting program.")
        break

    # Validate integer
    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    product_id = int(user_input)

    # Validate range
    if product_id < 1 or product_id > 100:
        print("Please enter a number between 1 and 100.")
        continue

    # API call
    try:
        response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)

        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"{product['title']} — ${product['price']}")
        else:
            print("Unexpected response:", response.status_code)

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)


#-----------------------------------Task 4-----------------------------------

LOG_FILE = "error_log.txt"


# Logger Function
# A logger program that writes timestamp dates in a local error file generated in case of Exception or unexpected response

def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file_ops:
        file_ops.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")



# 1. Triggering ConnectionError

try:
    response = requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    print("Connection error triggered.")
    log_error("fetch_products", "ConnectionError", str(e))


# 2. Trigger HTTP Error (404)


try:
    product_id = 999
    response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)

    if response.status_code != 200:
        print("HTTP error triggered (product not found).")
        log_error(
            "lookup_product",
            "HTTPError",
            f"{response.status_code} Not Found for product ID {product_id}"
        )

except requests.exceptions.ConnectionError as e:
    log_error("lookup_product", "ConnectionError", str(e))
except requests.exceptions.Timeout as e:
    log_error("lookup_product", "Timeout", str(e))
except Exception as e:
    log_error("lookup_product", "Exception", str(e))



# 3. Read and Print Log File


print("\n===== Error Log Contents =====\n")

try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Log file not found.")
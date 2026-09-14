import json

DATA_FILE = "products.json"
def load_products():
    try:
        with open(DATA_FILE, "r") as file:
            products_list = json.load(file)

    except FileNotFoundError:
        print("File not found")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON data")
        return []

    if not isinstance(products_list, list):
        print("Invalid product data")
        return []

    return products_list
def save_all_products(products):
    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)
def validation(prompt,minimum):
   while True:
    try:
      product_value=int(input(prompt));
    except ValueError:

      print("Invalid ")
      continue
    if product_value<minimum:
        print("ENter the Vaid one")
    else:
      return product_value
def save_products(product):
    products = load_products()
    products.append(product)
    save_all_products(products)
def str_validation(prompt):
  while True:
    value=input(prompt)
    if value.strip()=='':
      print("Enter  string is invalid")
    else:
      return value
def add_products():
  prodlist=load_products()
  product_id=validation("Enter the ID:",1)
  if find_product(prodlist, product_id):
      print("Product is already Present")
      return

  product=create_product(product_id)
  save_products(product)
def view_products():
  productslist=load_products()
  print("========== PRODUCT LIST ==========")
  print("ID | Name | Category | Price | Quantity")
  for prod in productslist:
    print(f"{prod['id']} | {prod['name']} | {prod['category']} | {prod['price']} | {prod['quantity']}")
def find_product(products, product_id):
  for pro in products:
    if pro["id"]==product_id:
      return pro
  return None
def search_product():
  product_id=validation("Enter Valid ID:",1)
  prod=load_products()
  pro=find_product(prod, product_id)
  if not pro:
   print("Product Not Found")
  else:
    print("----Product Found----")
    print(f"ID = {pro['id']}\nName = {pro['name']}\nCategory = {pro['category']}\nPrice = {pro['price']}\nQuantity = {pro['quantity']}")
def update_product():
    product_id = validation("Enter the ID: ", 1)
    products = load_products()
    product = find_product(products, product_id)

    if not product:
        print("Product Not Found")
        return

    print("Current product:", product)
    temp_product = product.copy()
    update_product_details(temp_product)

    while True:
        choice = input(
            "Save Changes? (y/n): "
        ).lower()

        if choice not in ["y", "n"]:
            print("Invalid choice")
            continue

        break

    if choice == "y":
        product.update(temp_product)
        save_all_products(products)
        print("Product updated successfully")
    else:
        print("Product updation stopped")
def delete_product():
    product_id = validation("Enter the ID:", 1)
    products = load_products()

    product = find_product(products, product_id)

    if not product:
        print("Product Not Found")
        return

    print("----Product Found----")
    print(
    f"ID = {product['id']}\n"
    f"Name = {product['name']}\n"
    f"Category = {product['category']}\n"
    f"Price = {product['price']}\n"
    f"Quantity = {product['quantity']}")

    while True:
        choice = input(
            "Are you sure you want to delete this product? (y/n): "
        ).lower()

        if choice not in ["y", "n"]:
            print("Invalid choice")
            continue
        break

    if choice == "y":
        products.remove(product)
        save_all_products(products)
        print("Product Deleted")

    else:
        print("Product Deletion stopped")
def calculate_inventory_value():
  products=load_products()
  total_value=0
  print("========== INVENTORY VALUE ==========")
  for prod in products:
     value=prod["price"]*prod["quantity"]
     print(f"{prod['name']}   :   {prod['price']*prod['quantity']}")
  total_value=calculate_total_value(products)
  print("--------------\n Total :",total_value)
def low_stock_report():
  products=load_products()
  stock=False
  print("========== LOW STOCK REPORT ==========")
  for prod in get_low_stock_products(products):
      print(f"{prod['name']} : {prod['quantity']}")
      stock=True
  if not stock:
      print("No products are currently in low stock")
def menu():
 print("""========================================
       "INVENTORY MANAGEMENT SYSTEM
========================================""")
 while True:
  print("1. View Products 2. Add Product 3. Search Product 4. Update Product 5. Delete Product 6. Calculate Inventory Value 7. Low Stock Report 8. Exit\n")
  try:
   choice=int(input("Enter the choice: "))
  except ValueError:
     print("Invalid Choice")
     continue
  if choice==1:
    view_products()
  elif choice==2:
    add_products()
  elif choice==3:
    search_product()
  elif choice==4:
    update_product()
  elif choice==5:
    delete_product()
  elif choice==6:
    calculate_inventory_value()
  elif choice==7:
    low_stock_report()
  elif choice==8:
    print("Exitting")
    break
  else:
    print("ENter valid choice")
def create_product(product_id):
  product={"id":product_id ,"name":str_validation("Enter teh name:"),"category":str_validation("Enter the category:"),"price":validation("Enter the Price:",1),"quantity":validation("Enter the Quantity:",0)}
  return product
def update_product_details(prod):
  while True:
         print("What do you want to update?\n\n1. Name\n2. Category\n3. Price\n4. Quantity\n5. Finish Editing")
         try:
          choice=int(input("What you want to update:"))
         except ValueError:
            print("Invalid choice")
            continue
         if choice==1:
          name=str_validation("Enter the name:")
          prod["name"]=name
         elif choice==2:
          category=str_validation("Enter the category:")
          prod["category"]=category
         elif choice==3:
          price=validation("Enter the Price:",1)
          prod["price"]=price
         elif choice==4:
          qty=validation("Enter the Quantity:",0)
          prod["quantity"]=qty
         elif choice==5:
          break
         else:
           print("Invalid choice")
def get_low_stock_products(products, limit=10):
    low_stock_products = []

    for product in products:
        if product["quantity"] < limit:
            low_stock_products.append(product)

    return low_stock_products
def calculate_total_value(products):
    total_value = 0

    for product in products:
        total_value += product["price"] * product["quantity"]

    return total_value
           
if __name__ == "__main__":
  menu()
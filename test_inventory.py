import unittest
import json
import os
import inventory_management
from inventory_management import find_product, load_products, save_products, save_all_products
from inventory_management import find_product
from inventory_management import find_product, load_products
from inventory_management import find_product, load_products, save_products
from inventory_management import find_product,load_products,save_products,save_all_products,calculate_total_value, get_low_stock_products

class TestFindProduct(unittest.TestCase):
  def test_invalid_json(self):
    inventory_management.DATA_FILE = "invalid_products.json"

    with open("invalid_products.json", "w") as file:
        file.write("this is not valid json")

    products = load_products()

    self.assertEqual(products, [])
    os.remove("invalid_products.json")
  def test_missing_file(self):
    inventory_management.DATA_FILE = "missing_products.json"

    if os.path.exists("missing_products.json"):
        os.remove("missing_products.json")

    products = load_products()

    self.assertEqual(products, [])
  def test_low_stock_products(self):
    products = [
        {
            "id": 101,
            "name": "Keyboard",
            "category": "Electronics",
            "price": 1200,
            "quantity": 9
        },
        {
            "id": 102,
            "name": "Mouse",
            "category": "Electronics",
            "price": 600,
            "quantity": 10
        },
        {
            "id": 103,
            "name": "Monitor",
            "category": "Electronics",
            "price": 8500,
            "quantity": 5
        }
    ]

    result = get_low_stock_products(products)

    self.assertEqual(len(result), 2)
    self.assertEqual(result[0]["id"], 101)
    self.assertEqual(result[1]["id"], 103)
  def test_delete_product(self):
    products = load_products()

    product = find_product(products, 101)

    self.assertIsNotNone(product)

    products.remove(product)
    save_all_products(products)

    loaded_products = load_products()

    deleted_product = find_product(loaded_products, 101)

    self.assertIsNone(deleted_product)
  def setUp(self):
    inventory_management.DATA_FILE = "test_products.json"

    test_data = [
        {
            "id": 101,
            "name": "Keyboard",
            "category": "Electronics",
            "price": 1200,
            "quantity": 10
        }
    ]

    with open("test_products.json", "w") as file:
        json.dump(test_data, file, indent=4)
  def test_update_product(self):
    products = [
        {
            "id": 101,
            "name": "Keyboard",
            "category": "Electronics",
            "price": 1200,
            "quantity": 10
        }
    ]

    product = find_product(products, 101)

    product["price"] = 1500

    save_all_products(products)

    loaded_products = load_products()

    updated_product = find_product(loaded_products, 101)

    self.assertIsNotNone(updated_product)
    self.assertEqual(updated_product["price"], 1500)
  def test_save_product(self):
    product = {
        "id": 999,
        "name": "Test Product",
        "category": "Testing",
        "price": 100,
        "quantity": 5
    }

    before = load_products()

    save_products(product)

    after = load_products()

    self.assertEqual(len(after), len(before) + 1)

    saved_product = find_product(after, 999)

    self.assertIsNotNone(saved_product)
    self.assertEqual(saved_product["name"], "Test Product")
  def test_load_products(self):
    products = load_products()

    self.assertIsInstance(products, list)
    self.assertGreater(len(products), 0)
  def test_existing_product(self):
        products = [
            {
                "id": 101,
                "name": "Keyboard",
                "category": "Electronics",
                "price": 1200,
                "quantity": 10
            }
        ]

        result = find_product(products, 101)

        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Keyboard")

  def test_product_not_found(self):
        products = [
            {
                "id": 101,
                "name": "Keyboard",
                "category": "Electronics",
                "price": 1200,
                "quantity": 10
            }
        ]

        result = find_product(products, 999)

        self.assertIsNone(result)
  def test_calculate_total_value(self):
    products = [
        {
            "id": 101,
            "name": "Keyboard",
            "category": "Electronics",
            "price": 1200,
            "quantity": 10
        },
        {
            "id": 102,
            "name": "Mouse",
            "category": "Electronics",
            "price": 600,
            "quantity": 5
        }
    ]

    result = calculate_total_value(products)

    self.assertEqual(result, 15000)

if __name__ == "__main__":
    unittest.main()
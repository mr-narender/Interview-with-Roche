# 📦 Interview with Roche — Product Inventory API

A simple Django RESTful API to create and list product inventory entries. This API was built for an interview assignment for roche.

---

## 🚀 Features

- **WRITE Endpoint**: Create a new product by sending `product_name`, `price`, and `quantity`.
- **READ Endpoint**: List all products in JSON format.
- **Validation**: Strong input validation with proper error messages.
- **Error Handling**: Returns structured JSON responses with appropriate HTTP status codes.
- **Tests**: Unit tests to verify core functionality.

---

## 📋 Requirements

- Python 3.13+
- pip or uv ( I have used uv but either can work)

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/interview-with-roche.git
cd interview-with-roche

# Create virtual environment
uv venv .venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
uv add django djangorestframework
OR
uv pip install .
```

## 🧪 Running the Project

```bash
# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

API will be available at: http://localhost:8000/api/products/

## 🔗 Example API Usage

### ✅ POST (Create a Product)

```bash
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"product_name": "Monitor", "price": 300, "quantity": 80}'
```

## 📥 GET (List Products)

```bash
curl http://localhost:8000/api/products/
```

### returns

```json
{
  "1": {
    "product_name": "Monitor",
    "price": 300.0,
    "quantity": 80
  }
}
```

## 🧪 Running Tests

```bash
python manage.py test inventory

Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK
Destroying test database for alias 'default'...
```

## Snowflake Connector

Repective depdencies should be installed automatically when creating virtualenv, however some configuaration needs tweaking.

To do that, please Open your settings.py file and locate the DATABASES configuration. Replace it with the respective Snowflake-specific settings as needed.

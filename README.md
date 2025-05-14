````markdown
# 🧠 SQL Table Extractor

A lightweight Python utility to extract unique table names from raw SQL queries using regular expressions. Ideal for static SQL analysis, metadata exploration, and quick audits.

## 📌 Features

- Removes inline and block comments
- Handles `FROM` and `JOIN` clauses
- Skips SQL keywords and aliases
- Returns **unique** table names
- Minimal dependencies

## 🚀 Usage

```bash
python find_tables.py
````

## 🧪 Example

Given the following SQL query:

```sql
SELECT e.employee_id, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
UNION
SELECT customer_id, order_id
FROM archived_orders;
```

The script will output:

```
Tables found:
- archived_orders
- departments
- employees
```

## 📂 File Structure

```
.
├── find_tables.py
└── README.md
```
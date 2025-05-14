import re

def find_tables(sql_query: str) -> list:
    """
    Extracts distinct table names from a given SQL query.

    Args:
        sql_query (str): A raw SQL query string.

    Returns:
        list: A list of unique table names used in FROM or JOIN clauses.
    """
    # Remove SQL comments (both inline and block comments)
    sql_query = re.sub(r"/\*.*?\*/", "", sql_query, flags=re.DOTALL)  # block comments
    sql_query = re.sub(r"--.*?$", "", sql_query, flags=re.MULTILINE)  # inline comments

    # Normalize spacing
    sql_query = re.sub(r"\s+", " ", sql_query)

    # Tokenize
    tokens = sql_query.split()

    # Keywords that usually indicate non-table names after FROM or JOIN
    stop_keywords = {
        'select', 'where', 'group', 'order', 'having', 'limit', 'offset',
        'on', 'and', 'or', 'as', 'case', 'when', 'then', 'else', 'end',
        'left', 'right', 'inner', 'outer', 'full', 'cross', 'union'
    }

    # Extract potential table names
    tables = set()
    for i, token in enumerate(tokens):
        if token.lower() in ('from', 'join'):
            # Look ahead to get the next token (potential table name)
            if i + 1 < len(tokens):
                next_token = tokens[i + 1].strip().lower()
                # Skip subqueries or keywords
                if next_token not in stop_keywords and next_token != '(':
                    # Remove trailing comma or semicolon
                    table = re.sub(r"[;,]", "", tokens[i + 1])
                    tables.add(table)

    return sorted(tables)


# Example usage
if __name__ == "__main__":
    sql_query = """
    -- Sample SQL query to test table extraction
    SELECT e.employee_id, e.first_name, d.department_name, l.city
    FROM dbo.employees e
    JOIN dbo.departments d ON e.department_id = d.department_id
    LEFT JOIN locations l ON d.location_id = l.location_id
    WHERE e.salary > 50000
    ORDER BY e.last_name;

    -- Another example with UNION
    SELECT customer_id, order_id
    FROM prd.orders
    WHERE order_date >= '2023-01-01'
    UNION
    SELECT customer_id, order_id
    FROM archived_orders
    WHERE order_date >= '2023-01-01';

    """
    
    result = find_tables(sql_query)
    print("Tables found:")
    for table in result:
        print("-", table)

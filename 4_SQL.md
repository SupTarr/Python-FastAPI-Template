# SQL commands

| id: (Serial + Primary Key) | name: Character varying(50) | price: Numeric(10, 2) | is_sale: Boolean | inventory: Integer | created_at: (Timestamp) |
| :------------------------: | :-------------------------: | :-------------------: | :--------------: | :----------------: | :---------------------: |
|             1              |         "Product A"         |         49.99         |       true       |        100         |  "2022-03-23 12:00:00"  |
|             2              |         "Product B"         |         19.99         |      false       |         50         |  "2022-03-22 10:30:00"  |
|             3              |         "Product C"         |         89.99         |       true       |         25         |  "2022-03-20 14:15:00"  |
|             4              |         "Product D"         |         59.99         |      false       |         75         |  "2022-03-18 16:45:00"  |

```SQL
SELECT * FROM products;
-- SELECT all-columns FROM table-name
```

```SQL
SELECT id, name, is_sale FROM products;
-- SELECT some-columns FROM table-name
```

```SQL
SELECT id AS product_id FROM products;
-- SELECT column AS new-column-name FROM table-name
```

```SQL
SELECT * FROM products WHERE id = 10;
SELECT * FROM products WHERE inventory = 0;
SELECT * FROM products WHERE price > 50;
-- SELECT * FROM table-name WHERE condition
```

```SQL
SELECT * FROM products WHERE inventory != 0;
SELECT * FROM products WHERE inventory <> 0;
-- SELECT * FROM table-name WHERE not-equal

SELECT * FROM products WHERE inventory <> 0 AND price > 20;
SELECT * FROM products WHERE inventory <> 0 OR price < 20;
```

```SQL
SELECT * FROM products WHERE id IN (1, 2, 3);
```

```SQL
SELECT * FROM products WHERE name LIKE 'TV%';
-- SELECT * FROM table-name WHERE {condition of name that start with TV}

SELECT * FROM products WHERE name LIKE '%e';
-- SELECT * FROM table-name WHERE {condition of name that end with TV}

SELECT * FROM products WHERE name LIKE '%en%';
-- SELECT * FROM table-name WHERE {condition of name that contain TV}
```

```SQL
SELECT * FROM products ORDER BY price ASC;
SELECT * FROM products ORDER BY price DESC;

SELECT * FROM products ORDER BY inventory DESC, price;

SELECT * FROM products WHERE price > 20 ORDER BY created_at DESC;
```

```SQL
SELECT * FROM products LIMIT 10;
SELECT * FROM products WHERE price > 10 LIMIT 3;
SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 2;
-- OFFSET is useful for pagination.
```

```SQL
INSERT INTO products (name, price, is_sale, inventory, created_at)
VALUES
  ('Product A', 49.99, true, 100, '2022-03-23 12:00:00'),
  ('Product B', 19.99, false, 50, '2022-03-22 10:30:00'),
  ('Product C', 89.99, true, 25, '2022-03-20 14:15:00'),
  ('Product D', 59.99, false, 75, '2022-03-18 16:45:00')
RETURNING *;
```

```SQL
DELETE FROM products WHERE id = 10 RETURNING *;
```

```SQL
UPDATE products SET name = 'Product E', price = 50.99 WHERE id = 10 RETURNING *;
```

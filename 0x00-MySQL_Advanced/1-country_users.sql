-- creates a users table if it doesn't exist
-- if it does, this script should not fail
DROP TABLE IF EXISTS users;

CREATE TABLE
  IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
  );
include .env
export

define CREATE_DB_SCRIPT
USE recommendations; \
CREATE TABLE IF NOT EXISTS products ( \
  product_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, \
  product_name varchar(255) NOT NULL, \
  product_slug varchar(255) NOT NULL \
); \
CREATE TABLE IF NOT EXISTS rules ( \
  rule_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, \
  recommended_product_id int(11) NOT NULL \
); \
CREATE TABLE IF NOT EXISTS rule_products ( \
  rule_product_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, \
  product_id int(11) NOT NULL, \
  rule_id int(11) NOT NULL \
); \
ALTER TABLE rules \
ADD FOREIGN KEY (recommended_product_id) REFERENCES products(product_id); \
ALTER TABLE rule_products \
ADD FOREIGN KEY (product_id) REFERENCES products(product_id); \
ALTER TABLE rule_products \
ADD FOREIGN KEY (rule_id) REFERENCES rules(rule_id);
endef

setup-db:
	@echo "Setting up database..."
	docker-compose exec maria-db bash -c 'mysql -u $(DB_USER) -e "$(CREATE_DB_SCRIPT)" -p'

run:
	docker run --rm -ti -v ${PWD}:/app -w /app --network=simple-recommendation_default python:3.7-slim \
    bash -c "/usr/local/bin/pip install -r /app/requirements.txt; python main.py"

include .env
export

define CREATE_DB_SCRIPT
USE recommendations; \
CREATE TABLE IF NOT EXISTS rules ( \
  rule_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, \
  rule_key varchar(255) NOT NULL, \
  recommended_product varchar(255) NOT NULL \
);
endef

setup-db:
	@echo "Setting up database..."
	docker-compose exec maria-db bash -c 'mysql -u $(DB_USER) -e "$(CREATE_DB_SCRIPT)" -p'

run:
	docker run --rm -ti -v ${PWD}:/app -w /app --network=simple-recommendations_default python:3.7-slim \
    bash -c "/usr/local/bin/pip install -r /app/requirements.txt; python main.py"

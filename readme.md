## Simple Recommendations

Recommends products based on previously defined rules

## Usage

### Creating rules

You will be prompted for 2 inputs:

- product list (separated by '|')
- recommended product

This will create an entry in the database with the provided parameters.
ex:

```
# product_list: milk|flour
# recommended_product: sugar
# will generate the following db row:

| rule_id | rule_key    | recommended_product |
|---------+-------------+---------------------|
|  xxxxx  | flour__milk | Sugar               |
```

_The inputs will be cleaned up before saving/querying, so it is not case sensitive. Product lists get converted into a 'rule_key' (trimmed, sorted, slugified, and concatenated), and recommended products get "prettified"_

### Listing rules:

Gets and prints all rules from the database, the user is then given the option to delete any rules. ex:

```
id: 3 - Product List: ['Honey', 'Milk', 'Sugar'] | Recommended Product: Egg
id: 4 - Product List: ['Honey', 'Sugar'] | Recommended Product: Ice Tea
id: 8 - Product List: ['Flour', 'Milk'] | Recommended Product: Sugar
Do you want to delete any rules? [y/N]:
```

If the input is `y`, the user is prompted for the ids he wishes to delete.

```
Enter the ids to delete separated by spaces (i.e: 10 20 40):
```

### Getting recommendations

The user is prompted for a list of products:

```
Enter product list separated by '|' (i.e: sugar | honey | ice tea): honey|sugar|milk
```

Then, every possible rule_key is generated from the provided list, for our example that would be:

```
'honey', 'sugar', 'milk', 'honey__sugar', 'honey__milk', 'milk__sugar', 'honey__milk__sugar'
```

We use all these `rule_keys` to query the database, returning all matching rules. Finally we compare the `recommended_products` to the provided `product_list`, ensuring we return only products not present in the list.

## Setup

### Application Setup

1 - Install requirements:

```bash
$ python3 -m pip install -r requirements.txt
```

### DB Setup

1 - Setup .env

```bash
$ cp .env.sample .env
```

Default values are setup to work with the provided docker-compose file, if you're using a different database you need to tweak these values manually

```
DB_ENDPOINT=localhost:3306
DB_USER=dba
DB_PASS=dba
DB_NAME=recommendations
```

2 - Bring database up:

```bash
$ docker-compose up
```

3 - Create DB/Table:

```bash
$ make db-setup
```

SQL for manual setup:

```sql
CREATE DATABASE `recommendations` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE recommendations;

-- recommendations.rules definition

CREATE TABLE `rules` (
  `rule_id` int(11) NOT NULL AUTO_INCREMENT,
  `rule_key` varchar(255) NOT NULL,
  `recommended_product` varchar(255) NOT NULL,
  PRIMARY KEY (`rule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
```

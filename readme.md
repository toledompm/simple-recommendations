## Simple Recommendations

Recommends products based on apriori algorithm.

#### Analysis repo

https://github.com/jasondavindev/ml-apriori-recommendation

## Usage

### Getting recommendations

The user is prompted for a list of products:

```
Enter product list separated by '|' (i.e: sugar | honey | ice tea): honey|sugar
```

For each product on the list, it will be created if it not exist in the database. Then the apriori algorithm will run and return a recommended product list or none.

Example

```text
  1- inform the cart
  2- exit

Enter your choice: 1
Enter product list separated by '|' (i.e: sugar | honey | ice tea): a|b
Recommended products: None
Press Enter to continue...

  1- inform the cart
  2- exit

Enter your choice: 1
Enter product list separated by '|' (i.e: sugar | honey | ice tea): a
Recommended products: B
Press Enter to continue...
```

## Setup (docker)

Clone the `.env.sample` file to `.env` and set the variable values.

```bash
cp .env.sample .env
```

### Database setup

Turn on database container using docker-compose file

```bash
docker-compose up
```

Run `setup-db` make command and put database password (`dba` as user and password)

```bash
make setup-db
```

### Application setup

Run `run` make command. It attatches to the container, installs requirements and executes `main.py` script

```bash
make run
```

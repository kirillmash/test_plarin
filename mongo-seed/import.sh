#! /bin/bash

chmod +x /mongo-seed/import.sh
mongoimport --host mongodb  --db test --collection employees --authenticationDatabase admin --username mongo_user --password mongo_password --type json --file /mongo-seed/employees.json --jsonArray
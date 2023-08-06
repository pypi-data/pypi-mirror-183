#!/bin/bash

# This script downloads the schema from the Runner API
# It requires that an instance of the Django API is runner locally

username=$1
password=$2

# get root directory
root_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; cd .. ; pwd -P )

# curl http://127.0.0.1:8000/api/schema/ --output $root_path/schema/schema.yaml --create-dirs -u $username:$password
curl http://127.0.0.1:8000/api/schema/ --output $root_path/schema/schema.yaml --create-dirs 

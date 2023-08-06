#!/bin/bash

# This script downloads the schema from the Runner API and generates the SDK for the Runner API.

username=$1
password=$2

# get root directory
# root_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; cd .. ; pwd -P )
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$parent_path/getschema.sh $username $password
$parent_path/generatesdk.sh

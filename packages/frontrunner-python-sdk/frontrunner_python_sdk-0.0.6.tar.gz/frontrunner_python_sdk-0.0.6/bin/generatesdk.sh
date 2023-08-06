#!/bin/bash


# This script generates the SDK for the Runner API. 


joinByString() {
  local separator="$1"
  shift
  local first="$1"
  shift
  printf "%s" "$first" "${@/#/$separator}"
}

schema_name="schema"
schema_folder="schema"

exclude=($schema_folder "bin")

# -s: source schema path
# -t: target sdk path
while getopts ":s:t:" opt; do
    case $opt in
        s) 
            schema_name="$OPTARG"
            ;;
        t) 
            target_sdk="$OPTARG"
            ;;
        \?) 
            echo "Invalid option -$OPTARG" >&2
            exit 1
            ;;
    esac

    case $OPTARG in
        -*) 
            echo "Option $opt needs a valid argument"
            exit 1
            ;;
    esac
done

# get root directory
root_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; cd .. ; pwd -P )
# schema_path=$root_path/schema/schema.yaml
# sdk_path=$root_path/sdk
schema_path=$root_path/$schema_folder/$schema_name.yaml
sdk_path=$root_path

# sdk must be deleted first
# rm -rf $sdk_path

# Turn on extended globbing
shopt -s extglob

# Create a list of files to keep
exclude_list=$(joinByString "\"|\"" "\"${exclude[@]}\"")

echo $exclude_list

eval "find $root_path/!($exclude_list) -exec rm -rf {} \;"
# join_by , "${exclude[@]}"

# Generate SDK using openapi-generator https://github.com/OpenAPITools/openapi-generator
openapi-generator generate -i $schema_path -g python -o $sdk_path --additional-properties=packageName=frontrunner_python_sdk



# UTILITES
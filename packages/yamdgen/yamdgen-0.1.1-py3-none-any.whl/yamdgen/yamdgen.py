#!/usr/bin/env python
# coding: utf-8


# automated version with user prompt
from yamdgen.yamd_helpers_function import *
import warnings
import yaml
import json
import sys
import os
import warnings




def generate_yamd():
    """
    This function takes in a path to a config file, a dbt project name and a path to a sql file or a folder containing sql files.
    It then generates a yaml file for each sql file in the folder or for the sql file.
    It also generates a markdown file for each sql file in the folder or for the sql file.
    """ 
    print_name()
    catalog_path = input("""Enter path to dbt catalog.json file(no quotes):""")
    file_path = input("""Now enter path to your dbt project folder or path to your sql file (no quotes) :""")
    create_md = input("Should I create md files also? yes/no:")
    suffix = '.sql'
    dbt_project_name = get_dbt_project(catalog_path)
    # Yamd for file
    if os.path.isfile(file_path) and file_path.endswith(suffix,-4): 
        path, file = os.path.split(file_path)
        table_name = file.rsplit('.', maxsplit=1)[0]
        
        model_details = get_all_cols(table_name,dbt_project_name,catalog_path)
        with open('{}/{}.yml'.format(path,table_name), 'w') as file:
            documents = yaml.dump(model_details,file, Dumper=MyDumper,  sort_keys=False)
        print("----------------------Generator Done-------------------------------------------")    
        print("File created: {}.yml has been created in {}".format(table_name,path))
        # create md
        if create_md.lower() == 'yes':
            lines = ['{{% docs {} %}}'.format(table_name),\
                     '## Overview','###### Resources:',\
                     '### Unique Key:','### Partitioned by:',\
                     '### Contains PII:','### Sources:',\
                     '### Granularity:','### Update Frequency:',\
                     '### Example Queries:','{% enddocs %}']
            with open('{}/{}.md'.format(path,table_name), 'w') as file:
                for line in lines:
                    file.write(line)
                    file.write('\n')
                    file.write('\n')
                print("File created: {}.md has been created in {}".format(table_name,path))
    # Yamd for folder
    elif os.path.isdir(file_path):
        all_tables = get_all_models(catalog_path)
        for root, dirs, files in os.walk(file_path):
            for file in files:
                suffix = '.sql'
                if file.endswith(suffix,-4) and file.rsplit('.', maxsplit=1)[0] in all_tables:
                    table_name = file.rsplit('.', maxsplit=1)[0]
                    
                    model_details = get_all_cols(table_name,dbt_project_name,catalog_path)
                    with open('{}/{}.yml'.format(root,table_name), 'w') as file:
                        documents = yaml.dump(model_details,file, Dumper=MyDumper,  sort_keys=False)
                    print("----------------------Generator Done-------------------------------------------")    
                    print("File created: {}.yml has been created in {}".format(table_name,root))
                    # create md
                    if create_md.lower() == 'yes':
                        lines = ['{{% docs {} %}}'.format(table_name),\
                                 '## Overview','###### Resources:',\
                                 '### Unique Key:','### Partitioned by:',\
                                 '### Contains PII:','### Sources:',\
                                 '### Granularity:','### Update Frequency:',\
                                 '### Example Queries:','{% enddocs %}']
                        with open('{}/{}.md'.format(root,table_name), 'w') as file:
                            for line in lines:
                                file.write(line)
                                file.write('\n')
                                file.write('\n')
                            print("File created: {}.md has been created in {}".format(table_name,root))
                            
                            
def main():
    generate_yamd()


if __name__ == '__main__':
    main()   
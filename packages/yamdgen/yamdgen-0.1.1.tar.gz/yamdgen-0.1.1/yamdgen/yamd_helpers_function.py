import yaml
import json
import sys
import os

    
def get_all_cols(table_name,dbt_project_name,catalog_file_loc):
    """
        This function returns all the columns of a table in a dbt project.
        Args:
            table_name (str): The name of the table in the dbt project.
            dbt_project_name (str): The name of the dbt project.
            catalog_file_loc (str): The location of the catalog file.
        Returns:
            model_details (dict): A dictionary containing the table name, description, tests and columns.   
    """        
    with open(catalog_file_loc) as f:
        catalogs = json.load(f)
    catalog_nodes = catalogs['nodes']    
    tbl_columns = []
    for column_name, column_details in catalog_nodes[f"""model.{dbt_project_name}.{table_name}"""]['columns'].items():  

            col_metadata = {
                'name':column_name,
                'col_type':column_details['type'],
                'materialization':catalog_nodes[f"""model.{dbt_project_name}.{table_name}"""]['metadata']['type']}
            tbl_columns.append(col_metadata)
    table_details = []
    for col in tbl_columns:
        if col.get('materialization') not in ['ephemeral']:
            table_details.append({"name":col.get('name'),"description": "","tests": ""})                                        
            schema_detail = [{'name':table_name,\
                      'description':"",\
                      'tests':"", 'columns' : table_details}]
            model_details = {'version':2,'models':schema_detail} 
    
    return (model_details)


def get_all_models(catalog_path):
    """
        This function returns all the tables of a dbt project found in the dbt catalog file.
        Args:
            catalog_file_loc (str): The location of the catalog file.
        Returns:
            table_all (list): A list containing all the table names in catalog.json of dbt.   
    """     
    with open(catalog_path) as f:
        catalogs = json.load(f)
    catalog_column_data = catalogs['nodes']    
    table_all = [catalog_column_data.get(tbl).get('metadata').get('name') for tbl in catalog_column_data]
    return (table_all)


def get_dbt_project(catalog_path):
    """
        This function returns the name of the dbt project in the catalog.json provided. =
        Args:
            catalog_file_loc (str): The location of the catalog file.
        Returns:
            dbt project name (str): A string value for the dbt project name.
    """     
    with open(catalog_path) as f:
        catalogs = json.load(f)
    catalog_column_data = catalogs['nodes']   
    dbt_project_name =  list(catalog_column_data.keys())[0].split('.')[1]
    return (dbt_project_name)

class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()       
        if len(self.indents) == 4 and self.line !=6 :
            super().write_line_break()      
            
            
def print_name():

    welcome="""                      
    ____ _____ _   _ _____ ____      _  _____ ___  ____  
    / ___| ____| \ | | ____|  _ \    / \|_   _/ _ \|  _ \ 
    | |  _|  _| |  \| |  _| | |_) |  / _ \ | || | | | |_) |
    | |_| | |___| |\  | |___|  _ <  / ___ \| || |_| |  _ < 
    \____|_____|_| \_|_____|_| \_\/_/   \_\_| \___/|_| \_\
                                                       
     
                                                           """
    print(welcome)
                                  
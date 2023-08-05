import yaml


def add_num(a, b):
    return a+b


def sub_num(a, b):
    return a-b


def mul_nu(a, b):
    return a*b


def get_yaml_config(dag_name):
    base_yaml_file_path = "sqlIngestConfigs/resources/base_sql_ingest_config.yaml"
    with open(base_yaml_file_path, 'r') as file:
        input_config = yaml.safe_load(file)

    print(input_config["dag_configs"]["name"])
    input_config["dag_configs"]["name"] = dag_name
    print(input_config["dag_configs"]["name"])



import ruamel.yaml
import string


def get_dag_name_from_table_name(table_name):
    return table_name.upper()


def get_cluster_name_from_table_name(table_name):
    prefix_cluster_name = "rapido-sql-ingest"
    cluster_name = table_name.replace("_", "-")
    return f"{prefix_cluster_name}-{cluster_name}"


def valid_person_name_chars():
    return set(string.ascii_lowercase + '_')


def valid_table_name_chars():
    return set(string.ascii_lowercase + string.digits + '_')


def valid_dag_name_chars():
    return set(string.ascii_uppercase + string.digits + '_')


def valid_cluster_name_chars():
    return set(string.ascii_lowercase + string.digits + '-')


def get_configs(pm_name, user_name, start_date, schedule_interval, table_name, partition_columns, backfill=False):
    if len(table_name) > 25:
        raise Exception("Table name should NOT exceed 25 chars !!!")

    if not set(pm_name) <= valid_person_name_chars():
        raise Exception("Invalid PM name, Only lowercase alphabets and '_' are allowed")

    if not set(user_name) <= valid_person_name_chars():
        raise Exception("Invalid PM name, Only lowercase alphabets and '_' are allowed")

    if not set(table_name) <= valid_table_name_chars():
        raise Exception("Invalid Table name, Only lowercase alphabets, digits and '_' are allowed")

    dag_name = get_dag_name_from_table_name(table_name)
    if not set(dag_name) <= valid_dag_name_chars():
        raise Exception("Invalid DAG name, Only uppercase alphabets, digits and '_' are allowed")

    cluster_name = get_cluster_name_from_table_name(table_name)
    if len(cluster_name) > 50:
        raise Exception("Dag name should NOT exceed 50 chars !!!")
    if not set(cluster_name) <= valid_cluster_name_chars():
        raise Exception("Invalid Cluster name, Only lowercase alphabets, digits and '-' are allowed")

    input_yaml_file_path = "resources/base_sql_ingest_config.yaml"
    input_config = ruamel.yaml.round_trip_load(open(input_yaml_file_path, "rb"), preserve_quotes=True)

    input_config['pm'] = pm_name
    input_config['user'] = user_name

    dag_config = input_config['dag_configs'][0]
    dag_config['name'] = dag_name
    dag_config['backfill'] = backfill

    dag_config['run_config']['cluster_config']['name'] = cluster_name
    dag_config['run_config']['schedule_config']['start_date'] = start_date
    dag_config['run_config']['schedule_config']['schedule_interval'] = schedule_interval

    job_configs = dag_config['job_configs'][0]
    job_configs['write_store']['base_path'] += table_name
    print(partition_columns)
    job_configs['write_store']['partition_columns'] = partition_columns

    job_configs['table_view_config']['table_name'] = table_name
    job_configs['table_view_config']['view_name'] = table_name
    job_configs['table_view_config']['base_path'] += table_name

    return input_config


def get_yaml_file(configs_dict, path):
    ruamel.yaml.round_trip_dump(configs_dict, open(path, "w"), default_flow_style=False)
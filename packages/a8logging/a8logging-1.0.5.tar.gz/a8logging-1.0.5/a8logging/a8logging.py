import logging
import traceback
import uuid

# from elasticsearch import Elasticsearch, NodeConfig
# node_config = NodeConfig(scheme='http')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='logs.txt'
)

# Connect to Elasticsearch
# es = Elasticsearch(host='localhost', port=9200, node_config=node_config)

def a8logging(status, message, function_name=None, error=None, project_name=None, version=None, save_to_file=False, push_to_kibana=False, file_name=None):
    """
    Log an event with the given status, message, function name, error, project name, and version.
    Optionally save the log to a file and/or push it to Kibana.

    :param status: (str): The status of the event ('success' or 'error')
    :param message: (str): The message to log
    :param function_name: (str, optional): The name of the function where the event occurred
    :param error: (Exception, optional): The error that occurred (if applicable)
    :param project_name: (str, optional): The name of the project where the event occurred
    :param version: (str, optional): The version of the project where the event occurred
    :param save_to_file: (bool, optional): Whether to save the log to a file (default: False)
    :param push_to_kibana: (bool, optional): Whether to push the log to Kibana (default: False)
    """
    if status == 'success':
        if function_name:
            log_message = "{} - {} - {} - {} - {}".format(message, function_name, project_name, version, status)
        else:
            log_message = "{} - {} - {} - {}".format(message, project_name, version, status)
        logging.info(log_message)
    elif status == 'error':
        if function_name:
            log_message = "{} - {} - {} - {} - {} - {}".format(message, function_name, error, project_name, version, status)
        else:
            log_message = "{} - {} - {} - {} - {}".format(message, error, project_name, version, status)
        logging.error(log_message)
    
    # Push log to Kibana (if enabled)
    # if push_to_kibana:
    #     log_id = str(uuid.uuid4())
    #     es.index(index='logs', id=log_id, body={'message': log_message})
    
    # Save log to file (if enabled)
    if save_to_file:
        if not file_name:
            file_name = 'logs.txt'
        with open(file_name, 'a') as f:
            f.write(log_message + '\n')
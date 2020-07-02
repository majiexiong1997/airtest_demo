import yaml
def yaml_load(yaml_file):
    yaml_type = yaml.safe_load(open(yaml_file))
    return yaml_type

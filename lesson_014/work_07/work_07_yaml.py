import yaml

with open('yaml_example.yaml', 'r') as stream:
    martin = yaml.load(stream, Loader=yaml.FullLoader)
    print(martin)

martin = yaml.dump(martin)

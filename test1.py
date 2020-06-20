import yaml


cfg = yaml.safe_load(open("./test_img/test_img.yml"))
list_app = []

for i in cfg['touch']:
    list_app.append(i)
print(list_app)








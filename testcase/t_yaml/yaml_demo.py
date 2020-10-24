import yaml
from utils.YamlUtil import YamlReader
# with open("./data.yaml","r",encoding="utf-8") as f:
#     r=yaml.safe_load(f)
#     print(r)


# with open("./data.yaml","r",encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)
#
# print(YamlReader("./data.yaml").data())
print(YamlReader("./data.yaml").data_all())
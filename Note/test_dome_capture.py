import yaml
with open('E:\AutomationApiTest_01\Config\config.yaml', 'r') as file:
  data = yaml.safe_load(file)

users=data['users']
names = [user['name'] for user in users]
print(names[0])


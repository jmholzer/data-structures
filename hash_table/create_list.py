from pprint import pprint
import random, string

str_dict = str_dict = {''.join(random.choices(string.ascii_uppercase + string.digits, k=10)): "test" for _ in range(130)} 

pprint(str_dict)
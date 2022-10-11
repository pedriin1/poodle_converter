import os
import sys
import json
import ijson
from datetime import date
import hashlib
from decimal import *


def hash_function(x):
    return hashlib.md5(x.encode()).hexdigest()

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


def generate_bulk_string(json_data, opensearch_index_name, name, position ):

    """
    Recives a list of json objects and returns a string with the bulk format
    ex: recived: [{"name": "pedro", "age": 23}, {"name": "pedro", "age": 23}]

    returns:    {"index": {"_index": "index_name", "_id": "09e2104d8e18e73d94c4be403f263d71"}}
                {"name": "pedro", "age": 23, "upload_id": [{"id": "name_2_2_2022-10-11"}, {"name": "name"}, {"length": "2"}, {"date": "2022-10-11"}, {"position": "2"}]}
                {"index": {"_index": "index_name", "_id": "09e2104d8e18e73d94c4be403f263d71"}}
                {"name": "pedro", "age": 23, "upload_id": [{"id": "name_2_2_2022-10-11"}, {"name": "name"}, {"length": "2"}, {"date": "2022-10-11"}, {"position": "2"}]}
    """
  
    bulk_data = []
    name = name.replace("_", "").replace(" ", "").replace("-", "")
    length = str(len(json_data))
    today = str(date.today())
    position = str(position)
    upload_id = [{"id": name+"_"+position+"_"+length+"_"+today }, {"name" : name}, {"length" : length}, {"date" : today}, {"position": position}]

    f1 = lambda x: x.update({"upload_id": upload_id}) or x
    f2 = lambda x: {"index" : { "_index": opensearch_index_name, "_id" : hash_function(str(x)) }}
    bulk_data = [f(x) for x in json_data for f in (f2,f1)]
  
    
    return '\n'.join([json.dumps(line) for line in bulk_data]) + '\n'



def generate_txt_files(file_path, file_size_in_mb, output_dir, opensearch_index_name):
    file_size_in_mb = file_size_in_mb/1.6
    read_result = []
    index = 0
    position = 0
    head_elements = 0
    estimated_size = 0
    total_length = 0
    

    file_name = file_path.split("/")[-1].replace(".json", "").replace("_", "").replace("-", "")
    today = date.today()

    f = open(file_path)
    file_stats = round(os.stat(file_path).st_size / (1024 * 1024))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    

    for item in ijson.items(f, "item"):
        read_result.append(item)
        head_elements += 1

        if head_elements == 500:
            estimated_size = sys.getsizeof(json.dumps(read_result, cls=DecimalEncoder))

        if estimated_size * head_elements/500  > file_size_in_mb * 1000000 + head_elements * 160:
            with open(f'{output_dir}/{file_name}_{position}_{len(read_result)}_{today}.poodle', 'w+') as f:
                f.write(generate_bulk_string(read_result, opensearch_index_name, file_name, position))            
            print(f"Writing file: {file_stats}/{round((estimated_size * index/500) / (1024 * 1024))}" ,end="\r")
            total_length += len(read_result)
            read_result = []
            head_elements = 0
            position += 1

        index += 1
        
    with open(f'{output_dir}/{file_name}_{position}_{len(read_result)}_{today}.poodle', 'w+') as f:
        f.write(generate_bulk_string(read_result, opensearch_index_name, file_name, position))  
        total_length += len(read_result)

    print(f"\n{total_length}")
    f.close()


def main():
    generate_txt_files("/Users/pedromaia/Desktop/s3-to-opensearch/resources/book_rating.json", 3, "/Users/pedromaia/Desktop/s3-to-opensearch/data_generated", "pedro")


if __name__ == "__main__":
    main()
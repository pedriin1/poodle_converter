from datetime import date, datetime
import json
from time import time
import ijson
import sys
import json
from decimal import *
import os
from datetime import date

from main import generate_bulk_string


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


def generate_txt_files(file_path, file_size_in_mb, file_name, output_dir):
    f = open(file_path + file_name)
    file_stats = os.stat(file_path + file_name)
    today = date.today()
    
    aux_arr = []
    counter = 0
    index = 0
    head_elements = 0
    estimated_size = 0
    file_size_in_mb = file_size_in_mb/3
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for item in ijson.items(f, "item"):
        index += 1
        aux_arr.append(item)
        head_elements += 1
        if head_elements == 500:
            estimated_size = sys.getsizeof(json.dumps(aux_arr, cls=DecimalEncoder))

        if estimated_size * head_elements/500  > file_size_in_mb * 1000000:
            with open(f'data_generated/{file_name.replace(".json", "").replace("_", "")}_{counter}_{len(aux_arr)}_{today}.txt', 'w+') as f:
                f.write(generate_bulk_string(aux_arr, "index_name", file_name, len(aux_arr)))
                json.dump(aux_arr, f, cls=DecimalEncoder)
            
            print(f"Writing file: {round(file_stats.st_size / (1024 * 1024))}/{round((estimated_size * index/500) / (1024 * 1024))}" ,end="\r")
            counter += 1
            aux_arr = []
            head_elements = 0

    with open(f'data_generated/data-{counter}-{len(aux_arr)}-{date.day()}.txt', 'w+') as f:
        json.dump(aux_arr, f, cls=DecimalEncoder)

def generate_txt_files2(file_path, file_size_in_mb, output_dir, opensearch_index_name):
    file_size_in_mb = file_size_in_mb/1.6
    read_result = []
    index = 0
    position = 0
    head_elements = 0
    estimated_size = 0

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
            with open(f'{output_dir}/{file_name}_{position}_{len(read_result)}_{today}.txt', 'w+') as f:
                f.write(generate_bulk_string(read_result, opensearch_index_name, file_name, position))            
            print(f"Writing file: {file_stats}/{round((estimated_size * index/500) / (1024 * 1024))}" ,end="\r")
            
            read_result = []
            head_elements = 0
            position += 1

        index += 1
        
    with open(f'{output_dir}/{file_name}_{position}_{len(read_result)}_{today}.txt', 'w+') as f:
        f.write(generate_bulk_string(read_result, opensearch_index_name, file_name, position))  

    f.close()

generate_txt_files2("/Users/pedromaia/Desktop/s3-to-opensearch/resources/book_rating.json", 3, "/Users/pedromaia/Desktop/s3-to-opensearch/data_generated", "pedro")


# name-len-date


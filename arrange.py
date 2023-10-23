import re
import random
import string

def generate_random_id(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return random_id
def extract_ips_from_file(filename):
    ips = []
    with open(filename, 'r') as file:
        for line in file:
            ip_matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            ips.extend(ip_matches)
    return ips

def remove_duplicate_ips(ips):
    return list(set(ips))

def sort_ips(ips):
    sorted_ips = sorted(ips, key=lambda ip: [int(x) for x in ip.split('.')])
    return sorted_ips

def save_ips_to_file(ips, output_filename):
    with open(output_filename, 'w') as file:
        for ip in ips:
            file.write(ip + '\n')

filename = 'input.txt'
rfilename = generate_random_id(8)
output_filename = f'./data/{rfilename}-output.txt'
ips = extract_ips_from_file(filename)
unique_ips = remove_duplicate_ips(ips)
sorted_ips = sort_ips(unique_ips)
save_ips_to_file(sorted_ips, output_filename)
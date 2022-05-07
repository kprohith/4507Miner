# Random Miner

import hashlib
import string
import itertools
import datetime
import random
import sys
import requests

count = int(sys.argv[1])
fixed_count = count
zero_str = ''
while count != 0:
    zero_str = zero_str + '0'
    count -= 1


s_id = '4xxxxxxx'
nonce = ""
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits +
                  "`~!@#$%^&*()_+[]{}\|;:'\",<.>?/")
random.shuffle(characters)
attempt = 0
found = 0
start_time = datetime.datetime.now()
print("Starting time: %s" % start_time)
while found == 0:
    print("Starting miner")
    random.shuffle(characters)
    for i in itertools.product(*[characters] * 40):  # Random
        print("|------------------------------------------------------------------------|")
        print("Attempt: %s" % attempt)
        nonce = ("".join(i))
        print("Nonce: %s" % nonce)
        con_string = str(s_id)+str(nonce)
        print("String: %s" % con_string)
        hash = hashlib.sha256(con_string.encode()).hexdigest()
        print("Hash: %s" % hash)
        # if hash[:11] == '00000000000':
        # if hash[:6] == '000000':
        if hash[:fixed_count] == zero_str:
            found = 1
            print(
                "|************************************************************************|")
            print("Hash found!")
            print(
                "|************************************************************************|")
            print('** Number of leading ZEROS: %s **' % fixed_count)
            print("Attempt: %s" % attempt)
            end_time = datetime.datetime.now()
            hashrate = attempt/(end_time-start_time).total_seconds()
            print('Start time: %s' % start_time)
            print('End time: %s' % end_time)
            print('Duration: %s' % (end_time-start_time))
            print('Hashrate: %s H/s' % hashrate)
            files = [
                ('from', (None, '<email>')),
                ('to', (None, '<email>')),
                ('to', (None, '<email>')),
                ('subject', (None, 'Hash found - Leading zeros: %s' % fixed_count)),
                ('text', (None, 'Hash found! \n Attempt: %s \n Leading zeros: %s! \n Hash: %s \n Nonce: %s \n Start time: %s \n End time: %s \n Duration: %s \n Hashrate: %s H/s' %
                 (attempt, fixed_count, hash, nonce, start_time, end_time, end_time-start_time, hashrate))),
            ]
            response = requests.post('<mailgun-url>',
                                     files=files, auth=('api', '<api-key>'))
            print("Email sent.")
            print(
                "|************************************************************************|")
            print('Hash: %s' % hash)
            print('Nonce: %s' % nonce)
            print(
                "|************************************************************************|")
            break
        else:
            print("Hash not found")
            random.shuffle(characters)
            attempt += 1

print("Exited")
from asyncore import write
import os
import json
import sys


map  = {
    "region": "${AWS_REGION}",
    "stagingAreaSubnetId": "${SUBNET_ID}",
    "edrClass": "${EDR_CLASS}"
}
with open('tmpfile.json', 'w') as outfile:
    json.dump(map, outfile)


map2 = {
    "sg_id": "${SG_ID}"
}
with open('tmpsgfile.json', 'w') as outfile:
    json.dump(map2, outfile) 

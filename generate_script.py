import os
import json
import sys


map  = {
    "region": "${env.AWS_REGION}",
    "stagingAreaSubnetId": "${env.SUBNET_ID}",
    "edrClass": "${env.EDR_CLASS}"
}
with open('config-repo/tmpfile.json', 'w') as outfile:
    json.dump(map, outfile)

map2 = {
    "sg_id": "${env.SG_ID}"
}
with open('config-repo/tmpsgfile.json', 'w') as outputfile:
    json.dump(map2, outfile) 

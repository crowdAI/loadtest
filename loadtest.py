#!/usr/bin/env python

# cd /tmp;virtualenv env;source env/bin/activate;pip install git+https://github.com/spMohanty/crowdai-client-py;python -c 'import crowdai;challenge = crowdai.Challenge("GeccoOptimizationChallenge2017", "4f2b61e1aaf03d3283f135febbe225a4");response = challenge.evaluate_parallel([[1, 2, 3]]*5);challenge.submit([1,2,3])'
import sys
import crowdai

#api_key = sys.argv[1]
#api_key = str(api_key).strip()

api_keys = [

]


def make_submission(api_key):
  challenge = crowdai.Challenge("GeccoOptimizationChallenge2017", api_key)
  print challenge
  response = challenge.evaluate_parallel([[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
  print response
  response = challenge.submit([1,2,3])
  print response
  challenge.disconnect()

for api_key in api_keys:
  make_submission(str(api_key).strip())

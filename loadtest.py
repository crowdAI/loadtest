#!/usr/bin/env python
import sys
import crowdai

api_key = sys.argv[1:]
print api_key
challenge = crowdai.Challenge("GeccoOptimizationChallenge2017", api_key)
print challenge
response = challenge.evaluate_parallel([[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
print response
response = challenge.submit([1,2,3])
print response

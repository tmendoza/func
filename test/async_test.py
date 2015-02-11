#!/usr/bin/python

from func.overlord.client import Overlord
import func.jobthing as jobthing
import time
import sys

TEST_SLEEP = 1
EXTRA_SLEEP = 1

SLOW_COMMAND = 1
QUICK_COMMAND = 2
RAISES_EXCEPTION_COMMAND = 3
FAKE_COMMAND = 4
TESTS = [ SLOW_COMMAND, QUICK_COMMAND, RAISES_EXCEPTION_COMMAND, FAKE_COMMAND ]
#TESTS = [ QUICK_COMMAND ]
#TESTS = [ SLOW_COMMAND, QUICK_COMMAND, R ]

def __tester(async,test, count):
    if async:
        overlord= Overlord("*",nforks=3,async=True)
        oldtime = time.time()

        job_id = -411
        print
  #      print "======================================================"
        print "test iteration: %s" % count
        if test == SLOW_COMMAND:
            print "TESTING command that sleeps %s seconds" % TEST_SLEEP
            job_id = overlord.test.sleep(TEST_SLEEP)
        elif test == QUICK_COMMAND:
  #          print "TESTING a quick command"
            job_id = overlord.test.ping()
  #          job_id = overlord.test.add(1,2)
        elif test == RAISES_EXCEPTION_COMMAND:
            print "TESTING a command that deliberately raises an exception"
            job_id = overlord.test.explode() # doesn't work yet
        elif test == FAKE_COMMAND:
            print "TESTING a command that does not exist"
            job_id = overlord.test.does_not_exist(1,2) # ditto
#       print "======================================================"

        print "job_id = %s" % job_id
        while True:
            status = overlord.job_status(job_id)
            print "job_status: %s" % status[0]
            (code, results) = status
            nowtime = time.time()
            delta = int(nowtime - oldtime)
            if nowtime > oldtime + TEST_SLEEP + EXTRA_SLEEP:
                print "time expired, test failed"
                return
            if code == jobthing.JOB_ID_RUNNING:
                print "task is still running, %s elapsed ..." % delta
            elif code == jobthing.JOB_ID_PARTIAL:
                print "task reports partial status, %s elapsed, results = %s" % (delta, results)
            elif code == jobthing.JOB_ID_FINISHED:
                print "task complete, %s elapsed, results = %s" % (delta, results)
                return
            else:
                print "job not found: %s, %s elapased" % (code, delta)
            time.sleep(1)
    else:
        print Overlord("*",nforks=3,async=False).test.sleep(5)
        print Overlord("*",nforks=3,async=False).test.bork(5)
        print Overlord("*",nforks=1,async=False).test.bork(5)

i = 1
while i < 3:
    for t in TESTS:
        __tester(True,t, i)
    i = i + 1

#print "======================================================="
#print "Testing non-async call"
#print __tester(False,-1)

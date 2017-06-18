#!/usr/bin/python2

import  os,time,commands,sys,socket
options="""
press  1  to  setup  Hadoop Cluster  :
press  2  to  setup  MR  :
press  3  to  setup  HIVE    :
"""
print   options 
#   ch  for  storing  options  
ch=raw_input()

if  ch  ==  '1' :
	print   "Nice  choice  lets  start  process  "
        time.sleep(2)
        #switch to hdfs_setup proces
	execfile('hdfs_setup.py')


elif   ch  ==  '2' :
	print   "make sure  you have enough  Amount to CPU cores "
        time.sleep(2)
        #switch mr_setup process
        #execfile('mr_setup.py')

elif   ch  ==  '3' :
        print   "ready for the hive_setup process"
        time.sleep(2)
        #switch to hive_setup process
        #execfile('hive_setup.py')

else   :
       print "wrong option"
       time.sleep(2)
       #switch to previous page
       execfile('statpr.py')





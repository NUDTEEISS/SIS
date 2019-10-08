import time
start = time.clock()
from imsharing import *
from imrecover import *
k=3
n=3
Keys = [1,2,3]
time1 = time.clock() - start
imsharing(k,n,Keys)
time2 = time.clock() - start
imrecover(Keys)
time3 = time.clock() - start
print "share:",time2 - time1
print "recover:",time3 - time2
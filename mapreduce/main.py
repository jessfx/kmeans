import os
import subprocess
import numpy as np

fp = open('./testdata.txt')
fp0 = open('./old_centlist.txt', 'w')
fplines = fp.readlines()
size = len(fplines)
centnumlist = random.sample(range(size), k)
string = []
for centnum in centnumlist:
    string.append(str(centnum) + '\t' + fplines[centnum])
fp0.writelines(string)
fp0.close()
fp.close()
os.system('hadoop fs -put ./old_centlist.txt /')
status_code, string = subprocess.getstatusoutput(
    'hadoop fs -ls /output_kmeans')
if status_code == 1:
    os.system('hadoop fs -rmr /output_kmeans')

for iterate_time in range(max_iterate):
    os.system('sh ./run.sh')
    os.system('hadoop fs -get /old_centlist.txt ~/')
    os.system('hadoop fs -rmr /old_centlist.txt')
    fp = open('~/old_centlist.txt')
    old_centlist = []
    for line in fp.readlines():
        cluster_num, values = line.strip().split('\t')
        array = []
        for value in values.split(' ')[2:]:
            array.append(int(value))
        old_cent = [int(cluster_num), 'xxxxxxxxxxxx',
                    'xxxxxxxxxx', np.array(array)]
        old_centlist.append(old_cent)
    fp0.close()
    old_cent.sort(cmp=lambda x, y: cmp(x[0], y[0]))
    os.system('hadoop fs -get /new_centlist.txt ~/')
    os.system('hadoop fs -rmr /new_centlist.txt')
    fp = open('~/new_centlist.txt')
    for line in fp.readlines():
        cluster_num, values = line.strip().split('\t')
        array = []
        for value in values.split(' ')[2:]:
            array.append(int(value))
        new_cent = [int(cluster_num), 'xxxxxxxxxxxx',
                    'xxxxxxxxxx', np.array(array)]
        if (new_cent[3] == old_centlist[new_cent[0]][3]).all() is not True:
            fp.close()
            # os.system('rm ~/old_centlist.txt')
            # os.system('mv ~/new_centlist.txt ~/old_centlist.txt')
            # os.system('touch ~/new_centlist.txt')
            # os.system('hadoop fs -put ~/old_centlist.txt /')
            # os.system('hadoop fs -put ~/new_centlist.txt /')
            # os.system('rm ~/old_centlist.txt')
            # os.system('rm ~/new_centlist.txt')
            os.system('sh ./clear.sh')
            break

rm ~/old_centlist.txt
mv ~/new_centlist.txt ~/old_centlist.txt
touch ~/new_centlist.txt
hadoop fs -put ~/old_centlist.txt /
hadoop fs -put ~/new_centlist.txt /
rm ~/old_centlist.txt
rm ~/new_centlist.txt
hadoop fs -rmr /output_kmeans
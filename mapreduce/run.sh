set -e -x

HADOOP_CMD="/usr/local/hadoop-2.8.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/hadoop-2.8.1/contrib/streaming/hadoop-streaming-2.8.1.jar"

INPUT_FILE_PATH="/testdata.txt"

OUTPUT_PATH="/output_kmeans"

# Step 3.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH\
    -output $OUTPUT_PATH \
    -mapper "python mapA.py" \
    -reducer "python reduceA.py" \
    -file ./mapA.py \
    -file ./reduceA.py \
    -file ./old_centlist.txt \
    -file ./new_centlist.txt \
    -jobconf mapred.reduce.tasks=5 \
    -jobconf stream.num.map.output.key.fields=1 \
    -jobconf num.key.fields.for.partition=5 \

    #-jobconf stream.map.output.field.separator='	' \

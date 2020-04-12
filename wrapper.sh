export SPARK_MAJOR_VERSION=2
spark-submit \
--master local \
--deploy-mode client \
xml_to_csv.py local `pwd`

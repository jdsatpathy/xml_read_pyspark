export SPARK_MAJOR_VERSION=2
spark-submit \
--master local \
--deploy-mode client \
/Users/jdsatpathy/python_scripts/xml_read/xml_to_csv.py local /Users/jdsatpathy/python_scripts/xml_read/out

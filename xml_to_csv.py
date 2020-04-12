from pyspark import SparkConf
from pyspark.sql import SparkSession
import sys
def main():
    arg = sys.argv
    master = arg[0]
    outputPath = arg[1]
    conf = SparkConf.setAppName("XML to CSV").setMaster(master)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    xml_file = spark.read.format("com.databricks.spark.xml").options(rootTag='catalog', rowTag='book').load(outputPath)
    xml_file.write.option("header", "true").csv(outputPath + "/output")
    print ("File saved successfully")


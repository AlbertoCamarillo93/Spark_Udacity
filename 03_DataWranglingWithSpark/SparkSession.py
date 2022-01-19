from pyspark sql import SparkSession

spark = SparkSession \
.builder \
.appName("app name") \
.config("conf option", "confi value") \
.getOrCreate()
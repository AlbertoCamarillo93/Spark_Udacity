from pyspark import SparkContext, SparkConf

configure = SparkConf().setAppName("name").setMaster("ip address / local")

sc = SparkContext(conf = configure)

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, udf
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from textblob import TextBlob
from elasticsearch import Elasticsearch

# ⚠️ Use Docker service name, NOT localhost
es = Elasticsearch("http://elasticsearch:9200")  # from docker-compose service name

# ⚠️ Use Kafka's internal Docker hostname
KAFKA_BROKER = "kafka:9092"
TOPIC = "social_stream"

# Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkConsumerWithSentiment") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Schema for Kafka JSON
schema = StructType([
    StructField("user", StringType(), True),
    StructField("text", StringType(), True),
    StructField("timestamp", DoubleType(), True)
])

# Sentiment analysis function
def get_sentiment(text):
    try:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
    except:
        return "unknown"

sentiment_udf = udf(get_sentiment, StringType())

# Read stream from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON and apply sentiment
parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

sentiment_df = parsed_df.withColumn("sentiment", sentiment_udf(col("text")))

# Write each batch to Elasticsearch
def write_to_es(batch_df, batch_id):
    for row in batch_df.toLocalIterator():
        doc = {
            "user": row["user"],
            "text": row["text"],
            "timestamp": row["timestamp"],
            "sentiment": row["sentiment"],
        }
        es.index(index="social_sentiment", document=doc)

# Start streaming
query = sentiment_df.writeStream \
    .foreachBatch(write_to_es) \
    .outputMode("update") \
    .start()

query.awaitTermination()

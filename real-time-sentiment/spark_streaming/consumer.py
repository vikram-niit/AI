from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, udf
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from textblob import TextBlob

# Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkConsumerWithSentiment") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.1") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Kafka config
KAFKA_BROKER = "localhost:9092"
TOPIC = "social_stream"

# JSON schema
schema = StructType([
    StructField("user", StringType(), True),
    StructField("text", StringType(), True),
    StructField("timestamp", DoubleType(), True)
])

# Sentiment function
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

# Register UDF
sentiment_udf = udf(get_sentiment, StringType())

# Read Kafka stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON
parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Add sentiment column
sentiment_df = parsed_df.withColumn("sentiment", sentiment_udf(col("text")))

# Print results to console
query = sentiment_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()

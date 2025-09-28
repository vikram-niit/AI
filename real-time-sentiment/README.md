# Real-time Sentiment Analysis System

A comprehensive real-time sentiment analysis pipeline using Kafka, Spark Streaming, and modern visualization tools.

## 🏗️ Architecture

```
Data Sources → Kafka Producer → Kafka → Spark Streaming → Sentiment Analysis → Dashboard
     ↓              ↓              ↓           ↓              ↓              ↓
  Twitter      Raw Data      Message      Processing      Results      Visualization
  News API     Ingestion     Queue        Pipeline        Storage      (Streamlit)
  Reddit
```

## 📁 Project Structure

```
real-time-sentiment/
│
├── kafka_producer/          # Data ingestion
│   ├── producer.py          # Kafka producer for streaming data
│   ├── config.json          # Configuration for data sources
│
├── spark_streaming/         # Stream processing
│   ├── stream_processor.py  # Spark streaming sentiment analysis
│
├── models/                  # ML models
│   ├── sentiment_model.pkl  # Pre-trained sentiment model (optional)
│
├── dashboard/               # Visualization
│   ├── app.py              # Streamlit dashboard
│
├── docker-compose.yml      # Container orchestration
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.8+ (for local development)
- Java 8+ (for Spark)

### 1. Clone and Setup

```bash
git clone <repository-url>
cd real-time-sentiment
```

### 2. Start the System

```bash
# Start all services
docker-compose up -d

# Check service status
docker-compose ps
```

### 3. Access the Dashboard

- **Streamlit Dashboard**: http://localhost:8501
- **Kafka UI**: http://localhost:8080
- **Kibana**: http://localhost:5601
- **Elasticsearch**: http://localhost:9200

## 🔧 Configuration

### Kafka Producer Configuration

Edit `kafka_producer/config.json`:

```json
{
  "kafka": {
    "bootstrap_servers": ["localhost:9092"],
    "topics": {
      "raw_data": "sentiment-raw-data",
      "processed_data": "sentiment-processed-data"
    }
  },
  "data_sources": {
    "twitter": {
      "enabled": true,
      "api_key": "your_twitter_api_key"
    }
  }
}
```

### Data Sources

The system supports multiple data sources:

- **Twitter API**: Real-time tweets
- **News API**: News articles
- **Reddit API**: Reddit posts and comments
- **Custom APIs**: Add your own data sources

## 📊 Features

### Real-time Processing
- **Kafka**: High-throughput message queuing
- **Spark Streaming**: Distributed stream processing
- **Low Latency**: Sub-second processing times

### Sentiment Analysis
- **TextBlob**: Rule-based sentiment analysis
- **Custom Models**: Support for pre-trained ML models
- **Multi-language**: Extensible language support

### Visualization
- **Real-time Dashboard**: Live sentiment trends
- **Interactive Charts**: Plotly-based visualizations
- **Alert System**: Notifications for extreme sentiments

### Monitoring
- **Kafka UI**: Message flow monitoring
- **Kibana**: Advanced analytics and dashboards
- **Logging**: Comprehensive logging system

## 🛠️ Development

### Local Development

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Start Kafka**:
```bash
docker-compose up kafka zookeeper -d
```

3. **Run Components**:
```bash
# Producer
cd kafka_producer
python producer.py

# Stream Processor
cd spark_streaming
python stream_processor.py

# Dashboard
cd dashboard
streamlit run app.py
```

### Adding New Data Sources

1. **Extend Producer**:
```python
def stream_custom_data(self):
    # Your custom data source logic
    pass
```

2. **Update Configuration**:
```json
{
  "data_sources": {
    "custom_api": {
      "enabled": true,
      "endpoint": "https://api.example.com"
    }
  }
}
```

### Custom Sentiment Models

1. **Train Model**:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load training data
X_train, y_train = load_training_data()

# Train model
vectorizer = TfidfVectorizer(max_features=10000)
X_train_tfidf = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Save model
with open('models/sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

2. **Update Stream Processor**:
The system will automatically detect and use the new model.

## 📈 Monitoring and Alerts

### Kafka Monitoring
- **Topic Metrics**: Message rates, lag, partitions
- **Consumer Groups**: Processing status
- **Broker Health**: Resource utilization

### Sentiment Alerts
- **Negative Sentiment**: Alerts for highly negative content
- **Positive Sentiment**: Notifications for positive trends
- **Anomaly Detection**: Unusual sentiment patterns

### Performance Metrics
- **Processing Latency**: End-to-end processing time
- **Throughput**: Messages per second
- **Error Rates**: Failed processing attempts

## 🔒 Security

### Data Privacy
- **Data Anonymization**: Remove PII from text
- **Access Controls**: Role-based permissions
- **Encryption**: Data in transit and at rest

### API Security
- **Authentication**: API key management
- **Rate Limiting**: Prevent abuse
- **Input Validation**: Sanitize incoming data

## 🚨 Troubleshooting

### Common Issues

1. **Kafka Connection Failed**:
```bash
# Check Kafka status
docker-compose logs kafka

# Restart Kafka
docker-compose restart kafka
```

2. **Spark Streaming Errors**:
```bash
# Check Spark logs
docker-compose logs spark-streaming

# Verify Java version
java -version
```

3. **Dashboard Not Loading**:
```bash
# Check dashboard logs
docker-compose logs dashboard

# Restart dashboard
docker-compose restart dashboard
```

### Performance Tuning

1. **Kafka Optimization**:
```yaml
environment:
  KAFKA_NUM_NETWORK_THREADS: 8
  KAFKA_NUM_IO_THREADS: 8
  KAFKA_SOCKET_SEND_BUFFER_BYTES: 102400
```

2. **Spark Optimization**:
```python
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
```

## 📚 API Documentation

### Kafka Topics

- **sentiment-raw-data**: Raw incoming data
- **sentiment-processed-data**: Processed sentiment results
- **sentiment-alerts**: Alert notifications

### Message Format

```json
{
  "text": "Sample text for analysis",
  "user": "user_id",
  "source": "twitter",
  "timestamp": "2024-01-01T12:00:00Z",
  "sentiment": "positive",
  "polarity": 0.8,
  "confidence": 0.95
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Apache Kafka**: Distributed streaming platform
- **Apache Spark**: Unified analytics engine
- **Streamlit**: Rapid app development
- **Plotly**: Interactive visualizations
- **TextBlob**: Natural language processing

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the documentation

---

**Happy Analyzing! 📊✨**

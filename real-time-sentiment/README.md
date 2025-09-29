# ✅ Real-Time Sentiment Analysis Pipeline (Docker + EC2 Deployment)

This project sets up a full real-time sentiment analysis system using **Kafka → Spark → Elasticsearch → Kibana / Streamlit**, all orchestrated with **Docker Compose**. You can run it locally or deploy it to an AWS EC2 instance.

---

## ✅ 1. Project Structure

```
real-time-sentiment/
│
├── kafka_producer/
│   ├── producer.py
│   ├── Dockerfile
│
├── spark_streaming/
│   ├── stream_processor.py
│   ├── Dockerfile
│
├── dashboard/
│   ├── app.py
│   ├── Dockerfile
│
├── models/
│   ├── sentiment_model.pkl  # (optional)
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ✅ 2. Deploy on AWS EC2

### Install Docker & Docker Compose on EC2:
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
```

---

## ✅ 3. Copy Project to EC2

From your local machine:
```bash
scp -i /path/to/key.pem -r real-time-sentiment/ ubuntu@<EC2_PUBLIC_IP>:/home/ubuntu/
```

SSH into EC2:
```bash
ssh -i /path/to/key.pem ubuntu@<EC2_PUBLIC_IP>
cd real-time-sentiment
```

---

## ✅ 4. Start All Services

```bash
docker-compose up -d --build
```

Check services:
```bash
docker ps
```

You should see:
- zookeeper  
- kafka  
- elasticsearch  
- kibana  
- streamlit  
- spark-streaming  
- kafka-producer

---

## ✅ 5. Verify Services

### ✅ Elasticsearch:
```bash
curl -X GET "localhost:9200/_cluster/health?pretty"
```

### ✅ Kibana (Browser)
```
http://<EC2_PUBLIC_IP>:5601
```

### ✅ Streamlit
```
http://<EC2_PUBLIC_IP>:8501
```

---

## ✅ 6. Kafka Topic (Only if Needed)

```bash
docker exec -it kafka kafka-topics --create --topic social_stream --bootstrap-server kafka:9092
```

---

## ✅ 7. Data Flow Overview

Once containers are up:

1. **Kafka Producer** generates random / static messages to the topic `social_stream`.
2. **Spark Streaming** consumes the topic:
   - Performs sentiment analysis
   - Writes output to Elasticsearch index: `social_sentiment`
3. **Kibana** visualizes results
4. **Streamlit** provides a UI (optional)

---

## ✅ 8. Check Data in Elasticsearch

```bash
curl -X GET "localhost:9200/social_sentiment/_search?pretty"
```

You should see docs containing:
- user
- text
- sentiment
- timestamp

---

## ✅ 9. Kibana Dashboard Setup

1. Go to:  
   `http://<EC2_PUBLIC_IP>:5601`
2. Navigate to:  
   **Stack Management → Data Views → Create Data View**
3. Enter:
   ```
   Name: social_sentiment
   Index pattern: social_sentiment*
   ```
4. View live data:  
   **Analytics → Discover**
5. Create visualizations:
   - Pie chart → sentiment distribution
   - Bar/Line chart → sentiment over time
6. Combine into a dashboard

---

## ✅ 10. Streamlit Dashboard (Optional)

Visit:
```
http://<EC2_PUBLIC_IP>:8501
```

Your `app.py` can query Elasticsearch and visualize results.

---

## ✅ 11. Stopping / Restarting Services

To stop:
```bash
docker-compose down
```

To restart:
```bash
docker-compose up -d
```

---

## ✅ 12. Open Required Ports in AWS Security Group

| Port | Purpose |
|------|--------|
| 2181 | Zookeeper |
| 9092 | Kafka |
| 29092| Kafka external access (optional) |
| 9200 | Elasticsearch |
| 5601 | Kibana |
| 8501 | Streamlit |

---

## ✅ 13. Troubleshooting

Check container logs:
```bash
docker logs <container_name>
```

Restart a failing service:
```bash
docker-compose restart spark-streaming
```

---

## ✅ Summary Checklist

| Step | Status |
|------|--------|
| SCP project to EC2 ✅ |
| Run `docker-compose up -d --build` ✅ |
| Verify services ✅ |
| Confirm data in Elasticsearch ✅ |
| Create Kibana dashboard ✅ |
| Access Streamlit ✅ |

---

## ✅ Enhancements

You can extend this with:
- HTTPS + Nginx
- CloudWatch logging
- Managed Kafka (MSK)
- HuggingFace sentiment model
- Alerts & dashboards

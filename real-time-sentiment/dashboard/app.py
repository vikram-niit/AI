"""
Real-time Sentiment Analysis Dashboard
Streamlit application for visualizing sentiment analysis results.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import time
from datetime import datetime, timedelta
from kafka import KafkaConsumer
import threading
import queue
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SentimentDashboard:
    """Dashboard class for real-time sentiment visualization."""
    
    def __init__(self):
        """Initialize the dashboard."""
        self.setup_page_config()
        self.data_queue = queue.Queue()
        self.consumer = None
        self.running = False
        
    def setup_page_config(self):
        """Setup Streamlit page configuration."""
        st.set_page_config(
            page_title="Real-time Sentiment Analysis",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS
        st.markdown("""
        <style>
        .main-header {
            font-size: 3rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #1f77b4;
        }
        .positive { color: #28a745; }
        .negative { color: #dc3545; }
        .neutral { color: #6c757d; }
        </style>
        """, unsafe_allow_html=True)
    
    def create_kafka_consumer(self):
        """Create Kafka consumer for real-time data."""
        try:
            consumer = KafkaConsumer(
                'sentiment-processed-data',
                bootstrap_servers=['localhost:9092'],
                value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                group_id='dashboard-consumer',
                auto_offset_reset='latest'
            )
            return consumer
        except Exception as e:
            logger.error(f"Failed to create Kafka consumer: {e}")
            return None
    
    def kafka_listener(self):
        """Listen to Kafka messages in a separate thread."""
        while self.running:
            try:
                if self.consumer:
                    message = next(self.consumer)
                    data = message.value
                    self.data_queue.put(data)
            except Exception as e:
                logger.error(f"Error in Kafka listener: {e}")
                time.sleep(1)
    
    def get_sample_data(self):
        """Generate sample data for demonstration."""
        import random
        
        sentiments = ['positive', 'negative', 'neutral']
        sources = ['twitter', 'news_api', 'reddit']
        
        sample_data = []
        for i in range(50):
            sentiment = random.choice(sentiments)
            polarity = random.uniform(-1, 1)
            confidence = random.uniform(0.5, 1.0)
            
            sample_data.append({
                'text': f'Sample text {i}',
                'sentiment': sentiment,
                'polarity': polarity,
                'confidence': confidence,
                'source': random.choice(sources),
                'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 60)),
                'processed_at': datetime.now()
            })
        
        return pd.DataFrame(sample_data)
    
    def render_header(self):
        """Render the dashboard header."""
        st.markdown('<h1 class="main-header">📊 Real-time Sentiment Analysis Dashboard</h1>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Messages", "1,234", "↑ 12%")
        
        with col2:
            st.metric("Positive Sentiment", "45%", "↑ 5%")
        
        with col3:
            st.metric("Processing Rate", "150 msg/min", "↑ 8%")
    
    def render_sentiment_overview(self, df):
        """Render sentiment overview charts."""
        st.subheader("📈 Sentiment Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Sentiment distribution pie chart
            sentiment_counts = df['sentiment'].value_counts()
            fig_pie = px.pie(
                values=sentiment_counts.values,
                names=sentiment_counts.index,
                title="Sentiment Distribution",
                color_discrete_map={
                    'positive': '#28a745',
                    'negative': '#dc3545',
                    'neutral': '#6c757d'
                }
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Polarity distribution histogram
            fig_hist = px.histogram(
                df, x='polarity', nbins=20,
                title="Polarity Distribution",
                color_discrete_sequence=['#1f77b4']
            )
            fig_hist.update_layout(
                xaxis_title="Polarity (-1 to 1)",
                yaxis_title="Count"
            )
            st.plotly_chart(fig_hist, use_container_width=True)
    
    def render_time_series(self, df):
        """Render time series analysis."""
        st.subheader("⏰ Time Series Analysis")
        
        # Group by time intervals
        df['time_bucket'] = pd.to_datetime(df['processed_at']).dt.floor('5min')
        time_series = df.groupby(['time_bucket', 'sentiment']).size().unstack(fill_value=0)
        
        # Create time series plot
        fig = go.Figure()
        
        colors = {'positive': '#28a745', 'negative': '#dc3545', 'neutral': '#6c757d'}
        
        for sentiment in ['positive', 'negative', 'neutral']:
            if sentiment in time_series.columns:
                fig.add_trace(go.Scatter(
                    x=time_series.index,
                    y=time_series[sentiment],
                    mode='lines+markers',
                    name=sentiment.title(),
                    line=dict(color=colors[sentiment], width=2)
                ))
        
        fig.update_layout(
            title="Sentiment Trends Over Time",
            xaxis_title="Time",
            yaxis_title="Message Count",
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_source_analysis(self, df):
        """Render source-based analysis."""
        st.subheader("📱 Source Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Sentiment by source
            source_sentiment = pd.crosstab(df['source'], df['sentiment'])
            fig_bar = px.bar(
                source_sentiment,
                title="Sentiment by Source",
                color_discrete_map={
                    'positive': '#28a745',
                    'negative': '#dc3545',
                    'neutral': '#6c757d'
                }
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            # Average polarity by source
            avg_polarity = df.groupby('source')['polarity'].mean().reset_index()
            fig_polarity = px.bar(
                avg_polarity, x='source', y='polarity',
                title="Average Polarity by Source",
                color='polarity',
                color_continuous_scale=['#dc3545', '#6c757d', '#28a745']
            )
            st.plotly_chart(fig_polarity, use_container_width=True)
    
    def render_recent_messages(self, df):
        """Render recent messages table."""
        st.subheader("💬 Recent Messages")
        
        # Show recent messages with sentiment
        recent_df = df.nlargest(20, 'processed_at')[['text', 'sentiment', 'polarity', 'confidence', 'source', 'processed_at']]
        
        # Color code sentiment
        def color_sentiment(val):
            if val == 'positive':
                return 'background-color: #d4edda'
            elif val == 'negative':
                return 'background-color: #f8d7da'
            else:
                return 'background-color: #e2e3e5'
        
        styled_df = recent_df.style.applymap(color_sentiment, subset=['sentiment'])
        st.dataframe(styled_df, use_container_width=True)
    
    def render_sidebar(self):
        """Render sidebar controls."""
        st.sidebar.title("🎛️ Dashboard Controls")
        
        # Data source selection
        data_source = st.sidebar.selectbox(
            "Data Source",
            ["Kafka Stream", "Sample Data"],
            help="Choose between real-time Kafka data or sample data for demonstration"
        )
        
        # Time range filter
        time_range = st.sidebar.selectbox(
            "Time Range",
            ["Last Hour", "Last 6 Hours", "Last 24 Hours", "All Time"]
        )
        
        # Sentiment filter
        sentiment_filter = st.sidebar.multiselect(
            "Sentiment Filter",
            ["positive", "negative", "neutral"],
            default=["positive", "negative", "neutral"]
        )
        
        # Source filter
        source_filter = st.sidebar.multiselect(
            "Source Filter",
            ["twitter", "news_api", "reddit"],
            default=["twitter", "news_api", "reddit"]
        )
        
        # Auto-refresh toggle
        auto_refresh = st.sidebar.checkbox("Auto Refresh", value=True)
        refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 5, 60, 10)
        
        return {
            'data_source': data_source,
            'time_range': time_range,
            'sentiment_filter': sentiment_filter,
            'source_filter': source_filter,
            'auto_refresh': auto_refresh,
            'refresh_interval': refresh_interval
        }
    
    def run(self):
        """Run the dashboard."""
        # Render sidebar
        controls = self.render_sidebar()
        
        # Render header
        self.render_header()
        
        # Get data based on selection
        if controls['data_source'] == "Kafka Stream":
            # Try to get real-time data from Kafka
            if not self.consumer:
                self.consumer = self.create_kafka_consumer()
            
            if self.consumer and not self.running:
                self.running = True
                kafka_thread = threading.Thread(target=self.kafka_listener)
                kafka_thread.daemon = True
                kafka_thread.start()
            
            # Get data from queue
            data_list = []
            while not self.data_queue.empty():
                try:
                    data_list.append(self.data_queue.get_nowait())
                except queue.Empty:
                    break
            
            if data_list:
                df = pd.DataFrame(data_list)
            else:
                st.info("Waiting for real-time data... Using sample data for demonstration.")
                df = self.get_sample_data()
        else:
            # Use sample data
            df = self.get_sample_data()
        
        if df.empty:
            st.warning("No data available. Please check your data source.")
            return
        
        # Apply filters
        if controls['sentiment_filter']:
            df = df[df['sentiment'].isin(controls['sentiment_filter'])]
        
        if controls['source_filter']:
            df = df[df['source'].isin(controls['source_filter'])]
        
        # Render charts
        self.render_sentiment_overview(df)
        self.render_time_series(df)
        self.render_source_analysis(df)
        self.render_recent_messages(df)
        
        # Auto-refresh
        if controls['auto_refresh']:
            time.sleep(controls['refresh_interval'])
            st.rerun()

def main():
    """Main function to run the dashboard."""
    dashboard = SentimentDashboard()
    
    try:
        while True:
            dashboard.run()
    except KeyboardInterrupt:
        logger.info("Dashboard stopped by user")
    except Exception as e:
        logger.error(f"Dashboard error: {e}")
        st.error(f"An error occurred: {e}")
    finally:
        if dashboard.consumer:
            dashboard.consumer.close()
        dashboard.running = False

if __name__ == "__main__":
    main()

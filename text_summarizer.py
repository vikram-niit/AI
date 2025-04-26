import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict
import heapq

# Download necessary NLTK data (first time only)
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(text.lower())

    # Create a frequency table
    freq_table = defaultdict(int)
    for word in words:
        if word not in stop_words:
            freq_table[word] += 1

    # Score sentences based on word frequency
    sentences = sent_tokenize(text)
    sentence_scores = defaultdict(int)

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] += freq_table[word]

    # Select top N sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

# Example input
input_text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.
"""

# Generate summary
summary = summarize_text(input_text, num_sentences=2)
print("Summary:\n", summary)

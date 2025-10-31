# Import necessary libraries
from rake_nltk import Rake
import nltk


nltk.download('stopwords')


r = Rake()


text = """
Artificial Intelligence (AI) is transforming the world.
From healthcare to education, AI applications are everywhere.
Machine learning, a subset of AI, enables computers to learn from data
and make intelligent decisions without being explicitly programmed.
Natural Language Processing (NLP) helps computers understand human language.
"""


r.extract_keywords_from_text(text)


keywords = r.get_ranked_phrases_with_scores()


print("🔑 Extracted Keywords and Scores:\n")
for score, keyword in keywords:
    print(f"{score} - {keyword}")

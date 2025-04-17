import requests
from bs4 import BeautifulSoup
import spacy
from collections import Counter

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Example URL (modify for pagination)
url = "https://www.linkedin.com/jobs/search/?keywords=CyberSecurity"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job descriptions
text = soup.get_text()
doc = nlp(text)

# Filter for nouns + technology-related words
cybersecurity_terms = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"] and len(token.text) > 3]

# Remove irrelevant words manually (custom filtering)
irrelevant_words = {"linkedin", "week", "applicant", "states", "new", "days", "jobs",
                    "security", "analyst", "engineer", "team", "work", "company", "experience",
                    "role", "responsibilities", "skills", "job", "position", "location",
                    "apply", "salary", "benefits", "description", "requirements", "education",
                    "qualifications", "hours", "remote", "office", "full-time", "part-time",
                    "internship", "contract", "temporary", "employment", "opportunity",
                    "career", "development", "training", "program", "project", "leadership",
                    "cybersecurity", "specialist", "cyber", "weeks"}
filtered_terms = [word for word in cybersecurity_terms if word not in irrelevant_words]

# Count frequency
common_terms = Counter(filtered_terms).most_common(20)
print(common_terms)

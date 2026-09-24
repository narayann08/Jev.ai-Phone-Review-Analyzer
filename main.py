# 1. read the reviews CSV
# 2. anaylze every review with jev
# 3. print a flipkart-style summary

import csv
from questions import TOPICS
from analyzer import analyze_review
from aggregation import aggregate

INPUT_FILE = "synthetic_phone_reviews.csv"

with open(INPUT_FILE, encoding="utf-8") as f:
    reviews = list(csv.DictReader(f))

all_ratings = []
for review in reviews:
    ratings = analyze_review(review["review_text"])
    all_ratings.append(ratings)
    print(review["review_id"], ratings)

overall = sum(int(r["overall_rating"] for r in reviews) / len(reviews))
summary = aggregate(all_ratings)

print()
print(f"{overall:.1f} * based on {len(reviews)} ratings")
print("-" * 40)

for topic, info in summary.items():
    if info["average"] is None:
        print(f"{topic:<16} no ratings yet")
    else:
        print(f"{topic:<16} {info['average']:.1f} * ({info['count']} reviews)")


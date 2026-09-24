# Phone Review Analyzer

A lightweight Python pipeline that reads customer phone reviews, analyzes each one using [jev](https://typesafe.ai) (a structured AI model), and produces a topic-level rating summary — similar to what you see on Flipkart or Amazon product pages.

---

## What It Does

Most review analysis tools give you a single score or a blob of sentiment text. This project does something more useful: it breaks each review down into **7 specific topics** and rates them independently, only when the reviewer actually talks about that topic.

For a batch of reviews, the output looks like this:

```
4.1 * based on 50 ratings
----------------------------------------
Camera           3.8 * (34 reviews)
Battery          4.2 * (38 reviews)
Display          4.5 * (29 reviews)
Design           3.6 * (22 reviews)
Performance      4.0 * (31 reviews)
Build Quality    4.1 * (27 reviews)
Value for Money  3.5 * (35 reviews)
```

---

## How It Works

Each review goes through a two-question check per topic:

1. **Did the reviewer mention this topic?** — a `Noul` (0–1 confidence score) determines relevance
2. **How satisfied were they?** — a `Score` maps their sentiment to one of five satisfaction levels

Only reviews that clear the mention threshold are included in that topic's average. This avoids polluting ratings with reviews that never discussed the topic at all.

```
CSV Reviews
    │
    ▼
analyzer.py  ──► jev (14 structured questions per review)
    │
    ▼
aggregation.py  ──► per-topic averages
    │
    ▼
main.py  ──► printed summary
```

---

## Project Structure

```
jev-demo/
├── main.py                      # Entry point — reads CSV, runs pipeline, prints results
├── analyzer.py                  # Sends one review to jev, converts answers to star ratings
├── questions.py                 # Defines the 14 structured questions (7 topics × 2 questions)
├── aggregation.py               # Averages per-topic ratings across all reviews
├── synthetic_phone_reviews.csv  # 50 synthetic reviews for the Aster M1 5G
└── .env                         # API key (not committed)
```

---

## Topics Analyzed

| Topic | What jev looks for |
|---|---|
| Camera | Opinions on photos, videos, focusing |
| Battery | Battery life and charging experience |
| Display | Screen quality, brightness, readability |
| Design | Appearance, shape, ergonomics |
| Performance | Speed, responsiveness, gaming, multitasking |
| Build Quality | Materials, sturdiness, durability |
| Value for Money | Whether the price feels justified |

---

## Getting Started

### Prerequisites

- Python 3.9+
- A [TypeSafe](https://typesafe.ai) API key

### Installation

```bash
git clone https://github.com/narayann08/xyz.git
cd xyz
pip install typesafe-sdk python-dotenv
```

### Configuration

Create a `.env` file in the project root:

```
TYPESAFE_API_KEY=your_api_key_here
```

### Run

```bash
python main.py
```

The script reads `synthetic_phone_reviews.csv`, analyzes all 50 reviews, and prints the topic-level summary.

---

## The Dataset

`synthetic_phone_reviews.csv` contains 50 synthetic reviews for a fictional phone — the **Aster M1 5G** — written to cover a realistic range of opinions: mixed camera feedback, battery complaints, display praise, build quality concerns, and value-for-money debate. Reviews are written in both English and Hinglish to reflect real-world diversity.

---

## Dependencies

| Package | Purpose |
|---|---|
| `typesafe-sdk` | jev client for structured AI inference |
| `python-dotenv` | loads `TYPESAFE_API_KEY` from `.env` |

---

## License

MIT

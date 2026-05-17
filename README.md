# SSD DataPath

AI-powered learning recommendation and assessment platform for NPC-SSD data professionals.

---

# Overview

SSD DataPath is a Streamlit-based enterprise learning intelligence platform designed to:

* Recommend personalized learning resources
* Generate AI-powered assessment questions
* Evaluate learner competency
* Track learner assessment history
* Support workforce upskilling initiatives
* Provide scalable metadata-driven learning management

The platform combines:

* AI-generated learning summaries
* AI-generated recommendation explanations
* AI-generated assessment question banks
* Persistent learner assessment history
* Enterprise-oriented learning metadata

---

# Core Features

## Learning Recommendations

* Personalized learning recommendations
* Metadata-driven filtering
* Learning track selection
* Skill-based recommendations
* Difficulty-level filtering
* Platform-category filtering
* AI-generated course summaries
* AI-generated recommendation explanations

## Skill Assessment

* AI-generated assessment question banks
* Randomized question selection
* Multiple technical domains
* Question review and explanations
* Learner tracking
* Persistent assessment history
* Enterprise-oriented assessments

## Learner Intelligence Foundation

* Assessment history persistence
* Skill-level tracking
* Performance scoring
* Extensible analytics architecture

---

# Supported Learning Domains

* SQL
* Informatica IDMC
* Databricks
* Python for Data Engineering
* Spark / PySpark
* SQL for Data Science
* Oracle APEX Development
* Power BI
* Oracle BI
* Statistical Analysis
* OCI Core Services
* OCI Architecture
* OCI Autonomous Database
* Oracle AI & Analytics

---

# Technology Stack

| Component         | Technology          |
| ----------------- | ------------------- |
| Frontend          | Streamlit           |
| Backend Logic     | Python              |
| Data Storage      | CSV                 |
| AI Generation     | OpenAI API          |
| Data Processing   | Pandas              |
| Assessment Engine | JSON Question Banks |

---

# Project Structure

```text
AI-Learning-Recommendation-Platform/
│
├── app.py
├── generate_course_summaries.py
├── generate_assessment_sources.py
├── generate_assessment_questions.py
│
├── logic/
│   └── recommender.py
│
├── pages/
│   ├── 1_Learning_Recommendations.py
│   ├── 2_Skill_Assessment.py
│   └── 3_Learner_Analytics.py
│
├── data/
│   ├── courses.csv
│   ├── assessment_sources.csv
│   ├── generated_questions.json
│   └── assessment_history.csv
│
├── assets/
│   └── logo.png
│
└── README.md
```

---

# courses.csv Schema

The platform uses `courses.csv` as the master metadata repository.

Recommended columns:

```text
course_id
career_track
skill
course_name
provider
learning_style
url
duration_hours
is_free
ai_summary
ai_recommendation_reason
difficulty_level
estimated_weeks
certification_related
tags
prerequisites
platform_category
assessment_enabled
assessment_source_url
assessment_knowledge_text
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd AI-Learning-Recommendation-Platform
```

---

## 2. Create Virtual Environment

### Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt does not exist yet:

```bash
pip install streamlit pandas openai
```

---

# OpenAI API Configuration

## 1. Create API Key

Create OpenAI API key from:

[https://platform.openai.com/](https://platform.openai.com/)

---

## 2. Configure Environment Variable

### Linux / Mac

```bash
export OPENAI_API_KEY="your_api_key"
```

### Windows

```bash
set OPENAI_API_KEY=your_api_key
```

---

# Initial Application Setup Workflow

If running the application from scratch, follow the sequence below.

---

# STEP 1 — Prepare courses.csv

Populate:

```text
data/courses.csv
```

with:

* learning tracks
* skills
* metadata
* URLs
* assessment knowledge
* AI-generated fields

This is the master metadata file.

---

# STEP 2 — Generate AI Course Summaries

Run:

```bash
python generate_course_summaries.py
```

This generates:

* ai_summary
* ai_recommendation_reason

inside:

```text
courses.csv
```

---

# STEP 3 — Generate Assessment Sources

Run:

```bash
python generate_assessment_sources.py
```

This generates:

```text
data/assessment_sources.csv
```

from:

```text
courses.csv
```

Assessment sources are automatically deduplicated by skill.

---

# STEP 4 — Generate Question Bank

Run:

```bash
python generate_assessment_questions.py
```

This generates:

```text
data/generated_questions.json
```

The question bank contains:

* AI-generated questions
* multiple choice options
* correct answers
* explanations

Question generation uses:

* skill
* difficulty
* tags
* prerequisites
* assessment knowledge
* documentation references
* platform category

---

# STEP 5 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# Application Pages

## Home

Platform overview and navigation.

## Learning Recommendations

Personalized course recommendation engine.

## Skill Assessment

AI-generated assessment platform.

## Learner Analytics

Assessment history and learner intelligence.

---

# Assessment Workflow

1. Learner enters:

   * Name
   * Email

2. Learner selects:

   * Learning Track
   * Skill
   * Question Count

3. AI-generated question bank is randomized.

4. Assessment is completed.

5. Results are stored in:

```text
data/assessment_history.csv
```

---

# Persistent Assessment Storage

Assessment attempts are automatically stored in:

```text
data/assessment_history.csv
```

Stored fields include:

* timestamp
* learner_name
* learner_email
* learning_track
* skill
* score
* percentage

---

# Future Roadmap

Planned enhancements:

* Learner analytics dashboard
* Skill-gap intelligence
* Personalized AI coaching
* SQLite integration
* Authentication system
* Downloadable assessment reports
* AI learning roadmap generation
* Advanced enterprise analytics
* RAG-based assessment generation

---

# Deployment

The platform can be deployed using:

* Streamlit Community Cloud
* Azure App Service
* Docker
* Kubernetes
* OCI Compute

---

# Recommended Architecture Evolution

```text
CSV
→ SQLite
→ PostgreSQL / Cloud Database
```

---

# License

Internal enterprise learning platform prototype.

---

# Author

SSD DataPath Development Initiative

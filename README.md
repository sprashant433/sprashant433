# 👋 Hey, I'm Prashant Singh

### AI/ML Engineer | MLOps | GenAI & LLM Engineering | Distributed Systems

📍 Bengaluru, India

AI/ML Engineer with **5+ years of experience** designing and shipping production-grade ML systems, scalable data pipelines, and Generative AI applications on **Google Cloud Platform**. My work spans the full ML lifecycle: data and feature engineering, model development, deployment, monitoring, and production optimization.

- 🤖 **Machine Learning & MLOps:** production ML systems, experiment tracking, model registry, CI/CD, observability
- 🧠 **GenAI & LLMs:** RAG, AI Agents, MCP, fine-tuning (LoRA, QLoRA, SFT), LLM applications
- ⚡ **Distributed Systems:** real-time inference, Redis, Cassandra, Apache Spark
- ☁️ **Cloud:** GCP, Vertex AI, BigQuery, Dataproc, Dataflow
- 🏆 **2x Google Cloud Certified:** Professional ML Engineer and Associate Cloud Engineer

---

## 🔭 What I'm Currently Working On

- Building and maintaining production ML pipelines using **Vertex AI and Apache Airflow**
- Implementing experiment tracking, model registry, and feature management workflows
- Improving ML reliability through monitoring, alerting, RCA, and production hardening
- Exploring advanced GenAI architectures: RAG, MCP, agents, and efficient LLM fine-tuning

---

## 💼 Professional Experience

### 🧑‍💻 AI Engineer: Fractal Analytics Limited
📍 Bengaluru, India | May 2026 – Present

**Fraud Detection AI Platform (Retail Client)**

- Built ML batch inference and training **Airflow DAGs** on GCP using **Vertex AI Experiments, Model Registry, and Feature Store**
- Own ML pipeline reliability: monitoring, alerting, RCA, and production hardening
- Authored RCA documentation and L2/L3 troubleshooting runbooks, **reducing repeat-incident resolution time by 30%**
- Contributed to CI/CD and release readiness for ML components using **GitHub Actions**

### 🧑‍💻 Senior Machine Learning Engineer: Horizontal Integration India
📍 Bengaluru, India | Nov 2025 – May 2026

**Equinox: Real-Time Promotional Forecasting Platform (Retail Client)**

- Architected a real-time ML inference API scoring **1M+ items in a single request at sub-60s P99 latency** using FastAPI, Redis Cluster, and Cassandra
- Designed Cassandra data models and Spark ingestion pipelines for a **44.8M-row dataset**
- Built a Redis caching layer with hash structures and asyncio pipeline batching, cutting Cassandra read load by **~60%** and response time from **320ms to under 90ms**
- Built a reproducible MLOps lifecycle with **PySpark, MLflow, and Vertex AI Model Registry**, plus **WMAPE-based automated retraining triggers** (20% degradation threshold)
- Containerized with Docker and Artifact Registry, automated deployments with Cloud Build, and added logging and alerting via Cloud Logging and Cloud Monitoring

<details>
<summary><b>🧑‍💻 Data Engineer: SAS2PY Software Private Limited</b> | Oct 2023 – Oct 2025 | Hyderabad</summary>

<br>

**Feature Store Platform (Telecom Client)**

- Led a team of 3 to deliver an **offline + online Feature Store using Feast on GCP**, serving **10+ ML pipelines** and eliminating duplication that caused 15%+ training/serving skew
- Built PySpark ETL pipelines across BigQuery, GCS, Cloud SQL, and Dataproc, processing TBs per batch within a 2-hour SLA
- Delivered a **RAG-based AI assistant (LangChain)** for Feature Store Q&A, cutting data scientist onboarding from **3 weeks to 5 days**
- Built CI/CD pipelines with Docker, Cloud Build, and Cloud Composer for automated deployments

**Banking Data Modernization (Banking Client)**

- Re-engineered **200+ legacy batch programs** into PySpark jobs on Dataproc Serverless, achieving a **3x runtime reduction** with zero regression validated through systematic output comparison
- Built an **Apache Beam Dataflow pipeline** ingesting third-party API data into Snowflake, cutting execution time by **66%**

</details>

<details>
<summary><b>🧑‍💻 Software Engineer: TEKsystems Global Services</b> | Aug 2021 – Oct 2023 | Bengaluru</summary>

<br>

**Google Cortex Framework: SAP AR Risk Assessment**

- Built ML models for accounts receivable risk scoring and payment-date prediction, **reducing manual dunning effort by 40%** and flagging high-risk invoices with **87% precision**
- Built BigQuery views and CDC workflows for near-real-time SAP-to-BigQuery data propagation

**Product Catalogue Search & Recommendations AI**

- Built semantic product search using Google LLMs on Vertex AI with dense vector embeddings, achieving **sub-50ms retrieval across a 500K+ product catalogue**
- Extracted metadata from product images using vision-language models, **improving search recall by 22%**
- Deployed Recommendations AI, Vision API Product Search, and Retail Search

</details>

---

## 🚀 Key Projects

| Project | Highlights | Tech |
|---|---|---|
| **Real-Time Promotional Forecasting (Equinox)** | 1M+ items per request, sub-60s P99, response time 320ms → <90ms, ~60% less DB read load | FastAPI, Redis Cluster, Cassandra, PySpark, MLflow, Vertex AI |
| **Enterprise Feature Store + RAG Assistant** | Offline + online store serving 10+ pipelines, onboarding 3 weeks → 5 days | Feast, BigQuery, PySpark, LangChain, Docker |
| **Banking Data Modernization** | 200+ programs migrated to PySpark (3x faster), Beam → Snowflake pipeline 66% faster | PySpark, Apache Beam, Dataflow, Dataproc, Snowflake |
| **Product Catalogue Semantic Search** | Sub-50ms retrieval over 500K+ products, +22% search recall | Vertex AI, Google LLMs, Vector Embeddings, Vision API |

---

## ⚙️ Technical Skills

### 🤖 Generative AI & LLMs

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat&logo=huggingface&logoColor=black)

OpenAI SDK • LangChain • Hugging Face • Transformers • RAG (Vector & Vectorless) • AI Agents • MCP • Prompt Engineering • LoRA • QLoRA • SFT • Vector Embeddings • LLM Leaderboards

### 🧠 Machine Learning & MLOps

![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)

Supervised Learning • Feature Engineering • Model Selection • Hyperparameter Tuning • MLflow • Vertex AI Experiments • Model Registry • Feature Stores (Feast) • NLP • Model Optimization

### ☁️ Cloud & GCP

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat&logo=googlecloud&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=flat&logo=googlebigquery&logoColor=white)

Vertex AI • BigQuery • BQML • Dataflow • Dataproc • Pub/Sub • Cloud Storage • Cloud Composer • Cloud Build • Compute Engine • Cloud SQL • Cloud Bigtable

### ⚡ Distributed Systems & Big Data

![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Apache Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=flat&logo=apachehadoop&logoColor=black)

PySpark • Hadoop • Hive • Apache Beam • Redis Cluster

### 🗄️ Databases & Storage

Cassandra • Redis • Dragonfly • MySQL • PostgreSQL • Aerospike • Snowflake • FAISS • Chroma • GCP Vector Store

### 🛠️ DevOps

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

Docker • Kubernetes (working knowledge) • Git • GitHub Actions • CI/CD • Airflow • Cloud Build

### 💻 Programming & Frameworks

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)

Python • C++ • FastAPI • Flask • Django • Streamlit • Gradio

**Libraries:** Scikit-learn • Pandas • NumPy • Matplotlib • SpaCy • Gensim

---

## 📜 Certifications

- 🏆 [Google Cloud Professional Machine Learning Engineer](https://www.credly.com/badges/29ad86cf-03de-48cf-9725-dec23f909680/public_url)
- 🏆 [Google Cloud Associate Cloud Engineer](https://www.credly.com/badges/ccfeedaa-020f-4ce4-a6a1-583185574394/public_url)

---

## 🎓 Education

**B.Tech in Computer Science**, Haldia Institute of Technology, West Bengal, India
Jul 2017 – Jul 2021 | DGPA: **9.08 / 10 (83.3%)**

---

## 🤝 Let's Connect

<p align="left">
  <a href="mailto:sprashant433@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://github.com/sprashant433">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://drive.google.com/file/d/16Jl1yjOhlhBoLyuSl1V18k7UOHu5-VCg/view?usp=sharing">
    <img src="https://img.shields.io/badge/Resume-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Resume" />
  </a>
</p>

---

⭐ **Always interested in discussing Machine Learning, MLOps, Generative AI, LLM systems, and scalable distributed architectures.**

*Building intelligent systems. Scaling ML in production.*

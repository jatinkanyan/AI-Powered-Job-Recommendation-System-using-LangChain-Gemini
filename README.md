# 💼 AI Job Recommendation System

## Project Overview
This project is a smart job helper app that uses AI to recommend jobs for people based on their skills, experience, and preferences. You tell it what you can do and what kind of job you want, and it finds matching job openings for you!

---

## Features
- Enter your skills, experience, and job preferences in a simple text box.
- The AI searches through stored job postings to find the best matches.
- Shows recommended jobs with job title, company, and location.
- Lets you see the original job descriptions for more details.

---

## How It Works (Architecture)

1. **User Input:** You type in your skills and job preferences.
2. **Embedding:** The app converts your input into numbers (vectors) that the AI can understand.
3. **Search:** It searches a database of job postings using these vectors to find similar job descriptions.
4. **Answer Generation:** An AI language model reads the search results and writes job recommendations in easy bullet points.
5. **Display:** The app shows the recommended jobs on the screen.

---

## Data Source

- The job postings data is stored locally in a **Chroma vector database**.
- You can add more job postings by updating this database with new data.

---

## How to Build or Update the Job Database

1. Collect job postings in text format.
2. Use the embedding function (`GoogleGenerativeAIEmbeddings`) to convert each job posting into vectors.
3. Add these vectors to the Chroma database (`jobs_chroma_db` directory).
4. This lets the app find new jobs during search.

---

## Environment Setup and Variables

Before running the app, you need:

- Python installed (version 3.7 or higher recommended)
- Install required packages:
  ```bash
  pip install -r requirements.txt

-How to Run the App
Open a terminal or command prompt.

Navigate to the project directory.

Run the Streamlit app with:

bash
Copy
Edit
streamlit run app.py
The app will automatically open in your default web browser.

Enter your skills and job preferences in the input box.

Click the Get Recommendations button to see job suggestions.

How It Works
The app creates embeddings for job postings using Google's embedding model.

Job data is stored and searched efficiently using Chroma vector database.

When a user inputs their profile, the app converts it into an embedding.

The most relevant job postings are retrieved based on similarity.

A Google Generative AI language model generates readable recommendations from these results.

Example Input
css
Copy
Edit
Skills: Python, SQL, Excel; Experience: 0 years; Looking for Data Analyst roles in Canada


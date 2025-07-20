# WhisperBoard

📝 **Anonymous Feedback and Suggestion Collection Application**

WhisperBoard is a simple app to collect **anonymous feedback, ratings, and suggestions** from users, built using **Python** and **Supabase**.

---

## 🚀 Use Cases

✅ **Quick Feedback Collector**

- For small businesses, workshops, classes
- Collects **name (optional)**, **rating (1-5)**, and **comments**

✅ **Anonymous Suggestion Box**

- For teams, classes, or organisations
- Users submit suggestions **without revealing identity**

---

## ✨ Features

### Feedback Collector

- 🗳️ Submit **Name, Rating (1-5), and Comments**
- 💾 Data stored securely in **Supabase table: `feedback`**
- 👨‍💻 **Admin page** to view recent feedback
- 🔍 *(Optional)* **Basic Sentiment Analysis** using keyword spotting for quick insights

#### Feedback Table Schema

| Column    | Type       |
|-----------|------------|
| id        | UUID       |
| name      | Text       |
| rating    | Integer    |
| comment   | Text       |
| timestamp | Timestamp  |

---

### Anonymous Suggestion Box

- 📝 Users submit **anonymous suggestions**
- 👨‍💻 **Admin page** to view suggestions easily

#### Suggestions Table Schema

| Column       | Type       |
|--------------|------------|
| id           | UUID       |
| content      | Text       |
| submitted_at | Timestamp  |

---

## 🔧 Tech Stack

- **Backend:** Python
- **Database:** Supabase Postgres
- *(Optional)* Sentiment Analysis: Basic keyword-based approach

---

## 💡 How to Use

1. **Clone this repo:**

   ```bash
   https://github.com/abhijeetsahu09/whisperBoard.git
   cd whisperBoard

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Setup Supabase credentials:**

Create a .env file

Add your Supabase URL and Key:

    ```bash
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key

3. **Run the app:**

 ```bash
 python app.py


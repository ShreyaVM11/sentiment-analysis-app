# 💬 AI-Powered Customer Feedback & Sentiment Analysis System

An intelligent, full-stack Flask web application for collecting customer feedback, performing real-time sentiment analysis using **NLTK VADER** and **TextBlob**, and visualizing actionable insights through an interactive **Admin Dashboard**.

---

## 🚀 Key Features

- **Multi-Modal Feedback Collection:**
  - Standard text feedback form with instant submission.
  - 🎤 **Voice-to-Text Input** using the browser Web Speech API.
  - ⚡ **Quick Reaction Buttons** (👍/👎 and 5 emotion emojis: 😡, ☹, 😐, 😊, 😃).
- **Dual-Engine Sentiment Analysis:**
  - Evaluates sentiment polarity and compound scores using **NLTK VADER** and **TextBlob**.
  - Classifies responses into **Positive**, **Neutral**, or **Negative**.
- **Admin Dashboard & Visual Analytics:**
  - Secure Admin authentication portal (`/login`).
  - Real-time sentiment percentage overview and feedback count cards.
  - Interactive distribution charts powered by **Chart.js** (Pie and Bar charts).
  - Searchable and filterable feedback record table.
  - 📥 **Export to PDF** (with jsPDF & AutoTable) and **CSV export** for reporting.
- **Configurable Database & Credentials:**
  - Externalized configuration in a dedicated `config/` directory.
  - Database password, admin credentials, and secret keys managed via environment variables or `.env`.

---

## 📁 Project Structure

```plaintext
Sentiment app/
├── app.py                      # Main Flask application and routing logic
├── app.spec                    # PyInstaller build specification
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment variables template
├── .gitignore                  # GitHub ignore rules (blocks 600MB+ build artifacts & secrets)
├── feedback.csv.example        # Sample CSV data structure
├── config/                     # 🔐 Externalized credentials & DB configuration
│   ├── __init__.py
│   ├── db_config.py            # Active database & admin configuration loader
│   └── db_config.example.py    # Template for database & admin credentials
├── static/
│   ├── css/
│   │   └── style.css           # Styling for feedback forms and components
│   └── images/                 # Static assets, branding, and backgrounds
└── templates/
    ├── feedback.html           # Customer feedback submission page (Home)
    ├── index.html              # Alternative feedback interface
    ├── login.html              # Admin authentication page
    ├── dashboard.html          # Interactive analytics dashboard
    └── results.html            # Feedback record viewing and filtering
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13 installed.
- Git installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd "Sentiment app"
```

### 3. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Database & Password Configuration

All sensitive passwords, database settings, and admin credentials are kept separated in the `config/` folder to ensure security when uploading to GitHub.

### Option A: Using `.env` (Recommended)
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and set your credentials:
   ```env
   # Admin Credentials
   ADMIN_USERNAME=Admin
   ADMIN_PASSWORD=your_secure_password
   SECRET_KEY=your_secret_session_key

   # Database Configuration
   DB_TYPE=csv
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=your_actual_db_password
   DB_NAME=sentiment_db
   ```

### Option B: Modifying `config/db_config.py` Directly
You can edit [`config/db_config.py`](config/db_config.py) directly on your local machine. Because `.env` and sensitive local files are listed in `.gitignore`, your passwords will remain private and won't be pushed to GitHub.

---

## ▶️ Running the Application

Start the Flask server:
```bash
python app.py
```

- **Customer Feedback Portal:** [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Admin Login:** [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)
  - Default Username: `Admin`
  - Default Password: `your_password_configured_in_config` (default: `1110`)

---

## 🚀 How to Upload to GitHub

Follow these steps to upload this project to your GitHub account:

### Step 1: Initialize Git in your project folder
```bash
git init
```

### Step 2: Stage and commit the clean project files
The `.gitignore` will automatically exclude the 600MB+ `build/` and `dist/` folders and sensitive data.
```bash
git add .
git commit -m "Initial commit: AI Sentiment Analysis web application"
```

### Step 3: Create a new repository on GitHub
1. Go to [GitHub New Repository](https://github.com/new).
2. Enter a repository name (e.g. `sentiment-analysis-app`).
3. Leave "Initialize this repository with a README" **unchecked** (we already have one).
4. Click **Create repository**.

### Step 4: Link your local repository and push
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sentiment-analysis-app.git
git push -u origin main
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

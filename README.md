🤖 QuickQuery-AI

QuickQuery-AI is a Flask-based AI chatbot web application that allows users to ask questions and receive intelligent, real-time responses using the OpenAI API.
It features a simple and clean user interface for seamless interaction.

🚀 Features

💬 AI-powered chatbot for instant responses

🌐 Web-based interface using Flask

🔐 Secure API key management using environment variables

⚡ Fast and lightweight backend

🎨 Simple HTML-based UI

🛠️ Tech Stack

Backend: Python, Flask

AI Model: OpenAI API

Frontend: HTML, CSS

Environment Management: python-dotenv

Version Control: Git & GitHub

📂 Project Structure
QuickQuery-AI/
│
├── app.py
├── templates/
│   └── index.html
├── .gitignore
├── README.md
└── .env   (not pushed to GitHub)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/NANCYGAUTAM78/QuickQuery-AI.git
cd QuickQuery-AI

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install flask openai python-dotenv

4️⃣ Configure OpenAI API Key

Create a .env file in the project root and add:

OPENAI_API_KEY=your_openai_api_key_here


⚠️ Never share or push this file to GitHub.

5️⃣ Run the application
python app.py


Open browser:

http://127.0.0.1:5000/





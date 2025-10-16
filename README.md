# 📧 Cold Traffic Email Generator using LLMs  

Generate highly personalized cold emails for businesses using **Groq**, **LangChain**, and **Streamlit** — powered by your own portfolio data.  

---

## 🚀 Project Overview  

This project is an **AI-powered cold email generator** designed for service-based companies.  
It allows users to input the **URL of a company’s careers page**, extracts job listings from that page, and then generates **customized cold emails** that highlight relevant skills and portfolio examples.  

### 🧠 How It Works  
1. **Input a Careers Page URL**  
   - Example: `https://www.hellowork.com/fr-fr/emploi/recherche.html?k=AI&k_autocomplete=&l=&l_autocomplete=`  
2. **Job Extraction**  
   - The app scrapes the page and extracts key job information (title, responsibilities, requirements).  
3. **Portfolio Matching**  
   - It compares the job description with entries in your **vector database (portfolio.csv)** to find relevant projects.  
4. **Email Generation**  
   - It generates a personalized email pitch using Groq + LangChain.  

---

## 💡 Example Use Case  

Imagine:  
company  is hiring a *Principal Software Engineer* and spending resources on recruitment.  
Your company  offers software development services.  
Using this tool, your business development executive (e.g., *Nexora*) can generate a personalized cold email to pitch the company’s services — showing relevant past work and expertise.  

---

## 🖥️ App Interface  

The interface is built with **Streamlit** for a clean and interactive experience.  

Features include:
- Elegant UI with custom layout and icons  
- URL input for job listings  
- “Generate” button for easy workflow  
- AI-generated output displayed in a styled email preview box  

---

## ⚙️ Tech Stack  

| Component | Description |
|------------|-------------|
| **Groq** | LLM API used to generate email text |
| **LangChain** | Manages prompt templates and LLM chains |
| **Streamlit** | Frontend web interface |
| **ChromaDB** | Vector database for storing and matching portfolio embeddings |
| **BeautifulSoup4** | For web scraping job listings |
| **Python** | Core language for logic and orchestration |



---

## 🧠 Setup Instructions  

### 1️⃣ Clone the Repository

git clone https://github.com/fouratkandil/Cold-Traffic-email-LLMS-.git

cd Cold-Traffic-email-LLMS-

2️⃣ Create a Virtual Environment

python -m venv venv

venv\Scripts\activate    # on Windows

source venv/bin/activate # on Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Add Environment Variables
Create a file named .env in the project root and add your Groq key:

GROQ_API_KEY=your_groq_api_key_here

⚠️ Never hardcode API keys inside notebooks or scripts.


5️⃣ Run the App

streamlit run app/main.py
---

📸 Preview
Check the demo video 
🧰 Future Improvements
Add multiple job link support

Integrate email sending (SMTP or Gmail API)

Support multilingual cold emails

Add analytics dashboard for sent emails
---
🧑‍💻 Author
Fourat Kandil
🎓 Student Engineer in Computer Science | 💡 Passionate about AI, Data, and Automation
🔗 LinkedIn | GitHub
---
📜 License
This project is licensed under the MIT License.




                                # -Mini-Text-Summarizer-

A desktop-based Text Summarization tool built using Python and Tkinter. This application allows users to load or input text, specify the number of sentences for the summary, and generate a concise summary of the input content. The UI features a clean layout with gradient backgrounds and is user-friendly for all levels.

🔧 Features
📂 Open Text File: Load .txt files directly from your system.

✍️ Manual Text Input: Paste or type text in the input area.

🧠 Summarize: Generate a summary based on the most important sentences.

🔢 Custom Summary Length: Choose how many sentences should be in the summary.

💾 Save Summary: Save the generated summary as summary.txt.

🎨 Gradient UI: Aesthetic user interface with a colorful gradient background.

📁 File Structure
graphql
Copy code
.
├── python2.py       # Main source code with GUI and summarization logic
├── summary.txt      # Output file saved after summarizing (created after use)
└── README.md        # Project documentation
🚀 Getting Started
✅ Prerequisites
Make sure you have Python 3.x installed.

📦 Dependencies
No external libraries required. Only standard Python libraries are used:

* tkinter

* collections

* string

* re



🧠 How It Works


* The input text is tokenized into sentences and cleaned of stopwords and punctuation.

* Words are counted using Counter to build frequency scores.

* Each sentence is scored based on the frequency of its words.

* The top N highest scoring sentences are returned in the original order.

![Screenshot 2025-05-31 234419](https://github.com/user-attachments/assets/1637103d-f105-43c0-be2c-08f1701b3071)


📌 Limitations

* Only supports .txt files.

* No advanced NLP techniques (e.g., BERT, LLMs) – purely frequency-based.

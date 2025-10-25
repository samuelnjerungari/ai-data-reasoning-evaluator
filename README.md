AI Data Reasoning Task Evaluator
Overview
This project simulates how AI models are tested for reasoning and data-science skills — similar to the evaluation workflow used in Project Agate (Pareto.AI). It designs a realistic data-analysis challenge, generates synthetic data, creates sample AI model answers, and grades them automatically using a rubric-based scoring system.
What It Does
•	Dataset Creation – builds a fake hospital dataset (patients.csv).
•	Task Design – defines a reasoning challenge for AI models.
•	Model Simulation – saves example model outputs.
•	Rubric Design – sets up weighted scoring criteria.
•	Automated Grading – runs grading_script.py to score answers.
•	Visualization – plots a bar chart comparing model scores.
Tech Stack
• Python 3.10
• pandas, numpy, matplotlib, Jupyter Notebook
• VS Code + Jupyter Extension
Example Output
🧾 Evaluation Report:
model_name   final_score
AI_Model_1   100.0
AI_Model_2    20.0
Visualization
The chart below shows a visual comparison of model performance:
 
How to Run
# 1. Clone or download this repo
cd ai-data-reasoning-evaluator

# 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the grader
python grading_script.py
Why This Project Matters
AI alignment and reasoning QA rely on robust evaluation design. This project demonstrates how to:
- Design data-reasoning tasks
- Build grading rubrics
- Automate evaluation & reporting
- Communicate results visually
Author
Samuel Njeru Ngari
Clinical NLP & Annotation QA Specialist
GitHub Profile: https://github.com/samuelnjerungari
LinkeIn: www.linkedin.com/in/samuel-n-ngari



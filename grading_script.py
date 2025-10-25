import pandas as pd

# Load the dataset and model answers
df = pd.read_csv("patients.csv")
models = pd.read_csv("model_output_sample.csv")

# Calculate the true readmission rate
true_rate = (df["readmitted"].value_counts(normalize=True).get("Yes", 0)) * 100

# Find the most common diagnosis among readmitted patients
most_common_diag = df[df["readmitted"] == "Yes"]["diagnosis"].mode()[0]

results = []

# Go through each model answer and give it a score
for _, row in models.iterrows():
    score = 0

    # 1️⃣ Correct Metric Calculation (±10% tolerance)
    model_rate = int(row["q1_readmission_rate"].replace("%", ""))
    if abs(model_rate - true_rate) <= 10:
        score += 0.4

    # 2️⃣ Logical Reasoning (diagnosis match)
    if row["q2_common_diagnosis"].strip().lower() == most_common_diag.lower():
        score += 0.3

    # 3️⃣ Clarity & Completeness (at least 3 words)
    if len(row["q3_action_suggestion"].split()) >= 3:
        score += 0.2

    # 4️⃣ Actionability (checks for realistic keywords)
    if any(word in row["q3_action_suggestion"].lower() for word in ["improve", "monitor", "educate", "reduce", "track"]):
        score += 0.1

    results.append({
        "model_name": row["model_name"],
        "final_score": round(score * 100, 2)
    })

# Turn results into a table
report = pd.DataFrame(results)

# Save as CSV
report.to_csv("evaluation_report.csv", index=False)

# Show final scores
print("\n🧾 Evaluation Report:")
print(report)
print("\nReport saved as evaluation_report.csv ✅")

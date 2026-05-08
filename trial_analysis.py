import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Clinical Trial Data Generation (Dummy)
# Maano hum 'Drug-X' test kar rahe hain Blood Pressure control ke liye
np.random.seed(42)
data_size = 250

clinical_data = {
    'Patient_ID': range(1001, 1001 + data_size),
    'Age': np.random.randint(25, 75, data_size),
    'Gender': np.random.choice(['Male', 'Female'], data_size),
    'Group': np.random.choice(['Placebo', 'Drug-X'], data_size),
    'BP_Baseline': np.random.randint(140, 185, data_size), # Treatment se pehle ka BP
    'BP_Post_Treatment': np.random.randint(110, 160, data_size), # Treatment ke baad ka BP
    'Adverse_Effects': np.random.choice(['None', 'Headache', 'Nausea', 'Dizziness'], data_size, p=[0.7, 0.1, 0.1, 0.1])
}

df_trial = pd.DataFrame(clinical_data)

# 2. Key Metric Calculation: BP Reduction
df_trial['BP_Reduction'] = df_trial['BP_Baseline'] - df_trial['BP_Post_Treatment']

# 3. Statistical Summary (Analysis)
summary = df_trial.groupby('Group').agg({
    'BP_Reduction': ['mean', 'std', 'max'],
    'Age': 'mean'
}).reset_index()

print("--- Clinical Trial Summary Report ---")
print(summary)

# 4. Efficacy Check Logic
drug_efficacy = df_trial[df_trial['Group'] == 'Drug-X']['BP_Reduction'].mean()
placebo_efficacy = df_trial[df_trial['Group'] == 'Placebo']['BP_Reduction'].mean()

print(f"\nAverage BP Reduction (Drug-X): {drug_efficacy:.2f} mmHg")
print(f"Average BP Reduction (Placebo): {placebo_efficacy:.2f} mmHg")

if drug_efficacy > (placebo_efficacy + 5):
    print("\nResult: ✅ Drug-X shows significant efficacy over Placebo.")
else:
    print("\nResult: ⚠️ Drug-X efficacy is comparable to Placebo. Further testing needed.")

# 5. Data Visualization (Portfolio ke liye zaruri hai)
plt.figure(figsize=(10,6))
sns.boxplot(x='Group', y='BP_Reduction', data=df_trial, palette='Set2')
plt.title('Efficacy Comparison: Drug-X vs Placebo')
plt.ylabel('Blood Pressure Reduction (mmHg)')
plt.show()

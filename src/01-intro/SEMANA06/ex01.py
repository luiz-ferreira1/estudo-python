import pandas as pd
df = pd.read_csv("src/01-intro/SEMANA06/classification_results_trial_0001.csv")
contagem = df["real_class"].value_counts()
print(contagem)
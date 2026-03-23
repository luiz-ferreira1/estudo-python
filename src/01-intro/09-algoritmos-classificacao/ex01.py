import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# 1. Leitura da base de dados
df = pd.read_csv("src/01-intro/09-algoritmos-classificacao/StudentPerformanceFactors.csv")

print("Primeiras linhas da base:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

print("\nValores ausentes por coluna:")
print(df.isnull().sum())

print("\nDescrição estatística:")
print(df.describe())



#IMPORTANTE: esse dataset tem colunas categóricas
# vamos transformar em números

le = LabelEncoder()

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = le.fit_transform(df[col])



# 2. Histogramas
df.hist(figsize=(15, 10))
plt.suptitle("Histogramas da base Student Performance")
plt.tight_layout()
plt.show()



# 3. Definir target
# aqui você precisa escolher a variável alvo
# Exemplo comum: "Exam_Score" (ajuste se necessário)

target = "Exam_Score"

X = df.drop(target, axis=1)
y = df[target]



# Se for regressão (nota contínua), transformamos em classificação
# Exemplo: acima da média = 1, abaixo = 0

y = (y > y.mean()).astype(int)



# 4. Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)



# 5. Valores ausentes
imputer = SimpleImputer(strategy="mean")

X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)



# 6. Padronização
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



# 7. Modelos
modelo_logistico = LogisticRegression(max_iter=1000, random_state=42)
modelo_knn = KNeighborsClassifier(n_neighbors=5)
modelo_arvore = DecisionTreeClassifier(random_state=42, max_depth=5)
modelo_floresta = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)



# 8. Treinamento
modelo_logistico.fit(X_train_scaled, y_train)
modelo_knn.fit(X_train_scaled, y_train)
modelo_arvore.fit(X_train, y_train)
modelo_floresta.fit(X_train, y_train)



# 9. Previsões
y_pred_logistico = modelo_logistico.predict(X_test_scaled)
y_pred_knn = modelo_knn.predict(X_test_scaled)
y_pred_arvore = modelo_arvore.predict(X_test)
y_pred_floresta = modelo_floresta.predict(X_test)



# 10. Avaliação
def avaliar_modelo(nome, y_real, y_prev):
    print("\n==============================")
    print(f"Modelo: {nome}")
    print("==============================")
    print("Acurácia:", accuracy_score(y_real, y_prev))
    print("Precisão:", precision_score(y_real, y_prev))
    print("Recall:", recall_score(y_real, y_prev))
    print("F1-score:", f1_score(y_real, y_prev))
    print("\nRelatório de classificação:")
    print(classification_report(y_real, y_prev))

avaliar_modelo("Regressão Logística", y_test, y_pred_logistico)
avaliar_modelo("KNN", y_test, y_pred_knn)
avaliar_modelo("Árvore de Decisão", y_test, y_pred_arvore)
avaliar_modelo("Random Forest", y_test, y_pred_floresta)



# 11. Tabela comparativa
resultados = {
    "Modelo": ["Regressão Logística", "KNN", "Árvore de Decisão", "Random Forest"],
    "Acurácia": [
        accuracy_score(y_test, y_pred_logistico),
        accuracy_score(y_test, y_pred_knn),
        accuracy_score(y_test, y_pred_arvore),
        accuracy_score(y_test, y_pred_floresta)
    ],
    "Precisão": [
        precision_score(y_test, y_pred_logistico),
        precision_score(y_test, y_pred_knn),
        precision_score(y_test, y_pred_arvore),
        precision_score(y_test, y_pred_floresta)
    ],
    "Recall": [
        recall_score(y_test, y_pred_logistico),
        recall_score(y_test, y_pred_knn),
        recall_score(y_test, y_pred_arvore),
        recall_score(y_test, y_pred_floresta)
    ],
    "F1-score": [
        f1_score(y_test, y_pred_logistico),
        f1_score(y_test, y_pred_knn),
        f1_score(y_test, y_pred_arvore),
        f1_score(y_test, y_pred_floresta)
    ]
}

resultados_df = pd.DataFrame(resultados)
print("\nTabela comparativa:")
print(resultados_df)



# 12. Gráfico
resultados_df.set_index("Modelo").plot(kind="bar", figsize=(10, 6))
plt.title("Comparação entre os algoritmos")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
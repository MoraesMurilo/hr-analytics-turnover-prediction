

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMClassifier
from sklearn.metrics import roc_auc_score, classification_report

# Carregamento dos dados
df = pd.read_csv("HRDataset_v14.csv")  

# Definição do alvo do alvo (target)
target = "Termd"  # 1 = desligado / 0 = ativo

#  Remoção de colunas que causam vazamento ou não são úteis para predição
cols_to_drop = [
    target,
    "DateofHire",
    "DateofTermination",
    "LastPerformanceReview_Date",
    "TermReason",
    "EmploymentStatus"
]

cols_to_drop = [c for c in cols_to_drop if c in df.columns]

X = df.drop(columns=cols_to_drop)
y = df[target]

# Remoção de colunas datetime ou com valores não numéricos que atrapalhem
for col in X.columns:
    if pd.api.types.is_datetime64_any_dtype(X[col]):
        X = X.drop(columns=[col])

# Variáveis categóricas (Label Encoding)
for col in X.columns:
    if X[col].dtype == "object":
        X[col] = LabelEncoder().fit_transform(X[col].astype(str))

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

#  Treinamento do modelo LightGBM
model = LGBMClassifier(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
model.fit(X_train, y_train)

# Avaliação
probs = model.predict_proba(X_test)[:, 1]
preds = model.predict(X_test)

print("\n========= RESULTADOS =========")
print("AUC:", roc_auc_score(y_test, probs))
print("\nRelatório de Classificação:\n", classification_report(y_test, preds))

# Geração de Variáveis mais importantes
feature_importance = pd.DataFrame({
    "Variável": X.columns,
    "Importância": model.feature_importances_
}).sort_values(by="Importância", ascending=False)
feature_importance.to_csv("importancia_variaveis.csv", index=False)

# Geração de arquivo com probabilidade de desligamento
df_export = df.copy()
df_export["Prob_Desligamento"] = model.predict_proba(X)[:, 1]

df_export.to_csv("predicoes_desligamento.csv", index=False)

print("\n Arquivo 'predicoes_desligamento.csv' gerado com sucesso!")

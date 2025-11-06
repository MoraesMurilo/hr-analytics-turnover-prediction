# 💼 HR Analytics Turnover Prediction

## 🧭 Resumo Executivo
Este projeto apresenta uma solução completa de **People Analytics** voltada à previsão de desligamentos e à melhoria da **retenção de talentos**.  
Unindo **ETL automatizado (Python + MySQL)**, **modelo de Machine Learning (LightGBM)** e **dashboard interativo em Power BI**, ele permite identificar áreas críticas, mensurar custos e prever riscos individuais de saída de colaboradores.

O resultado é uma ferramenta analítica que traduz dados de RH em **decisões estratégicas de retenção e eficiência organizacional**.

---

## 🧩 Problema de Negócio
O turnover elevado compromete produtividade e eleva custos operacionais.  
A empresa precisava compreender:

- Quais áreas concentram maior rotatividade?  
- Quais fatores impulsionam os desligamentos?  
- É possível prever quais colaboradores estão mais propensos a sair?  

O objetivo do projeto foi desenvolver um **sistema preditivo de desligamentos** integrado ao pipeline de dados corporativo e ao ambiente de BI.

---

## ⚙️ Metodologia

### 🔹 1. ETL (Python + MySQL)
- Limpeza e padronização do dataset `HRDataset_v14.csv`.  
- Criação das dimensões:  
  `dim_colaborador`, `dim_departamento`, `dim_cargo`, `dim_gestor`, `dim_tempo`.  
- Criação do fato principal:  
  `fato_desligamento` com motivo, tipo e custo de rescisão.  
- Carga automatizada para banco **MySQL** via `SQLAlchemy`.  

### 🔹 2. Modelagem Preditiva (LightGBM)
- Modelo supervisionado para prever `Termd` (1 = desligado / 0 = ativo).  
- Avaliação com **AUC = 0.98**, indicando alta precisão.  
- Exportação de:
  - `predicoes_desligamento.csv` — probabilidades individuais.  
  - `importancia_variaveis.csv` — explicabilidade das features.  

### 🔹 3. Visualização e Storytelling (Power BI)
- Dashboard com três camadas analíticas:
  1. **Descritiva:** turnover, motivos e distribuição por área.  
  2. **Diagnóstica:** engajamento, custo e satisfação.  
  3. **Preditiva:** risco médio de desligamento e performance por canal de recrutamento.  

---

## 🧠 Competências e Ferramentas Utilizadas

| Categoria | Ferramentas / Técnicas |
|------------|------------------------|
| **Linguagens** | Python, SQL (MySQL), DAX |
| **Bibliotecas Python** | Pandas, LightGBM, scikit-learn |
| **Data Pipeline** | ETL com SQLAlchemy e Pandas |
| **Visualização** | Power BI |
| **Machine Learning** | Classificação supervisionada, AUC, feature importance |
| **Business Skills** | Data storytelling e análise de turnover |

---

## 📊 Resultados e Recomendações de Negócio

### 🔸 Principais Resultados
- Modelo preditivo com **AUC de 0.98**, alta precisão.  
- Identificação de **canais de recrutamento com maior risco de desligamento** (Google Search e Indeed).  
- Validação de que **o engajamento médio não atua como fator real de retenção**, sugerindo influência de desempenho e satisfação individual.  
- Estimativa de **R$ 6,83 milhões** em custo total de desligamentos no período analisado.  

### 🔸 Recomendações
- Reforçar **programas de indicação interna** e canais com melhor histórico de retenção.  
- Reavaliar **fit de contratação e integração** em áreas com alto turnover (Produção e TI/IS).  
- Implementar **monitoramento preditivo mensal** integrado ao Power BI, com alertas automáticos.

---

## 🚀 Próximos Passos
- Aprofundar o cálculo de **Employee Lifetime Value (ELV)**.  
- Incluir dados de **performance e feedback contínuo** no modelo.  
- Automatizar a atualização de previsões via **API Python ↔ Power BI**.

---

## 🗂️ Estrutura do Repositório
📦 hr-analytics-turnover-prediction
┣ 📂 data
┃ ┣ HRDataset_v14.csv
┃ ┣ predicoes_desligamento.csv
┃ ┗ importancia_variaveis.csv
┣ 📂 etl
┃ ┗ etl.py
┣ 📂 model
┃ ┗ layoff_forecast.py
┣ 📂 dashboard
┃ ┗ view.pbix
┣ 📄 README.md
┗ 📄 requirements.txt

---

## 💬 Principais Insights do Dashboard

### **1️⃣ Indicadores de RH — Panorama Geral**
> Em 2025, a empresa mantém **207 colaboradores ativos** e registrou **104 desligamentos** (turnover de 33%).  
> O **departamento de Produção** concentra a maior parte das saídas, seguido por **TI/IS**.  
> A maioria dos desligamentos é **voluntária**, ligada à busca por novas oportunidades e à falta de progressão interna.

---

### **2️⃣ Diagnóstico — Engajamento e Custos**
> A relação entre **engajamento médio e turnover** não demonstra correlação clara.  
> Isso indica que o engajamento percebido **não está atuando como fator de retenção efetivo**, possivelmente refletindo percepções momentâneas.  
> O **custo total de desligamentos** ultrapassa **R$ 6,83 milhões**, concentrado em áreas com alto volume de funcionários e cargos estratégicos.  
> Sugere-se investigar **outros fatores de desligamento**, como desempenho, absenteísmo e políticas de liderança.

---

### **3️⃣ Preditivo — Risco de Desligamento**
> O modelo **LightGBM** atingiu **AUC = 0.98**, prevendo com alta precisão os colaboradores em risco.  
> Canais como **Google Search** e **Indeed** concentram maior risco predito, enquanto **Employee Referral** e **Diversity Job Fair** apresentam retenção superior.  
> As variáveis mais relevantes incluem **PerformanceScore**, **EngagementSurvey**, **EmpSatisfaction** e **Absences**.  
> O modelo apoia ações preventivas e otimiza investimentos em recrutamento.

---

## 🧩 Conclusão
Este projeto demonstra domínio completo do ciclo de **Data Analytics** — da engenharia de dados à entrega executiva.  
Mais do que prever desligamentos, ele mostra a capacidade de **traduzir dados complexos de RH em decisões práticas e mensuráveis**, unindo **ciência de dados e estratégia de negócios**.

---

## 📫 Contato
**Autor:** [Murilo Anselmo de Moraes](https://www.linkedin.com/in/muriloanselmomoraes)  
**LinkedIn:** [linkedin.com/in/muriloanselmomoraes](https://www.linkedin.com/in/muriloanselmomoraes)  
**E-mail:** moraesmurilo36id@gmail.com 
**Ferramentas:** Python · MySQL · Power BI · Machine Learning · Data Storytelling

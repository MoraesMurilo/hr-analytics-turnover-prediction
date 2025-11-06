import pandas as pd
from sqlalchemy import create_engine

def main():
    print("🔹 Iniciando ETL...")

    # Leiura CSV bruto
    csv_path = "HRDataset_v14.csv"
    print(f"🔹 Lendo CSV: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"🔹 Linhas carregadas do CSV: {len(df)}")

    # Conversão de datas
    df["DateofHire"] = pd.to_datetime(df["DateofHire"], errors="coerce")
    df["DateofTermination"] = pd.to_datetime(df["DateofTermination"], errors="coerce")
    df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce")

    if "Termd" in df.columns:
        df["Termd"] = df["Termd"].fillna(0).astype(int)
    else:
        df["Termd"] = 0

    print("🔹 Montando dimensões...")

    # Departamento
    dim_departamento = (
        df[["Department"]]
        .dropna()
        .drop_duplicates()
        .rename(columns={"Department": "nome_departamento"})
        .reset_index(drop=True)
    )
    dim_departamento.insert(0, "id_departamento", range(1, len(dim_departamento) + 1))
    print(f"   • dim_departamento: {len(dim_departamento)} linhas")

    # Cargo
    dim_cargo = (
        df[["Position"]]
        .dropna()
        .drop_duplicates()
        .rename(columns={"Position": "nome_cargo"})
        .reset_index(drop=True)
    )
    dim_cargo.insert(0, "id_cargo", range(1, len(dim_cargo) + 1))
    print(f"   • dim_cargo: {len(dim_cargo)} linhas")

    # Gestor
    dim_gestor = (
        df[["ManagerName"]]
        .fillna("Sem Gestor")
        .drop_duplicates()
        .rename(columns={"ManagerName": "nome_gestor"})
        .reset_index(drop=True)
    )
    dim_gestor.insert(0, "id_gestor", range(1, len(dim_gestor) + 1))
    print(f"   • dim_gestor: {len(dim_gestor)} linhas")

    # voltar IDs pro df principal
    df = df.merge(dim_departamento, left_on="Department", right_on="nome_departamento", how="left")
    df = df.merge(dim_cargo, left_on="Position", right_on="nome_cargo", how="left")
    df = df.merge(dim_gestor, left_on="ManagerName", right_on="nome_gestor", how="left")

    if "LastPerformanceReview_Date" in df.columns:
        df["LastPerformanceReview_Date"] = pd.to_datetime(df["LastPerformanceReview_Date"], errors="coerce")

    # dim_colaborador
    dim_colaborador = pd.DataFrame({
        "id_colaborador": df["EmpID"],
        "nome": df["Employee_Name"],
        "sexo": df["Sex"],
        "genero_id": df["GenderID"],
        "estado_civil": df["MaritalDesc"],
        "marital_status_id": df["MaritalStatusID"],
        "data_nascimento": df["DOB"],
        "data_admissao": df["DateofHire"],
        "data_desligamento": df["DateofTermination"],
        "status_emprego": df["EmploymentStatus"],
        "citizenship": df["CitizenDesc"],
        "race": df["RaceDesc"],
        "estado": df["State"],
        "cep": df["Zip"],
        "id_departamento": df["id_departamento"],
        "id_cargo": df["id_cargo"],
        "id_gestor": df["id_gestor"],
        "salario": df["Salary"],
        "recrutamento": df["RecruitmentSource"],
        "performance_score": df["PerformanceScore"],
        "perf_score_id": df["PerfScoreID"],
        "engagement_survey": df["EngagementSurvey"],
        "emp_satisfaction": df["EmpSatisfaction"],
        "special_projects": df["SpecialProjectsCount"],
        "last_performance_review_date": df["LastPerformanceReview_Date"],
        "days_late_last_30": df["DaysLateLast30"],
        "absences": df["Absences"]
    })
    print(f"   • dim_colaborador: {len(dim_colaborador)} linhas")

    # fato_desligamento
    fato_desligamento = df[(df["DateofTermination"].notna()) | (df["Termd"] == 1)].copy()
    fato_desligamento = pd.DataFrame({
        "id_colaborador": fato_desligamento["EmpID"],
        "data_desligamento": fato_desligamento["DateofTermination"],
        "motivo": fato_desligamento["TermReason"],
        "tipo": fato_desligamento["EmploymentStatus"],
        "custo_rescisao": fato_desligamento["Salary"]
    })
    print(f"   • fato_desligamento: {len(fato_desligamento)} linhas")

    # dim_tempo
    datas_deslig = fato_desligamento["data_desligamento"].dropna().drop_duplicates().sort_values()
    dim_tempo = pd.DataFrame({"data_completa": datas_deslig})
    dim_tempo["ano"] = dim_tempo["data_completa"].dt.year
    dim_tempo["mes"] = dim_tempo["data_completa"].dt.month
    dim_tempo["nome_mes"] = dim_tempo["data_completa"].dt.strftime("%B")
    dim_tempo.insert(0, "id_tempo", range(1, len(dim_tempo) + 1))
    print(f"   • dim_tempo: {len(dim_tempo)} linhas")

    # --------------- CONEXÃO MYSQL ---------------
    print("🔹 Gravando no MySQL...")
    engine = create_engine("mysql+pymysql://hr_user:senha123@localhost:3306/hr_analytics")


    # gravação
    dim_departamento.to_sql("dim_departamento", engine, if_exists="append", index=False)
    dim_cargo.to_sql("dim_cargo", engine, if_exists="append", index=False)
    dim_gestor.to_sql("dim_gestor", engine, if_exists="append", index=False)
    dim_colaborador.to_sql("dim_colaborador", engine, if_exists="append", index=False)
    dim_tempo.to_sql("dim_tempo", engine, if_exists="append", index=False)
    fato_desligamento.to_sql("fato_desligamento", engine, if_exists="append", index=False)

    print(" Carga concluída no MySQL.")

if __name__ == "__main__":
    main()

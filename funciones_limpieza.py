import pandas as pd
from sklearn.preprocessing import StandardScaler


def limpiar_datos(ruta):
    df = pd.read_csv(ruta)

    # 1 sacar el ID y las columnas que ya dicen si hay cancer
    df = df.drop(columns=['Patient_ID', 'Biopsy_Result', 'Cancer_Stage'])

    # 2 Sacar las 300 filas con datos vacíos
    df = df.dropna()

    # 3 Recortar valores extremos (no se borran, se llevan al límite)
    for col in ['BMI', 'Tumor_Size_cm']:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        df[col] = df[col].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)

    # 4 Pasar texto a numeros
    si_no = ['Family_History', 'Smoking', 'Alcohol_Consumption', 'Hormone_Therapy',
             'Lymph_Node_Involvement', 'Diabetes']
    for col in si_no:
        df[col] = df[col].map({'No': 0, 'Yes': 1})

    df['Genetic_Mutation'] = df['Genetic_Mutation'].map({'Negative': 0, 'Positive': 1})
    df['Menopause_Status'] = df['Menopause_Status'].map({'Pre': 0, 'Post': 1})
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    df['Physical_Activity'] = df['Physical_Activity'].map({'Low': 0, 'Moderate': 1, 'High': 2})

    # estas no tienen orden, así que se crea una columna 0/1 por cada opcion
    df = pd.get_dummies(df, columns=['Mammogram_Result', 'Breastfeeding_History'], dtype=int)

    # 5 Normalizar los numeros para que queden en la misma escala
    numericas = ['Age', 'BMI', 'Tumor_Size_cm', 'Blood_Pressure',
                 'Cholesterol', 'Exercise_Days_Per_Week', 'Annual_Income_USD']
    df[numericas] = StandardScaler().fit_transform(df[numericas])

    return df

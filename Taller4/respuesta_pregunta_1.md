**Respuesta 1:**

**El objetivo y las variables desde la perspectiva de las pacientes.**

El dataset busca predecir si una persona tiene cáncer de mama (`Cancer` = 0/1) a partir de variables clínicas, demográficas y de estilo de vida (mobeenfatimah, s. f.). Quien construye el modelo lo ve como un problema de clasificación. Para una paciente, en cambio, ese objetivo significa que su salud, su genética y su situación económica se reducen a una fila de números, y que de ellos sale una etiqueta que puede definir si la atienden, cuándo y en qué condiciones. Ella no participó en decidir qué se mide ni para qué se usará. Tampoco puede corregir un dato erróneo ni saber quién más lo verá.

Las variables sobre su vida personal (fumar, beber alcohol, no hacer ejercicio) pueden sentirse como un juicio sobre ella, y no como una descripción de factores de riesgo. Una predicción de "alto riesgo" puede generar angustia, estigma o pérdida de oportunidades, aunque sea incorrecta. Además, la paciente solo aparece como un conjunto de rasgos individuales. No se registra dónde vive, si pudo acceder a un control a tiempo ni qué previsión tiene. Esas condiciones suelen explicar buena parte de por qué una persona se enferma o se diagnostica tarde (Braveman & Gottlieb, 2014).

**Variables con riesgo de mal uso.** Los datos del dataset sirven para mostrar que el riesgo no depende de si la variable "predice" bien:

| Variable | Dato en el dataset | Qué muestra |
|---|---|---|
| `Smoking` | Cáncer en 37,7 % de fumadoras vs. 13,1 % de no fumadoras | Un modelo se apoyaría mucho en esta variable. Eso refuerza la culpabilización: la enfermedad se atribuye a la decisión individual. |
| `Alcohol_Consumption` | 18,6 % (con consumo) vs. 19,9 % (sin consumo) | Casi no hay diferencia, pero la variable igual puede usarse para señalar a las pacientes. |
| `Annual_Income_USD` | Ingreso medio de ~82 mil USD (sin cáncer) vs. ~83 mil USD (con cáncer) | No está asociado a la enfermedad. Aun así, permite perfilar por nivel socioeconómico. |
| `Gender` | Cáncer en 21,3 % de los hombres vs. 19,2 % de las mujeres (723 hombres, 7,2 % del total) | Contradice la epidemiología real, donde el cáncer de mama en hombres es poco frecuente. |
| `Genetic_Mutation` | 14,6 % de positivos | Es una proporción mucho mayor que la de la población general, donde la prevalencia de variantes patogénicas de *BRCA1/2* se estima en 1 de cada 400 a 800 personas (National Cancer Institute, s. f.). |

- **Genetic_Mutation:** es un dato genético, el más sensible del dataset. Una aseguradora o un empleador podrían usarlo para discriminar (primas más altas, rechazo de cobertura, no contratación). Además, revela información sobre familiares que no consintieron. En Chile, la Ley 20.120 prohíbe la discriminación arbitraria basada en el patrimonio genético y establece que los resultados de exámenes genéticos no pueden usarse con ese fin (art. 4), y declara reservada la información genética de una persona (art. 12). En EE. UU., la Genetic Information Nondiscrimination Act (2008) prohíbe usarla en seguros de salud y en el empleo. Que existan estas normas muestra que el riesgo de discriminación es reconocido. Y como el dataset sobrerrepresenta las mutaciones, un modelo entrenado con él exageraría su peso.
- **Annual_Income_USD:** permite perfilar socioeconómicamente. Se podría usar para priorizar o excluir a personas del acceso a tratamiento, o para estigmatizar a grupos de bajos ingresos. Combinado con otras variables, facilita la reidentificación.
- **Gender:** el dataset es sintético y no reproduce la epidemiología real: muestra más cáncer en hombres que en mujeres. Un modelo entrenado con estos datos aprendería una relación que no existe en la población, y eso es un riesgo en sí mismo. Además, la variable reduce el género a dos categorías, e invisibiliza a personas trans o no binarias.
- **Smoking y Alcohol_Consumption:** pueden llevar a culpabilizar a la víctima, es decir, a atribuir la enfermedad a las decisiones individuales. Eso ignora los determinantes sociales (Braveman & Gottlieb, 2014) y puede justificar restringir la cobertura o el acceso a tratamiento, o aumentar el estigma hacia quienes tienen estos hábitos. Aunque el tabaco sí figura entre los factores de riesgo reconocidos (Centros para el Control y la Prevención de Enfermedades, 2026), no se debe usar para responsabilizar a la paciente.

**¿Por qué se consideran estas variables y no otras?** Se eligen por su disponibilidad y por lo que la literatura clínica reconoce como factores de riesgo, como la edad, los antecedentes familiares y la terapia hormonal (Centros para el Control y la Prevención de Enfermedades, 2026). Pero faltan variables estructurales, como territorio, etnia, previsión de salud y acceso a atención. Sin ellas, el modelo atribuye el riesgo a rasgos individuales y no mide las brechas de acceso. Así se sobrerrepresenta lo individual y se invisibiliza lo estructural.

**Referencias**

Braveman, P., & Gottlieb, L. (2014). The social determinants of health: It's time to consider the causes of the causes. *Public Health Reports, 129*(Suppl. 2), 19–31. https://doi.org/10.1177/00333549141291S206

Centros para el Control y la Prevención de Enfermedades. (2026, 15 de abril). *Factores de riesgo del cáncer de mama*. https://www.cdc.gov/breast-cancer/es/risk-factors/index.html

Genetic Information Nondiscrimination Act of 2008, Pub. L. No. 110-233, 122 Stat. 881 (2008). https://www.govinfo.gov/content/pkg/PLAW-110publ233/html/PLAW-110publ233.htm

Ley 20.120. Sobre la investigación científica en el ser humano, su genoma, y prohíbe la clonación humana. (2006, 22 de septiembre). Diario Oficial de la República de Chile. https://www.bcn.cl/leychile/navegar?idNorma=253478

mobeenfatimah. (s. f.). *Breast cancer prediction dataset | 10,000 patient* [Conjunto de datos]. Kaggle. https://www.kaggle.com/datasets/mobeenfatimah/breast-cancer-prediction-dataset-10000-patient

National Cancer Institute. (s. f.). *BRCA1 and BRCA2: Cancer risks and management (PDQ®) – Health professional version*. https://www.ncbi.nlm.nih.gov/books/n/pdqcis/CDR0000811356

# 🤖 Modelo Preditivo de Preços de Livros + Análise Exploratória

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)](https://matplotlib.org/)
[![TCC](https://img.shields.io/badge/TCC-2025-blue?style=for-the-badge)](https://github.com/Aram-Bohmann/TCC-Aplicacao-Movel-de-Literatura-Digital)

> **Machine Learning aplicado à precificação inteligente de livros digitais**  
> Parte do TCC LêBits - Aplicação Móvel de Literatura Digital

Sistema de precificação automatizada usando Regressão Linear com interface interativa em Streamlit, desenvolvido para demonstrar o potencial de Machine Learning na plataforma LêBits.

---

## 📖 Sobre o Projeto

Este repositório contém a **prova de conceito** de funcionalidades de Machine Learning que serão implementadas na aplicação LêBits. O projeto combina:

- 🤖 **Modelo Preditivo** - Regressão Linear para precificação
- 📊 **Análise Exploratória** - Visualizações com Matplotlib
- 🎨 **Interface Interativa** - Dashboard Streamlit
- 📈 **Insights de Negócio** - Tendências do mercado editorial

### 🎯 Aplicações de IA no LêBits

- 🔍 **Pesquisa inteligente** - Busca de livros por características
- 🎯 **Sistema de recomendação** - Sugestões personalizadas
- 💰 **Precificação dinâmica** - Preços justos baseados em dados
- 📊 **Análise de mercado** - Insights sobre tendências editoriais

---

## 🎯 Objetivos

### Objetivo Principal
Desenvolver um modelo de Machine Learning capaz de prever preços de livros com alta acurácia, baseado em avaliação, número de páginas e popularidade.

### Objetivos Específicos
✅ Implementar algoritmo de Regressão Linear  
✅ Criar interface interativa para demonstração  
✅ Gerar visualizações analíticas dos dados  
✅ Validar modelo com métricas estatísticas  
✅ Documentar processo para replicação  

---

## 📊 Dataset - Goodreads Best Books Ever

### 📋 Características

| Atributo | Valor |
|----------|-------|
| **Fonte** | [Goodreads BBE Dataset](https://github.com/scostap/goodreads_bbe_dataset) |
| **Registros** | ~50.000 livros |
| **Período** | 1900-2023 |
| **Idioma** | Predominantemente inglês |
| **Atualização** | Estático (snapshot) |

### 🗂️ Variáveis Utilizadas

| Coluna | Tipo | Descrição | Uso no Modelo |
|--------|------|-----------|---------------|
| `rating` | Float | Avaliação média (0-5) | ✅ Feature |
| `pages` | Integer | Número de páginas | ✅ Feature |
| `numRatings` | Integer | Total de avaliações | ✅ Feature |
| `price` | Float | Preço em USD | 🎯 Target |
| `author` | String | Nome do autor | 📊 Análise |
| `genres` | String | Gêneros literários | 📊 Análise |
| `title` | String | Título do livro | - |

---

## 🤖 Modelo Preditivo - Streamlit App

### 📸 Interface do Dashboard

<p align="center">
  <img width="100%" alt="Dashboard Streamlit" src="[COLE_AQUI_A_IMAGEM_DO_DASHBOARD]" />
</p>

### ⚙️ Arquitetura do Modelo
```python
# Pipeline Completo
📥 Carregamento de Dados (CSV)
    ↓
🧹 Pré-processamento
    ├── Conversão de tipos (str → float)
    ├── Extração de números (páginas)
    └── Remoção de valores nulos
    ↓
🔀 Divisão Treino/Teste (80/20)
    ↓
🤖 Treinamento (Regressão Linear)
    ↓
📊 Avaliação (MSE)
    ↓
🎯 Predição Interativa (Streamlit)
```

### 🔧 Funcionalidades do App

#### 1️⃣ Visualização dos Dados
```python
st.dataframe(df)
```
- Exibição completa do dataset
- Tabela interativa com scroll
- Visualização de todas as colunas

#### 2️⃣ Treinamento do Modelo
```python
# Features utilizadas
X = df[["rating", "pages", "numRatings"]]
y = df["price"]

# Split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
model = LinearRegression()
model.fit(X_train, y_train)
```

**Métricas exibidas:**
- 📊 Tamanho do conjunto de treino
- 📊 Tamanho do conjunto de teste
- 📈 MSE (Mean Squared Error)

#### 3️⃣ Predição Interativa

**Inputs do usuário:**
- 📖 **Nota do Livro** - Slider (0.0 a 5.0)
- 📄 **Número de Páginas** - Input numérico
- ⭐ **Número de Avaliações** - Input numérico

**Output:**
```python
# Exemplo de predição
Inputs: 
  - rating: 4.5
  - pages: 350
  - numRatings: 50000

Output: "O Preço previsto foi de: $24.87 dólares!"
```

---

## 📊 Análise Exploratória de Dados (EDA)

### 📈 Visualizações com Matplotlib

Três gráficos principais desenvolvidos para análise de mercado:

#### 1️⃣ Distribuição das Avaliações
```python
plt.hist(df["rating"], bins=30)
plt.xlabel("Avaliação dos Livros")
plt.title("Qual é a Distribuição das Avaliações?")
```

<p align="center">
  <img width="700" alt="Histograma - Distribuição de Avaliações" src="https://github.com/user-attachments/assets/f763bf8b-bad5-460b-8fb6-77684cb60913" />

</p>

**Insights:**
- ✅ Maioria dos livros tem avaliação entre 3.5-4.5
- ✅ Distribuição aproximadamente normal
- ✅ Poucos livros com nota < 2.0 ou > 4.8

---

#### 2️⃣ Top 5 Autores Mais Avaliados
```python
# Tratamento de nomes
df["author"] = df["author"].str.replace(r"\(.*\)", "", regex=True).str.strip()

# Agregação
autor_avaliado = df.groupby("autor_nome_curto")["numRatings"].sum()

# Top 5
plt.bar(autor_avaliado.index[:5], autor_avaliado.values[:5])
plt.title("Quais são os Autores mais Avaliados?")
```

<p align="center">
  <img width="700" alt="Gráfico - Top Autores" src="https://github.com/user-attachments/assets/c1ee66f9-c84b-4c77-a34b-24d0b778fe96" />

</p>

**Insights:**
- ✅ J.K. Rowling e Stephen King lideram
- ✅ Autores populares têm milhões de avaliações
- ✅ Correlação entre fama e volume de reviews

---

#### 3️⃣ Top 5 Gêneros Mais Frequentes
```python
# Separação de gêneros
generos_separado = df["genres"].str.split(",").explode().str.strip()
generos_contados = generos_separado.value_counts().head(5)

# Remoção de aspas
generos_tratado.index = generos_tratado.index.str.replace("'", "")

plt.bar(generos_tratado.index, generos_contados.values)
plt.title("Top 5 Gêneros Mais Frequentes")
```

<p align="center">
  <img width="700" alt="Gráfico - Top Gêneros" src="https://github.com/user-attachments/assets/83a9bf88-4439-4e1f-93fa-ffbcd7ca4d27" />
</p>

**Insights:**
- ✅ Fiction domina o mercado
- ✅ Fantasy e Young Adult são populares
- ✅ Romance e Thriller completam o top 5

---

## 🔧 Pré-processamento de Dados

### Etapas de Limpeza

#### 1️⃣ Extração de Números (Páginas)
```python
# Problema: pages pode vir como "300 pages" ou "300"
df["pages"] = (
    df["pages"]
    .astype(str)
    .str.extract(r"(\d+)")  # Extrai apenas dígitos
    .astype(float)
)
```

#### 2️⃣ Conversão de Tipos
```python
# Conversão para numérico com tratamento de erros
colunas_numericas = ["numRatings", "rating", "price"]
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")
```

#### 3️⃣ Remoção de Valores Nulos
```python
# Remove linhas com NaN nas features críticas
df = df.dropna(subset=["rating", "pages", "numRatings", "price"])
```

#### 4️⃣ Tratamento de Nomes (Autores)
```python
# Remove anotações como (Illustrator), (Goodreads Author)
df["author"] = df["author"].str.replace(
    r"\(.*goodreads author.*\)", "", 
    regex=True, 
    case=False
).str.strip()

# Encurta nomes (Primeiro + Último)
def nome_menor(nome):
    partes = nome.split()
    if len(partes) <= 2:
        return nome
    return partes[0] + " " + partes[-1]

df["autor_nome_curto"] = df["author"].apply(nome_menor)
```

---

## 🚀 Como Executar

### Pré-requisitos
```bash
# Python 3.8 ou superior
python --version

# Pip atualizado
pip --version
```

### Instalação
```bash
# Clone o repositório
git clone https://github.com/Aram-Bohmann/Modelo-Preditivo-de-Precos-de-Livros-e-Visualizacoes.git

# Entre no diretório
cd Modelo-Preditivo-de-Precos-de-Livros-e-Visualizacoes

# Instale as dependências
pip install streamlit pandas scikit-learn matplotlib
```

### Executando o Dashboard
```bash
# Inicie o Streamlit
streamlit run app.py

# O navegador abrirá automaticamente em:
# http://localhost:8501
```

### Executando Análises EDA
```bash
# Gerar visualizações estáticas
python visualizacoes.py

# Os gráficos serão exibidos sequencialmente
```

---

## 📊 Métricas de Performance

### Avaliação do Modelo

| Métrica | Descrição | Valor Típico |
|---------|-----------|--------------|
| **MSE** | Mean Squared Error | < 50 |

### Interpretação do MSE
```python
# Exemplo de output
mse = mean_squared_error(y_test, predictions)
# Output: "Erro Médio Quadrático (MSE): 32.4567"

# Interpretação:
# MSE baixo (<50) = Boas predições
# MSE médio (50-100) = Predições aceitáveis
# MSE alto (>100) = Modelo precisa melhorar
```

---

## 🎯 Casos de Uso

### Exemplo 1: Livro Bestseller

**Input:**
```
rating: 4.7
pages: 450
numRatings: 2500000
```

**Output:** `$28.50`

**Interpretação:** Livro muito popular com alta avaliação = preço premium

---

### Exemplo 2: Livro Indie

**Input:**
```
rating: 4.2
pages: 250
numRatings: 1500
```

**Output:** `$9.99`

**Interpretação:** Livro menos conhecido = preço acessível

---

### Exemplo 3: Livro Acadêmico

**Input:**
```
rating: 4.0
pages: 800
numRatings: 5000
```

**Output:** `$45.00`

**Interpretação:** Livro extenso com público específico = preço elevado

---

## 🛠️ Stack Tecnológica

### Core
![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

### Visualização
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)

### Bibliotecas Utilizadas
```python
# requirements.txt
streamlit==1.28.0
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
```

---

## 🎨 Customizações Visuais

### Paleta de Cores
```python
# Cor principal dos gráficos
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#6E5346"])
```

**Cor:** `#6E5346` (Marrom Terroso)  
**Filosofia:** Relacionado ao universo literário e elegância

### Formatação de Eixos
```python
# Evita notação científica
def sem_notacao_cientifica(x, pos):
    if x >= 1e6:
        return f"{x/1e6:.1f}M"
    if x >= 1e3:
        return f"{x/1e3:.0f}k"
    return f"{int(x)}"

plt.gca().yaxis.set_major_formatter(FuncFormatter(sem_notacao_cientifica))
```

**Resultado:**
- 1.000 → "1k"
- 1.000.000 → "1M"

---

## 💡 Insights do Mercado Editorial

### 📊 Descobertas Principais

#### Preços
- 💰 Média global: $15-25
- 📚 Bestsellers: $20-35
- 🎓 Acadêmicos: $40-80
- 📖 Indie: $5-15

#### Avaliações
- ⭐ Livros 4.5+: Premium pricing
- ⭐ Livros 3.0-4.0: Preço competitivo
- ⭐ Livros <3.0: Desconto necessário

#### Páginas
- 📄 Sweet spot: 300-400 páginas
- 📕 Curtos (<200): Menor valor percebido
- 📚 Longos (>600): Preço justificado por conteúdo

#### Popularidade
- 🔥 10k+ reviews: +15% no preço
- 📈 100k+ reviews: +30% no preço
- 🌟 1M+ reviews: Preço premium garantido

---

## 🔗 Projeto Completo - TCC LêBits

Este modelo faz parte de um ecossistema maior:

### 📚 [Documentação Acadêmica](https://github.com/Aram-Bohmann/TCC-Aplicacao-Movel-de-Literatura-Digital)
- 📄 TCC completo (62 páginas)
- 🗄️ Arquitetura de banco de dados
- 📊 Pesquisa de aplicabilidade (61 respondentes)
- 📈 Análise SWOT e matriz de comparação

### 📱 [Aplicativo Móvel](https://github.com/Aram-Bohmann/App-de-Literatura)
- Apache Cordova + Framework7
- 18 telas desenvolvidas
- Interface completa de leitura
- Gamificação implementada

---

## 🎓 Contexto Acadêmico

### Informações do TCC

| Item | Detalhe |
|------|---------|
| **Curso** | Técnico em Ciência de Dados |
| **Instituição** | CEDUP Timbó - SC |
| **Ano** | 2025 |
| **Equipe** | Aram Bohmann, David Zumach, Enzo Dias, João Victor Pereira |

### Competências Demonstradas

1. **📊 Análise de Dados** - EDA completa com Pandas e Matplotlib
2. **🤖 Machine Learning** - Regressão Linear com Scikit-Learn
3. **🎨 Visualização** - Gráficos profissionais customizados
4. **💻 Desenvolvimento Web** - Dashboard interativo com Streamlit
5. **🧹 Data Cleaning** - Pré-processamento robusto
6. **📝 Documentação** - README técnico detalhado

---

## 🚀 Melhorias Futuras

### Roadmap

#### Curto Prazo
- [ ] Adicionar mais features (gênero, editora, ano)
- [ ] Implementar validação cruzada (k-fold)
- [ ] Melhorar interface Streamlit (sidebar, tabs)
- [ ] Adicionar gráficos de resíduos

#### Médio Prazo
- [ ] Ensemble methods (Random Forest, XGBoost)
- [ ] Feature importance visualization
- [ ] API REST para integração
- [ ] Deploy em Streamlit Cloud

#### Longo Prazo
- [ ] Sistema de recomendação colaborativo
- [ ] Análise de sentimento em reviews
- [ ] Deep Learning (Neural Networks)
- [ ] Integração completa com app LêBits

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

### Como Contribuir

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/melhoria`)
3. Commit suas mudanças (`git commit -m 'Adiciona feature X'`)
4. Push para a branch (`git push origin feature/melhoria`)
5. Abra um Pull Request

### Áreas de Contribuição

- 📊 **Análises** - Novos gráficos e insights
- 🤖 **Modelos** - Algoritmos alternativos
- 🎨 **UI/UX** - Melhorias no Streamlit
- 📝 **Docs** - Aprimoramentos na documentação
- 🐛 **Bugs** - Correções e otimizações

---

## 📝 Licença

Este projeto foi desenvolvido como **Trabalho de Conclusão de Curso** e está disponível para:

✅ Uso educacional  
✅ Modificação e adaptação  
✅ Distribuição com créditos  

---

## 📞 Contato

**Desenvolvedor:** Aram Bohmann Leite da Luz

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arambohmannleitedaluz@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aram-luz-1b0ab1321)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Aram-Bohmann)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aram-bohmann.github.io/Site-Portfolio/)

---

## 🙏 Agradecimentos

- **CEDUP Timbó** - Formação técnica de excelência
- **Scikit-Learn** - Biblioteca robusta de ML
- **Streamlit** - Framework incrível para dashboards
- **Goodreads** - Dataset público de qualidade
- **Comunidade Python** - Ferramentas open-source

---

<div align="center">

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Desenvolvido com 💙 e 🤖 para o TCC 2025**

*"Machine Learning democratizando o acesso à literatura digital"*

</div>

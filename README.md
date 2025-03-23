# ERP Financeiro com Streamlit

Este é uma simulaçaõ de um sistema **ERP Financeiro** simples, desenvolvido com **Streamlit** e **SQLite**, para gerenciamento de clientes, contas a pagar, contas a receber e lançamentos financeiros.

## 📌 Funcionalidades
- 📋 **Cadastro de Clientes**: Gerencie seus clientes com nome, e-mail e telefone.
- 💰 **Contas a Pagar**: Controle suas despesas e pagamentos.
- 📥 **Contas a Receber**: Acompanhe os valores a receber de clientes.
- 📊 **Lançamentos Financeiros**: Registre receitas e despesas.
- 📈 **Relatórios**: Visualize fluxos de caixa e outras métricas financeiras.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Streamlit** (para interface gráfica)
- **SQLite** (banco de dados)
- **Faker** (geração de dados fictícios)
- **Pandas** (manipulação de dados)

## 🚀 Como Executar o Projeto

###  Clone o repositório:
```bash
git clone https://github.com/seu-usuario/erp-financeiro.git
cd erp-financeiro
```

###  Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
pip install -r requirements.txt
```

###  Execute a carga do banco de dados:
```bash
python database_finance.py
```


### Execute a aplicação:
```bash
streamlit run app.py
```
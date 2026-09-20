# 💰 Smart Expense Tracker

> **Track the chaos. Control the cash.** 💸

A serverless personal expense tracking web application built with **HTML, CSS, JavaScript, Python and AWS**. Track expenses, manage budgets, view transactions, and analyze spending.

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?style=for-the-badge&logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-blue?style=for-the-badge&logo=amazondynamodb)
![Lambda](https://img.shields.io/badge/AWS%20Lambda-Python-yellow?style=for-the-badge&logo=awslambda)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-black?style=for-the-badge&logo=githubactions)

---

## ✨ Features

- 💳 Add, view and delete expenses
- 📊 Spending analytics and category breakdown
- 📅 Today, This Week, This Month, Last Month & All Time filters
- 💰 Monthly budget tracking
- 🧠 Spending insights and saving suggestions
- 📱 Responsive Gen-Z style dashboard

---

## 🏗️ Architecture

```text
                         👤 USER
                            │
                            ▼
                    ┌──────────────┐
                    │   Amazon S3  │
                    │   Frontend   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ API Gateway  │
                    │   HTTP API   │
                    └──────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        Add Lambda     Get Lambda    Delete Lambda
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    ┌──────────────┐
                    │  DynamoDB    │
                    │SmartExpense- │
                    │   Tracker    │
                    └──────────────┘
                           ▲
CI/CD Highlights
Automated deployment on push to main
GitHub Actions workflow
AWS OIDC authentication
IAM role-based access
No long-lived AWS credentials stored in GitHub
Automatic deployment of all 4 Lambda functions
🗄️ DynamoDB

Table: SmartExpenseTracker

Attribute	Type	Description
expense_id	String	Primary key
amount	Number	Expense amount
category	String	Expense category
description	String	Expense description
date	String	Expense date
created_at	String	Creation timestamp
🔄 Application Flow
User enters expense
       ↓
JavaScript sends API request
       ↓
API Gateway
       ↓
Lambda
       ↓
DynamoDB
       ↓
API Response
       ↓
Dashboard updates
🛠️ Tech Stack

Frontend: HTML5, CSS3, JavaScript, LocalStorage
Backend: Python, Boto3, AWS Lambda
Cloud: Amazon S3, API Gateway, DynamoDB, IAM
DevOps: GitHub Actions, AWS OIDC

📂 Project Structure
SmartExpenseTracker/
│
├── .github/
│   └── workflows/
│       └── deploy-lambda.yml
│
├── lambdas/
│   ├── add/
│   │   └── lambda_function.py
│   ├── get/
│   │   └── lambda_function.py
│   ├── delete/
│   │   └── lambda_function.py
│   └── stats/
│       └── lambda_function.py
│
├── index.html
└── README.md
🌐 Live Demo

Live Website:
http://smart-expense-tracker-anuja-2026.s3-website.ap-south-1.amazonaws.com/

👩‍💻 Developer
Anuja Gaikwad

Python Developer | AI • Data Analytics • Automation | AWS

Track the chaos. Control the cash. 💜📊
                           │
                     Stats Lambda

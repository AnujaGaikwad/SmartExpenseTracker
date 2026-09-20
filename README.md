# 💰 Smart Expense Tracker

> **Track the chaos. Control the cash.** 💸

A serverless personal expense tracking web application built with **HTML, CSS, JavaScript, Python and AWS**. Track expenses, manage budgets, view transactions, and analyze spending.

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
                │ SmartExpense │
                │   Tracker    │
                └──────────────┘
                       ▲
                       │
                 Stats Lambda
````

---

## ☁️ AWS Services

| Service               | Purpose                             |
| --------------------- | ----------------------------------- |
| 🪣 **Amazon S3**      | Static website hosting              |
| 🚪 **API Gateway**    | HTTP API                            |
| ⚡ **AWS Lambda**      | Python backend                      |
| 🗄️ **DynamoDB**      | Expense data storage                |
| 🔐 **IAM**            | Access control                      |
| 🔄 **GitHub Actions** | CI/CD automation                    |
| 🔑 **AWS OIDC**       | Secure GitHub-to-AWS authentication |

---

## 🔌 API Endpoints

| Method   | Endpoint                 | Lambda               | Purpose              |
| -------- | ------------------------ | -------------------- | -------------------- |
| `POST`   | `/expenses`              | `SmartExpenseAdd`    | Add expense          |
| `GET`    | `/expenses`              | `SmartExpenseGet`    | Get expenses         |
| `DELETE` | `/expenses/{expense_id}` | `SmartExpenseDelete` | Delete expense       |
| `GET`    | `/stats`                 | `SmartExpenseStats`  | Calculate statistics |

---

## ⚡ Lambda Functions

### `SmartExpenseAdd`

Receives expense data and stores it in DynamoDB.

```text
POST /expenses
      ↓
SmartExpenseAdd
      ↓
DynamoDB.put_item()
```

### `SmartExpenseGet`

Retrieves stored expenses.

```text
GET /expenses
      ↓
SmartExpenseGet
      ↓
DynamoDB.scan()
```

### `SmartExpenseDelete`

Deletes an expense using its unique ID.

```text
DELETE /expenses/{expense_id}
      ↓
SmartExpenseDelete
      ↓
DynamoDB.delete_item()
```

### `SmartExpenseStats`

Calculates spending statistics.

```text
GET /stats
     ↓
SmartExpenseStats
     ↓
DynamoDB
     ↓
Statistics
```

---

## 🔄 CI/CD with GitHub Actions

Lambda code is maintained in GitHub and automatically deployed to AWS whenever changes are pushed to the `main` branch.

```text
Change Lambda Code
        ↓
    Push to main
        ↓
   GitHub Actions
        ↓
     AWS OIDC
        ↓
      IAM Role
        ↓
   Package Lambda
        ↓
   Deploy to AWS
        ↓
    AWS Lambda
```

### CI/CD Highlights

* Automated deployment on push to `main`
* GitHub Actions workflow
* AWS OIDC authentication
* IAM role-based access
* No long-lived AWS credentials stored in GitHub
* Automatic deployment of all 4 Lambda functions

---

## 🗄️ DynamoDB

**Table:** `SmartExpenseTracker`

| Attribute     | Type   | Description         |
| ------------- | ------ | ------------------- |
| `expense_id`  | String | Primary key         |
| `amount`      | Number | Expense amount      |
| `category`    | String | Expense category    |
| `description` | String | Expense description |
| `date`        | String | Expense date        |
| `created_at`  | String | Creation timestamp  |

---

## 🔄 Application Flow

```text
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
```

---

## 🛠️ Tech Stack

**Frontend:** HTML5, CSS3, JavaScript, LocalStorage

**Backend:** Python, Boto3, AWS Lambda

**Cloud:** Amazon S3, API Gateway, DynamoDB, IAM

**DevOps:** GitHub Actions, AWS OIDC

---

## 📂 Project Structure

```text
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
```

---

## 🌐 Live Demo

**Live Website:**
[http://smart-expense-tracker-anuja-2026.s3-website.ap-south-1.amazonaws.com/](http://smart-expense-tracker-anuja-2026.s3-website.ap-south-1.amazonaws.com/)

---

## 👩‍💻 Developer

### Anuja Gaikwad

**Python Developer | AI • Data Analytics • Automation | AWS**

> **Track the chaos. Control the cash.** 

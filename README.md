# 🔑 Password Complexity Checker — PRODIGY_CS_03

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Internship](https://img.shields.io/badge/Prodigy-InfoTech-purple?style=for-the-badge)

> **Task 03** — Prodigy InfoTech Cyber Security Internship

---

## 📌 Task Description

Build a tool that **assesses the strength of a password** based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

---

## ✨ Features

- ✅ Checks **5 security criteria**
- ✅ Gives **score out of 8**
- ✅ Visual **strength bar** display
- ✅ Detailed **what's good / what to improve** feedback
- ✅ Detects **common weak passwords**
- ✅ Strength levels: Weak → Fair → Good → Strong → Very Strong
- ✅ No external libraries needed!

---

## 🔍 Scoring Criteria

| Criteria | Points |
|----------|--------|
| Length 8+ characters | +2 |
| Length 12+ characters | +3 |
| Uppercase letters (A–Z) | +1 |
| Lowercase letters (a–z) | +1 |
| Numbers (0–9) | +1 |
| Special characters (!@#$%) | +2 |
| Common password detected | -3 |

### Strength Levels

| Score | Strength |
|-------|----------|
| 0 – 2 | 🔴 Weak |
| 3 – 4 | 🟠 Fair |
| 5 – 6 | 🟡 Good |
| 7 | 🟢 Strong |
| 8 | 💪 Very Strong |

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed!

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/Prasadsarkate/PRODIGY_CS_03.git

# Navigate to folder
cd PRODIGY_CS_03

# Run the program
python password_checker.py
```

---

## 💻 Usage Example

```
=============================================
   🔑 Password Complexity Checker
=============================================

Enter password to check: MyP@ss#2024!

─────────────────────────────────────────────
  Overall  : 💪 Very Strong
  Strength : [████████████████████] 100%
  Score    : 8 / 8
─────────────────────────────────────────────

  What's good:
    ✅ Excellent length (12+ characters)
    ✅ Contains uppercase letters (A–Z)
    ✅ Contains lowercase letters (a–z)
    ✅ Contains numbers (0–9)
    ✅ Contains special characters (!@#$ etc.)
─────────────────────────────────────────────
```

```
Enter password to check: password123

─────────────────────────────────────────────
  Overall  : 🔴 Weak
  Strength : [████░░░░░░░░░░░░░░░░] 25%
  Score    : 2 / 8
─────────────────────────────────────────────

  What to improve:
    ❌ Add at least one UPPERCASE letter (A–Z).
    ❌ Add at least one special character (!@#$%).
    ⚠  This is a very common password — avoid it!

  💡 Tip: A strong password looks like → MyP@ss#2024!
```

---

## 📂 Project Structure

```
PRODIGY_CS_03/
│
├── password_checker.py   # Main program
└── README.md             # Project documentation
```

---

## 📚 What I Learned

- Importance of **password security** in cybersecurity
- Using **regex** for pattern matching in Python
- How to build a **scoring system** for evaluations
- Understanding **common password vulnerabilities**
- Building user-friendly **CLI feedback tools**

---

## 👨‍💻 Author

**Sudeep** — Cyber Security Intern @ Prodigy InfoTech

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/sudeepm17)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/sudeepgowda172003)

---

## 🏢 Internship

This project was completed as part of the **Prodigy InfoTech Cyber Security Internship**.

`#ProdigyInfoTech` `#Internship` `#CyberSecurity` `#Python` `#PasswordSecurity`

"""
Task-03: Password Complexity Checker
Prodigy Infotech Internship

Checks password strength based on:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
Provides detailed feedback to the user.
"""

import re


# ──────────────────────────────────────────────
# Password analysis
# ──────────────────────────────────────────────

def check_password_strength(password: str) -> dict:
    """
    Analyse password and return score, strength label, and feedback.
    """
    score = 0
    feedback = []
    passed = []

    # 1. Length checks
    length = len(password)
    if length == 0:
        return {
            "score": 0,
            "strength": "No Password",
            "feedback": ["❌ Please enter a password."],
            "passed": [],
            "details": {}
        }
    elif length < 6:
        feedback.append("❌ Too short — use at least 8 characters.")
    elif length < 8:
        score += 1
        feedback.append("⚠  Acceptable length, but 12+ characters is recommended.")
    elif length < 12:
        score += 2
        passed.append("✅ Good length (8+ characters)")
    else:
        score += 3
        passed.append("✅ Excellent length (12+ characters)")

    # 2. Uppercase
    has_upper = bool(re.search(r'[A-Z]', password))
    if has_upper:
        score += 1
        passed.append("✅ Contains uppercase letters (A–Z)")
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (A–Z).")

    # 3. Lowercase
    has_lower = bool(re.search(r'[a-z]', password))
    if has_lower:
        score += 1
        passed.append("✅ Contains lowercase letters (a–z)")
    else:
        feedback.append("❌ Add at least one lowercase letter (a–z).")

    # 4. Numbers
    has_digit = bool(re.search(r'\d', password))
    if has_digit:
        score += 1
        passed.append("✅ Contains numbers (0–9)")
    else:
        feedback.append("❌ Add at least one number (0–9).")

    # 5. Special characters
    has_special = bool(re.search(r'[!@#$%^&*(),.?\":{}|<>_\-\[\]\/\\+=~`\';\&]', password))
    if has_special:
        score += 2
        passed.append("✅ Contains special characters (!@#$ etc.)")
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&* etc.).")

    # 6. Common password check
    common_passwords = [
        "password", "123456", "password123", "admin", "letmein",
        "welcome", "monkey", "qwerty", "abc123", "111111", "iloveyou"
    ]
    if password.lower() in common_passwords:
        score = max(0, score - 3)
        feedback.append("⚠  This is a very common password — avoid it!")

    # Determine strength label
    if score <= 2:
        strength = "🔴 Weak"
    elif score <= 4:
        strength = "🟠 Fair"
    elif score <= 6:
        strength = "🟡 Good"
    elif score <= 7:
        strength = "🟢 Strong"
    else:
        strength = "💪 Very Strong"

    details = {
        "length": length,
        "has_uppercase": has_upper,
        "has_lowercase": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "score": score,
        "max_score": 8
    }

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "passed": passed,
        "details": details
    }


def display_strength_bar(score: int, max_score: int = 8):
    """Display a visual strength bar."""
    filled = round((score / max_score) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    percent = round((score / max_score) * 100)
    print(f"  Strength : [{bar}] {percent}%")


def display_result(result: dict):
    print("\n" + "─" * 45)
    print(f"  Overall  : {result['strength']}")
    display_strength_bar(result['score'])
    print(f"  Score    : {result['score']} / 8")
    print("─" * 45)

    if result['passed']:
        print("\n  What's good:")
        for p in result['passed']:
            print(f"    {p}")

    if result['feedback']:
        print("\n  What to improve:")
        for f in result['feedback']:
            print(f"    {f}")

    print("─" * 45)


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def main():
    print("=" * 45)
    print("   🔑 Password Complexity Checker")
    print("=" * 45)

    while True:
        print("\nOptions:")
        print("  1. Check a password")
        print("  2. Exit")

        choice = input("\nEnter choice (1/2): ").strip()

        if choice == '2':
            print("\nStay secure! 👋")
            break
        elif choice != '1':
            print("  ⚠  Invalid choice.")
            continue

        password = input("\nEnter password to check: ")
        result = check_password_strength(password)
        display_result(result)

        # Tips for very weak passwords
        if result['score'] <= 2:
            print("\n  💡 Tip: A strong password looks like → MyP@ss#2024!")


if __name__ == "__main__":
    main()

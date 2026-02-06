# Spam Email Detection - User Input Version (Programiz Compatible)

# Training data
emails = [
    "Win a free iPhone now",
    "Congratulations you won a prize",
    "Meeting scheduled at 10 AM",
    "Please find the attached report",
    "Free money offer just for you",
    "Let's have lunch tomorrow",
    "Claim your free reward now",
    "Project deadline is next week"
]

# Labels: 1 = Spam, 0 = Not Spam
labels = [1, 1, 0, 0, 1, 0, 1, 0]

# Build word frequency dictionaries
spam_words = {}
ham_words = {}

for email, label in zip(emails, labels):
    words = email.lower().split()
    for word in words:
        if label == 1:
            spam_words[word] = spam_words.get(word, 0) + 1
        else:
            ham_words[word] = ham_words.get(word, 0) + 1

# Prediction function
def predict_email(email):
    words = email.lower().split()
    spam_score = 0
    ham_score = 0

    for word in words:
        spam_score += spam_words.get(word, 0)
        ham_score += ham_words.get(word, 0)

    if spam_score > ham_score:
        return "Spam Email"
    else:
        return "Not Spam Email"

# ------------------ USER INPUT ------------------

user_email = input("Enter an email message: ")

result = predict_email(user_email)

print("\nEmail Entered:", user_email)
print("Prediction:", result)

# Language codes include "pt" for Portuguese and "es" for Spanish.
language_code = "es"

# Subjects can be math, science, computing, or humanities.
subject = input("Enter subject name in lowercase : ")
url = "https://" + language_code + ".khanacademy.org/" + subject

print(f"Navigate to the {subject} page below!")
print(url)

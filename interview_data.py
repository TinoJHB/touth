import os

def save_interview_data(interview_data):
    # Check if interview_docs folder exists
    if not os.path.exists("interview_docs"):
        os.mkdir("interview_docs")

    # Find the latest interview file number
    file_number = 1
    while os.path.exists(f"interview_docs/interview_{file_number}.txt"):
        file_number += 1

    # Save interview data to a file
    filename = f"interview_docs/interview_{file_number}.txt"
    with open(filename, "w") as f:
        for item in interview_data:
            f.write("Question: " + item["question"] + "\n")
            f.write("Answer: " + item["answer"] + "\n")
            f.write("Assessment: " + item["assessment"] + "\n")
            f.write("\n")

    # Rename all files in interview_docs folder if any are missing
    for i, file in enumerate(sorted(os.listdir("interview_docs"))):
        os.rename(f"interview_docs/{file}", f"interview_docs/interview_{i+1}.txt")

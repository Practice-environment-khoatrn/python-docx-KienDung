from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    text_content = ""

    for paragraph in doc.paragraphs:
        text_content += paragraph.text + "\n"

    return text_content

# Example usage:
file_path = "Document.docx"
content = read_docx(file_path)

# Specify the encoding when printing to the console (Windows-specific)
print(content.encode('utf-8', 'replace').decode('utf-8'))

# Write to a file with UTF-8 encoding
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(content)

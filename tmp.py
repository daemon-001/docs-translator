from PyPDF2 import PdfReader

def fix_word_warping(pdf_path):
    # Initialize a PdfReader object
    reader = PdfReader(pdf_path)
    fixed_text = []

    # Loop through each page
    for page in reader.pages:
        # Extract raw text
        raw_text = page.extract_text()

        # Fix word wrapping by removing newlines in the middle of sentences
        # cleaned_text = ' '.join(line.strip() for line in raw_text.splitlines())
        
        # Append cleaned text
        # fixed_text.append(cleaned_text)
        fixed_text.append(raw_text)


    # Join all the pages' text
    return '\n\n'.join(fixed_text)

# Example usage
pdf_path = "D:/Workspace/Project/doc-translator/new/demo.pdf"
cleaned_text = fix_word_warping(pdf_path)
print(cleaned_text)

# Save the cleaned text to a file
# with open("cleaned_text.txt", "w", encoding="utf-8") as output_file:
#     output_file.write(cleaned_text)

# print("Word warping fixed and saved to 'cleaned_text.txt'")
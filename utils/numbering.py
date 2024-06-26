doc_file = r"C:\Users\tulip\Desktop\Numbering\output_txt\temp_e5bb364ad2624f91be07df05328195e4.docx"
txt_file = r"C:\Users\tulip\Desktop\Numbering\output_txt\temp_e5bb364ad2624f91be07df05328195e4_95731ae59047483ea4a328088c02d7e2.txt"

from docx import Document
class NumberedTextReader:
    """Compare textfile content and docfile content and return numbering
    """
    def __init__(self):
        pass

    def split_paragraph(self, i, para_text):
        lines = []
        if '\n' in para_text:
            texts = para_text.split('\n')
            for t in texts:
                lines.append({'idx': i, 'txt': t})
        else:
            lines.append({'idx': i, 'txt': para_text})
        return lines

    def read_txt_lines(self, file_path):
        """
        Reads the file line by line and returns a list of lines.
        Tries 'utf-8' encoding first, then falls back to 'euc-kr' if it fails.
        """
        try:
            with open(file_path, 'r', encoding='cp949', errors='ignore') as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
        return [ l.replace('\n','') for l in lines ] 
    
    def read_doc_lines(self, file_path):
        doc = Document(file_path)
        doc_lines = []
        for i, para in enumerate(doc.paragraphs):
            para_text = para.text.strip()
            doc_lines.extend(self.split_paragraph(i, para_text))
        return doc_lines


## test
num = NumberedTextReader()
lines = num.read_doc_lines(doc_file)
print('l:', lines)

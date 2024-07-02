import os
import subprocess
import threading
import uuid
from docx import Document
from datetime import datetime

class DocxToTxtConverter:
    def __init__(self, input_file):
        
        self.output_dir = 'output_txt'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.lock = threading.Lock()

    def remove_tables_from_docx(self, doc):
        try:
            print("Removing tables from DOCX...")
            body = doc.element.body
            for tbl in body.findall('.//w:tbl', namespaces=doc.element.nsmap):
                body.remove(tbl)
            # 수정된 DOCX 파일을 임시 파일로 저장
            temp_docx_path = os.path.join(self.output_dir, 'temp_' + uuid.uuid4().hex + '.docx')
            doc.save(temp_docx_path)
            print(f"Tables removed, saved to {temp_docx_path}")
            return temp_docx_path
        except Exception as e:
            print(f"An error occurred while removing tables: {e}")
            return None

    def convert_to_txt(self, input_file):
        with self.lock:
            doc = Document(input_file)
            new_docx_path = self.remove_tables_from_docx(doc)

            # 고유한 파일 이름 생성
            unique_id = uuid.uuid4().hex
            output_txt_name = f"{os.path.basename(new_docx_path).replace('.docx', '')}_{unique_id}.txt"
            temp_txt_path = os.path.join(self.output_dir, f"{os.path.basename(new_docx_path).replace('.docx', '')}.txt")
            final_txt_path = os.path.join(self.output_dir, output_txt_name)

            subprocess.run([
                'soffice', '--convert-to', 'txt:Text', '--headless',
                '--outdir', self.output_dir, new_docx_path
            ], check=True)

            # 변환된 파일을 UUID가 포함된 이름으로 이동
            os.rename(temp_txt_path, final_txt_path)

            print('This is final_txt_path:', final_txt_path)
            return final_txt_path, new_docx_path

    def read_txt(self, txt_path):
        with open(txt_path, 'r', encoding='cp949-8') as file:
            lines = file.readlines()
        return lines


import os
import subprocess
import threading
import uuid
from docx import Document
from datetime import datetime

class DocxToTxtConverter:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.lock = threading.Lock()

    
    def convert_to_txt(self, input_file):
        with self.lock:
            new_docx_path = self.remove_tables_from_docx(input_file)

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
            return final_txt_path


    def read_txt(self, txt_path):
        with open(txt_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines


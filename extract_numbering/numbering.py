import difflib
import shutil
from docx import Document
from enums import NUMTYPES
from convert import DocxToTxtConverter

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


class DocNumberingExtractor:
    def __init__(self, input_file):
        self.numbering_data = {}
        self.out_dir = 'output_txt'
        con = DocxToTxtConverter(self.out_dir)
        self.txt_path, self.doc_path = con.convert_to_txt(input_file)
        num = NumberedTextReader()
        self.doc_lines = num.read_doc_lines(self.doc_path)
        self.txt_lines = num.read_txt_lines(self.txt_path)
        self.NUMTYPES = NUMTYPES
        self.match_document()
        self.compare_lines()
        self._rm_dir()

    def find_combined_differences(self, text1, text2):
        differ = difflib.Differ()
        diff = list(differ.compare(text1.strip(), text2.strip()))
        
        combined_diffs = []
        temp_diff = ""

        for item in diff:
            if item.startswith('+ '):
                temp_diff += item[2:]
            else:
                if temp_diff:
                    combined_diffs.append(temp_diff)
                    temp_diff = ""

        if temp_diff:
            combined_diffs.append(temp_diff)
        
        return combined_diffs

    def compare_lines(self):
        """매칭된 라인 2개에서 다른 점을 추출한다"""
        numbering_data = {}
        for i, (d, t) in enumerate(zip(self.doc_lines, self.txt_lines)):
            d_text = d['txt'].strip()
            t_text = t.strip()

            print(f'd{i}: {d_text}')
            print(f't{i}: {t_text}')
            
            if d_text == t_text:
                print('SAME!')
            else:
                print('DIFFERENCES:')
                diffs = self.find_combined_differences(d_text, t_text)
                print(diffs)
                num_type, num, numbering = self.check_is_numbering_types(diffs, d_text, t_text)
                if num_type is not None: 
                    numbering_data[i] = {
                        'num_type':num_type,
                        'num': num,
                        'numbering': numbering,
                        'is_decimal': True
                    }
            print('##############################')
        self.numbering_data = numbering_data
        print(self.numbering_data)
        return self.numbering_data


    def check_is_numbering_types(self, diffs, d_text, t_text):
        """ diffs의 요소중 1개가 t는 스트립했을때 이 요소로 시작 d는 이 요소로 시작하지 않음
                # 그리고 그 요소가 enums에 있는지 확인
                # 있으면 그 요소를 넘버링이라고 판단하고
                # 텍스트의 i번째의 넘버링은 decimal_eclose_circle 의 N+1숫자 값이며 그 텍스트는 뭐다 라고 리턴해야함

        Args:
            diffs (list): ['1. ']
            d_text(str): doc에서 추출한 텍스트.strip()
            t_text(str): txt에서 추출한 텍스트.strip()
        """
        for dif in diffs:
            if t_text.startswith(dif.strip()):# and not (d_text.startswith(dif.strip())):
                # text에서 추출되었으나 doc에서 추출되지 않은 첫글자
                for num_type, patterns in self.NUMTYPES.items():
                    if dif.strip() in patterns:
                        num = patterns.index(dif.strip()) + 1
                        return  num_type, num, dif.strip()
        return None, None, None


    def match_document(self):
        """목표: 두 라인에서 그 값이 정확하게 일치하는걸 찾는다"""
        list_a = self.doc_lines
        list_b = self.txt_lines

        def _find_same_match(target, list_b):
            target = target.strip()
            for idx_b, line_b in enumerate(list_b):
                if len(target) > 1 and (line_b.strip() == target):
                    return idx_b
            return None

        idx_b = 0
        def _get_match_idx(list_a, list_b):
            for idx_a, line_a in enumerate(list_a):
                target = line_a['txt']
                match_b_idx = _find_same_match(target, list_b[idx_b:])
                if match_b_idx:
                    return idx_a, match_b_idx
            return None, None

        idx_a, idx_b = _get_match_idx(list_a, list_b)
        line_gap = idx_a - idx_b
        if line_gap > 0:
            list_b.insert(0, '')
        elif line_gap < 0:
            list_b.pop(0)

        self.doc_lines = list_a
        self.txt_lines = list_b
    def _rm_dir(self):
        shutil.rmtree(self.out_dir)

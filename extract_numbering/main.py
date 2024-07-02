from convert import DocxToTxtConverter
from numbering import NumberedTextReader, DocNumberingExtractor
import shutil


def process_file(input_file):
    output_dir = 'output_txt'

    con = DocxToTxtConverter(output_dir)
    txt_path, doc_path = con.convert_to_txt(input_file)

    num = NumberedTextReader()
    doc_lines = num.read_doc_lines(doc_path)
    txt_lines = num.read_txt_lines(txt_path)

    ext = DocNumberingExtractor(doc_lines, txt_lines)
    ext.match_document()
    res = ext.compare_lines()
    print(res)

    # 작업 완료 후 output_txt 디렉토리 삭제
    shutil.rmtree(output_dir)

def main():
    input_file = input("Enter the path to the input file: ")
    process_file(input_file)
    
if __name__ == "__main__":
    main()
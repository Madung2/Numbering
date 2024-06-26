from utils.convert import DocxToTxtConverter
from utils.numbering import NumberedTextReader
import threading
import difflib

def compare_lines(doc_lines, txt_lines):

    for i, (d, t) in enumerate(zip(doc_lines, txt_lines)):
        d_text = d['txt']

        print(f'd{i}: {d_text}')
        print(f't{i}: {t}')
        differences =[]
        if d_text.strip() == t.strip():
            print('SAME!')
        else:
            print('DIFFERENCES:')
            differ = difflib.Differ()
            diff = list(differ.compare(d_text.strip(), t.strip()))
            
            diffs = [item[2:] for item in diff if item.startswith('+ ')] 
            print(diffs)
        print('##############################')

def main():
    input_file = '일반사모투자신탁1호(before).docx'
    output_dir = 'output_txt'

    con = DocxToTxtConverter(output_dir)
    txt_path , doc_path = con.convert_to_txt(input_file)

    num = NumberedTextReader()
    doc_lines = num.read_doc_lines(doc_path)
    txt_lines = num.read_txt_lines(txt_path)

    compare_lines(doc_lines, txt_lines)
        # # 멀티스레딩 예제
    # threads = []
    # for _ in range(5):  # 예제: 동시에 5개의 변환 작업을 수행
    #     thread = threading.Thread(target=convert_file, args=(converter, input_file))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()

if __name__ == "__main__":
    main()

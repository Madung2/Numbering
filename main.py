from utils.convert import DocxToTxtConverter
import threading

def convert_file(converter, input_file):
    try:
        txt_path = converter.convert_to_txt(input_file)
        lines = converter.read_txt(txt_path)
        for line in lines:
            print(line.strip())
    except Exception as e:
        print(f"Error during conversion: {e}")

def main():
    input_file = 'without_table.docx'
    output_dir = 'output_txt'

    converter = DocxToTxtConverter(output_dir)
    converter.convert_to_txt(input_file)

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

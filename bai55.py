import zipfile

def zip_file(file_name, zip_name):
    """
    Hàm để nén một tệp thành tệp ZIP.
    
    :param file_name: Tên tệp cần nén.
    :param zip_name: Tên tệp ZIP đầu ra.
    """
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_name)

def unzip_file(zip_name, extract_to):
    """
    Hàm để giải nén một tệp ZIP vào một thư mục.
    
    :param zip_name: Tên tệp ZIP cần giải nén.
    :param extract_to: Thư mục đích để giải nén tệp.
    """
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)

if __name__ == "__main__":
    zip_file('example.txt', 'example.zip')
    print("Đã nén 'example.txt' thành 'example.zip'")
    unzip_file('example.zip', 'extracted')
    print("Đã giải nén 'example.zip' vào thư mục 'extracted'")
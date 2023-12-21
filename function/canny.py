import cv2 as cv
import numpy as np 

class canny:
    def __init__(self):
        pass

    def filter_canny(self, file_name):
        file_path = "./img/" + file_name
        image = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
        if image is None:
            print("Unable to read the image.")
        
        # Cannyフィルタを適用
        edges = cv.Canny(image, 50, 150)  # 50と150は閾値の下限と上限を表します

        #保存するためのパス
        save_path = "./img/canny_filter/" + file_name

        # 結果の保存
        

if __name__ == "__main__":
    file_name = "Lenna.png"
    canny = canny()
    canny.filter_canny(file_name)



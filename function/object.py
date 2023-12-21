import cv2
import sys

def object(image_path):
    #image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    #if image is None:
    #    print("Unable to read the image.")
    #    return

    # Cannyフィルタを適用
    edges = cv2.Canny(image, 50, 150)  # 50と150は閾値の下限と上限を表します

    # 結果の表示
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



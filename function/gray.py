import cv2

class gray:
    def grayscale():
        # 画像の読み込み
        image = cv2.imread('input_image.jpg')

        # グレースケール変換
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # グレースケール画像の保存
        cv2.imwrite('gray_image.jpg', gray_image)

        # 2値化のための閾値設定（例：128）
        threshold_value = 128

        # 2値化
        _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

        # 2値化画像の保存
        cv2.imwrite('binary_image.jpg', binary_image)
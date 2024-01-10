import cv2 as cv
import numpy as np 

from yunet import YuNet

class mosaic:
    def __init__(self, model_path='./face_detection_yunet_2023mar.onnx', input_size=[320, 320], conf_threshold=0.9, nms_threshold=0.3, top_k=5000):
        """
        FaceDetectorクラスのコンストラクタです.

        Parameters
        ----------
        model_path : str
            モデルファイルのパス (デフォルト: './face_detection_yunet_2023mar.onnx')
        input_size : list
            モデルの入力サイズ [width, height] (デフォルト: [320, 320])
        conf_threshold : float
            信頼度の閾値 (デフォルト: 0.9)
        nms_threshold : float
            非最大抑制の閾値 (デフォルト: 0.3)
        top_k : int
            出力する候補の最大数 (デフォルト: 5000)
        """
        # YuNetモデルのインスタンスを作成します.
        self.model = YuNet(
            modelPath=model_path,        # modelPath: モデルのパス
            inputSize=input_size,        # inputSize: モデルの入力サイズ
            confThreshold=conf_threshold,    # 信頼度の閾値。この値以上の信頼度を持つバウンディングボックスのみが結果として出力されます。
            nmsThreshold=nms_threshold,     # 非最大抑制(NMS)の閾値。この値以上のIoUを持つバウンディングボックスは、NMSにより抑制されます。
            topK=top_k,             # 上位のバウンディングボックスの数. この数だけバウンディングボックスが出力されます。
            backendId=cv.dnn.DNN_BACKEND_OPENCV,         # バックエンドのID. ここではOpenCVのDNNバックエンドを使用します。(例: cv.dnn.DNN_BACKEND_OPENCV)
            targetId=cv.dnn.DNN_TARGET_CPU          # ターゲットのID ここではCPUをターゲットとします。(例: cv.dnn.DNN_TARGET_CPU)
        )
    
    def face_detection(self, file_name):
        """
        与えられた画像から顔を検出します.

        Parameters
        ----------
        image_path : str
            顔検出を行う画像のファイルパス

        Returns
        -------
        results : list
            検出された顔の情報を含むリスト. 各顔の情報は次の形式のリストで表されます.
            [x, y, width, height, confidence]

            - x: バウンディングボックスの左上隅の x 座標
            - y: バウンディングボックスの左上隅の y 座標
            - width: バウンディングボックスの幅
            - height: バウンディングボックスの高さ
            - confidence: 顔検出の信頼度（確信度）

        信頼度が指定された閾値（conf_threshold）よりも低い場合、その顔の検出結果は無視されます.
        """
        # 画像を読み込みます. ここではOpenCVのimread関数を使用しています. 
        image = cv.imread(file_name)
        # 画像の形状（高さ、幅、チャンネル数）を取得します.
        h, w, _ = image.shape
        # モデルの入力サイズを画像の幅と高さに設定します.
        self.model.setInputSize((w , h))
        # モデルを使って画像から顔を検出します.
        results = self.model.infer(image)
        return results

    def mosaic_face(self,file_name, factor = 20):
        """
        与えられた画像に対して顔を検出し、顔部分をモザイク処理します.

        Parameters
        ----------
        image_path : str
            顔検出を行う画像のファイルパス
        factor : int
            モザイク処理の程度を示す係数 (デフォルト: 20)
        """
        # 画像を読み込みます. face_detectionを使って顔を検出します.
        detected_faces = self.face_detection(file_name)
        # 画像を読み込みます. ここではOpenCVのimread関数を使用しています.
        image = cv.imread(file_name)
        # 元の画像のコピーを作成します. このコピーに対して変更を加えます.
        output = image.copy()

        # 検出結果を反復処理します. 各検出結果は、バウンディングボックスの座標を含む配列です.
        for det in detected_faces :
            bbox = det[0:4].astype(np.int32)    # バウンディングボックスの座標を整数に変換します.
            # バウンディングボックスの座標を使って顔部分を切り出します.
            x, y, w, h = bbox

            # 顔部分をモザイク処理します.
            face_roi = image[y : y + h , x : x + w]  # 顔部分を切り出します.
            small = cv.resize(face_roi, None, fx=1.0 / factor, fy=1.0 / factor, interpolation=cv.INTER_NEAREST) # 顔部分を縮小します.
            mosaic_face = cv.resize(small, (w, h), interpolation=cv.INTER_NEAREST)  # 顔部分を元のサイズに戻します.
            output[y:y + h, x:x + w] = mosaic_face  # モザイク処理した顔部分を元の画像に貼り付けます.
        # 矩形で囲まれた画像を保存する
        cv.imwrite('mosaic_output.jpg' , output)


if __name__ == '__main__':
    Mosaic = mosaic()
    Mosaic.mosaic_face('input_image.jpg')






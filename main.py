from flask import Flask, request, render_template
from os import path, remove
import base64
import json

app = Flask(__name__)

# index
@app.route('/')
def index():
    return render_template('index.html')

# upload
# パラメータ:upload_file　画像データ
# パラメータ:override_file_name ファイル名を上書きする場合に指定
# パラメータ:category 画像処理のカテゴリ(canny_filter, face_frame, face_mosaic, grayscale, object_detection)
@app.route('/upload', methods=["POST"])
def upload():
    # パラメータの取得
    file = request.files.get('upload_file')
    overrideFileName = request.values['override_file_name']
    category = request.values['category']
    # パスの生成
    filePath = './img/' + category + '/' + fileName
    # ファイル名の上書きチェック
    fileName = ""
    if(overrideFileName != ''): 
        fileName = overrideFileName
    else:
        fileName = file.filename
    # 拡張子チェック pdf以外は弾く
    if fileName.endswith('.png'):
        # 保存処理
        try:
            with open(filePath) as f:
                f.write(file.read())
        except FileExistsError:
            # ファイルが存在した場合
            print("FileExistsError")
            return ""
    return fileName

#delete
# パラメータ:category 画像処理のカテゴリ(canny_filter, face_frame, face_mosaic, grayscale, object_detection)
# パラメータ:file_name 削除するファイル名
@app.route('/delete', methods=["POST"])
def delete():
    # パラメータの取得
    fileName = request.files.get('file_name')
    category = request.values['category']
    # パスの生成
    filePath = './img/' + category + '/' + fileName
    # 存在チェック
    if path.exists(filePath):
        # 削除処理
        try:
            remove(filePath)
        except FileExistsError:
            # ファイルが存在しない場合
            print("FileNotExists")
            return False
    return True

if __name__ == '__main__':
    app.run()
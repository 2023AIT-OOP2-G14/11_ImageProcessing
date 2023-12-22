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
@app.route('/upload', methods=["POST"])
def upload():
    # パラメータの取得
    file = request.files.get('upload_file')
    overrideFileName = request.values['override_file_name']
    # パスの生成
    filePath = './img/' + fileName
    # ファイル名の上書きチェック
    fileName = ""
    if(overrideFileName != ''): 
        fileName = overrideFileName
    else:
        fileName = file.filename
    # 拡張子チェック pdf以外は弾く
    if fileName.endswith('.png'):
        # 保存処理
        file.save(filePath)
        return True
    else:
        return False

#delete
# パラメータ:file_name 削除するファイル名
@app.route('/delete', methods=["POST"])
def delete():
    # パラメータの取得
    fileName = request.files.get('file_name')
    # パスの生成
    filePath = './img/' + fileName
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
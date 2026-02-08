from flask import Flask, render_template_string
import os

# 【修正1】name ではなく __name__ （アンダーバー2つ）です
app = Flask(__name__)

@app.route('/')
def home():
    # 1. サーバーにあるHTMLファイルを読み込む
    try:
        # index.html が app.py と同じ場所にある必要があります
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        return "エラー: index.html が見つかりませんでした。app.pyと同じ場所に置いてください。"

    # 2. Renderに設定した「秘密の鍵」を取り出す
    api_key = os.environ.get('GEMINI_API_KEY')

    if not api_key:
        return "エラー: APIキーが設定されていません。RenderのEnvironment Variablesを確認してください。"

    # 3. HTMLの中の「空っぽの鍵置き場」を「本物の鍵」に書き換える
    # 注意: index.htmlの中に 'const apiKey = "AIzaSyCjj_mHySzY0qa_qRzHy6Tf1QzaotNXyms";' という文字がそのまま残っている必要があります
    html_content = html_content.replace('const apiKey = "";', f'const apiKey = "{api_key}";')

    # 4. 完成したHTMLをブラウザに送る
    return render_template_string(html_content)

# 【修正2】ここも name ではなく __name__ です
if __name__ == '__main__':
    # 【修正3】インデント（字下げ）を揃えました
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

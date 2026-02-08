from flask import Flask, render_template_string
import os
app = Flask(name)
@app.route('/')
def home():
　　　　with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
```
api_key = os.environ.get('GEMINI_API_KEY')
 
if not api_key:
    return "エラー: APIキーが設定されていません。RenderのEnvironment Variablesを確認してください。"
 
html_content = html_content.replace('const apiKey = "";', f'const apiKey = "{api_key}";')
 
return render_template_string(html_content)
 
```
if name == 'main':
port = int(os.environ.get('PORT', 10000))
app.run(host='0.0.0.0', port=port)

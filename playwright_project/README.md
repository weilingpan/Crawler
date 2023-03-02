# Setup

python -m playwright install (安装瀏覽器: chromium、frefox、webkit)

安裝成功後瀏覽器路徑會在: C:\Users\{UserName}\AppData\Local\ms-playwright

# How to Run

```python -m playwright codegen --target python -o {YourPy}.py -b chromium {url} --timeout 時間```


  -m playwright codegen: 錄製指令


  --target 指定要產生的語法語言: python, javascript


  -o: 指定要產生的檔案位置


  -b: 指定要使用的瀏覽器: chromium, firefox, webkit

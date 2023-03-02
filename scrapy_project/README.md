# Enviorment

> conda install -c conda-forge scrapy

> pip install scrapy-selenium

<br>

#### ========== 建立一個 Scrapy ==========
Scrapy 是基於 Twisted 的架構，主要包含 **ENGIN, SCHEDULER SPIDER, MIDDLEWARE, ITEM PIPELIN** 這幾個元件。

From 官方文件: https://docs.scrapy.org/en/latest/topics/architecture.html

<img src="https://docs.scrapy.org/en/latest/_images/scrapy_architecture_02.png" width=700>

From https://www.learncodewithmike.com/2020/12/python-scrapy-architecture.html

<img src="https://1.bp.blogspot.com/-ZwHUrSdRsP0/YDIWO60AS3I/AAAAAAAAE4o/2C8EFSJaB5QSG0qwa2EQh_-jBhirpNMZwCLcBGAsYHQ/s16000/python_scrapy_architecture.PNG" width=700>

其中，4、5表示下載器中間件，6、7表示爬蟲中間件。爬蟲中間件會在以下幾種情況被調用。

- 當運行到yield scrapy.Request()或者yield item的時候，爬蟲中間件的process_spider_output()方法被調用。

-  當爬蟲本身的代碼出現了Exception的時候，爬蟲中間件的process_spider_exception()方法被調用。

- 當爬蟲裡面的某一個回調函數parse_xxx()被調用之前，爬蟲中間件的process_spider_input()方法被調用。
- 當運行到start_requests()的時候，爬蟲中間件的process_start_requests()方法被調用。

##### 如何開始?

0.   使用 scrapy startproject {ProjectName} 建立一個專案目錄

下方範例的 ProjectName = news_scraper

<img src="https://1.bp.blogspot.com/-VVzY6Y3qeEM/X-hCIkkRJcI/AAAAAAAAEuQ/Ew77j4EEG20DToOfsjqSH-i5fnAeSaXkgCLcBGAsYHQ/s16000/scrapy_installation_and_create_project.PNG" width=300> 

(https://www.learncodewithmike.com/2020/12/scrapy-installation.html)

1. 查看 scrapy.cfg (根目錄)
2. 查看 settings.py，會有一些基本的設定，往後像是 chromedriver 也可以設定在此
3. 建立一個 {SpiderName}.py >>> 必須有scrapy.Spider類

    > 該類包含三個資訊: name, allowed_domains, start_urls。留意裡面的 name variable，第 7 步會使用到

4. 為了看爬蟲情形，使用 selenium 做瀏覽器的自動測試

    > settings.py 新定義 SELENIUM_DRIVER 相關資訊

    > 需留意電腦本身的 chreome version，並使用對應的 chromedriver.exe

5. 設定 proxy 

    > settings.py 開啟 SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES

    > moddlewares.py 的 DownloaderMiddleware 加入 proxy 資訊


6. 為了查看爬蟲執行時的 Log

    > settings.py 開啟 ITEM_PIPELINES

    > pipelines.py 寫 spider.logger.info() 

7. 在跟目錄執行 scrapy crawl {SpiderName}　>>> 建議 {SpiderName}.py 檔名與 name variable 統一 (比對步驟3)，雖然不統一仍可執行，因為 scrapy crawl 是讀 .py 裡面的 name variable

    **若不想透過指令來執行爬蟲，可以直接執行 Run.py**


8. 若想要儲存 log 檔 

    > settings.py 新定義 LOG_FILE = “{Path}/Log.txt”，也可定義 LOG_LEVEL = ‘INFO’ 讓Terminal 只顯示 INFO 的資訊

9. 後續若要儲存至DB，建議使用 items.py (用來定義欄位)
    
    以MongoDB為例

    > settings.py 定義 DB 基本資訊

    > piplines.py 寫 insert_db 的邏輯

<br>

#### ========== 本地安裝 MongoDB ==========


參考: https://ithelp.ithome.com.tw/articles/10186324


#### ========== 如何查看 MongoDB ==========

- 使用 Python pymongo
    
    參考: https://www.w3schools.com/python/python_mongodb_sort.asp

- 使用 Robo 3T

    參考: https://blog.csdn.net/qq_33274810/article/details/108493732


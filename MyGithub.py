import os
import shutil
import subprocess


def Create(name, type="private"):
    # def Create(name, type="public"):
    subprocess.run(
        f" gh repo create --{type} {name} ",
        shell=True
    )


def Clone(name):
    source = f"{name}"
    Desktop = os.path.expanduser("~/Desktop")
    subprocess.run(
        f" git clone https://github.com/vvn20206205/{name}",
        shell=True
    )
    shutil.move(source, Desktop)


def Zip(name):
    subprocess.run(
        f" start Chrome https://github.com/vvn20206205/{name}/archive/refs/heads/main.zip",
        shell=True
    )
               

def Delete(name):
    subprocess.run(
        f" gh repo delete --yes {name} ",
        shell=True
    )


list_name = [
# "PythonExtension",
# "PythonExtension",
# "parallel",
# "parallel",
# "StartOS",
# "StartOS",
# "Latex",
# "Latex",
# "ATS",
# "ATS",
# "template",
# "template",
# "test",
# "test",
# "products",
# "products",
# "tong-cuc-thue-demo",
# "tong-cuc-thue-demo",
# "vercel",
# "vercel",
# "email",
# "email",
# "tra_cuu_ma_so_thue",
# "tra_cuu_ma_so_thue",
# "NV2",
# "NV2",
# "BaiToanNghiepVu",
# "BaiToanNghiepVu",
# "CrawlData",
# "CrawlData",
# "CLI",
# "CLI",
# "solutions",
# "solutions",
# "DanhBa",
# "DanhBa",
# "MyBootTodoLIST",
# "MyBootTodoLIST",
# "python_web_crawl_data",
# "python_web_crawl_data",
# "NonIT",
# "NonIT",
# "FlashSaleShopee",
# "FlashSaleShopee",
# "Net",
# "Net",
# "solution",
# "solution",
# "CodeLaiDoAn",
# "LatexATS",
#     "start",
# "tong-cuc-thue-demo",
# "nestjs",
# "nghia",
# "_GTP",
# "latex_TTSS",
   
   
#    "PythonExtension",



"template",
"solutions0",
"solution",
"einvoice-system",
"CrawlData",





# 

# "Vietnamese",
# "Vietnamese",
# "Vietnamese",
# "Vietnamese",
# "report",
# "report",
# "report",
# "report",
# "report",
# "Desktop",
# "Desktop",
# "Desktop",
# "Desktop",
# "Desktop",
# "VideoVN",
# "VideoVN",
# "VideoVN",
# "VideoVN",
# "VideoVN",
# "WatchVideo",
# "WatchVideo",
# "WatchVideo",
# "WatchVideo",
# "WatchVideo",
# "StartOS",
# "StartOS",
# "StartOS",
# "StartOS",
# "StartOS",
# "cicd",
# "cicd",
# "cicd",
# "cicd",
# "cicd",
# "MyBootTodoLIST",
# "MyBootTodoLIST",
# "MyBootTodoLIST",
# "MyBootTodoLIST",
# "MyBootTodoLIST",
# "Net",
# "Net",
# "Net",
# "Net",
# "Net",
# "CLI",
# "CLI",
# "CLI",
# "CLI",
# "CLI",
# "CodeLaiDoAn",
# "CodeLaiDoAn",
# "CodeLaiDoAn",
# "CodeLaiDoAn",
# "CodeLaiDoAn",
# "DanhBa",
# "DanhBa",
# "DanhBa",
# "DanhBa",
# "DanhBa",
# "Latex",
# "Latex",
# "Latex",
# "Latex",
# "Latex",
# "CrawlData",
# "CrawlData",
# "CrawlData",
# "CrawlData",
# "CrawlData",
# "FlashSaleShopee",
# "FlashSaleShopee",
# "FlashSaleShopee",
# "FlashSaleShopee",
# "FlashSaleShopee",
# "python_web_crawl_data",
# "python_web_crawl_data",
# "python_web_crawl_data",
# "python_web_crawl_data",
# "python_web_crawl_data",
# "solution",
# "solution",
# "solution",
# "solution",
# "solution",
# "solutions0",
# "solutions0",
# "solutions0",
# "solutions0",
# "solutions0",
# "template",
# "template",
# "template",
# "template",
# "template",





]
list_name = list(set(list_name))

for name in list_name:
    # https://cli.github.com
    # print(len(list_name))
    
    # Create(name)
    # Clone(name)
    # Zip(name)
    # Delete(name)
    # 
    # Tạo lại tự động
    # Zip(name)
    # Delete(name)
    # Create(name)
    # Clone(name)



    # Zip(name)
    Delete(name)





# vercel remove --yes notifications

#  vercel remove --yes django-hello-world
#  vercel remove --yes flask-hello-world
#  vercel remove --yes flask-hello-world-fz8l

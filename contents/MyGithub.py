import os
import shutil
import subprocess


# def Create(name, type="private"):
#     # def Create(name, type="public"):
#     subprocess.run(
#         f" gh repo create --{type} {name} ",
#         shell=True
#     )


def Clone(name):
    source = f"{name}"
    Desktop = os.path.expanduser("~/Desktop")
    subprocess.run(
        f" git clone https://github.com/{author}/{name}",
        shell=True
    )
    shutil.move(source, Desktop)


def Zip(name):
    subprocess.run(
        f" start Chrome https://github.com/{author}/{name}/archive/refs/heads/main.zip",
        shell=True
    )
               

def Delete(name):
    subprocess.run(
        f" gh repo delete --yes {name} ",
        shell=True
    )


    
if __name__ == "__main__":
    author="vuvannghia452002"


    list_name = [ 
    # "Kho-Link",  
    # "Kho-Slide",  
    "Kho-Data",  
    ]

    list_name = list(set(list_name))
    print(f"🚀 Xử lý: {len(list_name)}")
    print(len(list_name))

    for name in list_name:
        
        
        
        
        # Zip(name)
        Clone(name)



        # Delete(name)
        # Create(name)

 




# vercel remove --yes notifications

#  vercel remove --yes django-hello-world
#  vercel remove --yes flask-hello-world
#  vercel remove --yes flask-hello-world-fz8l

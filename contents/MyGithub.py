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
    subprocess.run(
        f" git clone https://github.com/{author}/{name}",
        shell=True
    )

    source = f"clone/{name}"
    Desktop = os.path.expanduser("~/Desktop")
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
    author = "vuvannghia452002"

    list_name = [

        "DualBoot",
        "v2ray-ubuntu",

    ]

    list_name = list(set(list_name))
    print(f"🚀 Xử lý: {len(list_name)}")
    print(len(list_name))

    for name in list_name:
        print(f"🚀 {name}")
# gh auth login
#  gh auth refresh -h github.com -s delete_repo

        # Zip(name)
        # Clone(name)

        Delete(name)
        # Create(name)


#  vercel remove --yes flask-hello-world

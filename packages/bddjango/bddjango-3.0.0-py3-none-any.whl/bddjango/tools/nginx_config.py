"""
将nginx的配置文件替换为当前文件下的`default`, 并重启nginx
"""

import os
import platform
import shutil


assert "Linux" in platform.platform(), "必须是`Linux`版本!"

if 'Ubuntu' in platform.platform():
    is_ubuntu = True
else:
    is_ubuntu = False

package_manager = "apt-get" if is_ubuntu else "yum"
os.system(f"{package_manager} install -y nginx")

if is_ubuntu:
    dst = "/etc/nginx/sites-available/default"
    src = os.path.join(os.path.dirname(__file__), "default")
else:
    dst = "/etc/nginx/conf.d/default.conf"
    src = os.path.join(os.path.dirname(__file__), "default")


assert os.path.exists(src), f'`nginx`配置文件`default`的路径[{src}]不存在!'


shutil.copy2(src, dst)
os.system("service nginx restart")

print("nginx配置已更新.")

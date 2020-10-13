# -*- coding:utf-8 -*-
import os
import shutil


class CopyWallpaper:

    def __init__(self, steam_url, copy_dir):
        """
        类的初始化，两个地址必需传递为本地电脑的绝对路径
        :param steam_url: wallpaper的数据文件夹，例如：D:/**/Steam/steamapps/workshop/content/431960
        :param copy_dir:  你需要存储文件的地址
        """
        self.steam_url = steam_url
        self.copy_dir = copy_dir
        self.file_format = [".mp4", ".MP4", ".MOV", ".mov", ".avi", ".AVI", ".pkg"]
        self.video_format = [".mp4", ".MP4", ".MOV", ".mov", ".avi", ".AVI"]
        self.pkg_file_format = [".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG", "gif", "GIF"]
        if "img" not in os.listdir(self.copy_dir):
            os.makedirs(self.copy_dir + "/img")

    def get_repkg_img(self, list_pkg):
        """
        通过本地的pkg文件地址列表，将pkg解压后的图片文件移动到指定文件夹（copy_dir）下
        :param list_pkg: 本地的pkg文件地址列表
        :return:
        """
        pkg_path = os.getcwd() + "/repkg"
        base_driver = pkg_path[0]
        for i in list_pkg:
            if "dispose" not in os.listdir(pkg_path):
                os.makedirs(pkg_path + "/dispose")
            self.file_copy([i], "./repkg/dispose")
            pkg_name = i[str(i).rfind("/") + 1:]
            cmd_line = "%s: && cd %s && RePKG.exe extract -o ./dispose ./dispose/%s" % (base_driver, pkg_path, pkg_name)
            os.system(cmd_line)
            img_list = self.get_file_list(dir_path=pkg_path + "/dispose/materials", file_format=self.pkg_file_format)
            [self.file_copy([j], self.copy_dir + "/img") for j in img_list if os.path.getsize(j) >= 100000]
            shutil.rmtree("./repkg/dispose/")

    def file_copy(self, file_list, copy_dir=None):
        """
        一个复制文件的方法，把列表中地址的文件拷贝到指定文件夹
        :param file_list: 一个本地文件地址的列表
        :param copy_dir: 默认是self.copy_dir
        :return:
        """
        if copy_dir is None:
            copy_dir = self.copy_dir
        for i in file_list:
            copy_file_list = os.listdir(copy_dir)
            file_name = i[str(i).rfind("/") + 1:]
            if file_name in copy_file_list:
                new_name = str(i).replace(file_name, ("重复" + file_name))
                os.rename(i, new_name)
                shutil.copy(new_name, copy_dir)
                print("拷贝文件：%s" % new_name)
            else:
                shutil.copy(i, copy_dir)
                print("拷贝文件：%s" % file_name)

    def get_file_list(self, dir_path, file_list=None, file_format=None):
        """
        通过一个目录地址，递归获取目录下所有‘规定格式’的文件的地址（默认文件类型：视频、pkg）
        :param dir_path:文件夹绝对地址
        :param file_list:默认None
        :param file_format:默认None
        :return: file_list
        """
        if file_list is None:
            file_list = []
        if file_format is None:
            file_format = self.file_format

        file_in_dir_list = os.listdir(dir_path)
        for file_name in file_in_dir_list:
            url_join = dir_path + '/' + file_name
            file_type = os.path.splitext(url_join)[1]
            if os.path.isdir(url_join):
                self.get_file_list(url_join, file_list)
            elif file_type in file_format:
                file_list.append(url_join)
            else:
                pass
        return file_list

    def split_list(self, file_list):
        """
        处理单个wallpaper地址列表，变为视频和pkg文件地址的两个列表
        :param file_list:
        :return: mp4_list, pkg_list
        """
        list_mp4 = [x for x in file_list if os.path.splitext(x)[1] in self.video_format]
        list_pkg = [y for y in file_list if ".pkg" == os.path.splitext(y)[1]]
        return list_mp4, list_pkg

    def start_get_wallpaper_file(self, pkg_only=False, mp4_only=False):
        """
        一键获取所有wallpaper文件
        :return:
        """
        whole_file_list = self.get_file_list(self.steam_url)
        list_mp4, list_pkg = self.split_list(whole_file_list)
        if pkg_only:
            self.get_repkg_img(list_pkg)
        elif mp4_only:
            self.file_copy(list_mp4)
        else:
            self.get_repkg_img(list_pkg)
            self.file_copy(list_mp4)


if __name__ == '__main__':
    test = CopyWallpaper("D:/Program Files (x86)/Steam/steamapps/workshop/content/431960", "D:/test1")
    # 全部类型拷贝
    test.start_get_wallpaper_file()
    # 仅图片类型拷贝
    # test.start_get_wallpaper_file(pkg_only=True)
    # 仅视频类型拷贝
    # test.start_get_wallpaper_file(mp4_only=True)

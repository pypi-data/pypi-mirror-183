import argparse
import logging
import os
import sys
import yhgit


# -*- coding: utf-8 -*-

def debugInfo(msg):
    logging.info(msg)
    print(msg)


def parse_args():
    parse = argparse.ArgumentParser(description='modules operation')  # 2、创建参数对象
    parse.add_argument('type', type=str, help='Command Type')  # 3、命令类型
    parse.add_argument('-b', '--branch', type=str, action='store_true', help='set the name of branch')  # 3、指定分支名
    parse.add_argument('-m', '--message', action='store_true', type=str, help='set the name of branch')  # 3、指定分支名
    parse.add_argument('list', nargs='+', help='set modules')  # 3、指定分支名
    args = parse.parse_args()
    return args


if __name__ == '__main__':
    cuPath = os.getcwd()

    """
    argv[0]:  获取命令的类型 如下
    install  

    argv[1]:  命令的


    """
    # 获取参数
    argvs = sys.argv
    print(argvs)
    # 获取指令类型
    command = argvs.type

    modules = []
    print(command)
    if command == "install":
        branchname = argvs.branch
        if branchname and len(branchname) > 0:
            # 需要获取具体的分支名
            modules = argvs.list
        else:
            modules = argvs.list

        if not (branchname and len(branchname) > 0):
            # 获取本地配置的分支名称
            # 获取ymal 数据
            cuPath = os.getcwd()
            local_yaml_path = cuPath + '/PodfileLocal.yaml'
            if os.path.exists(local_yaml_path):
                podfile_module_data = yhgit.yaml_data(local_yaml_path)
                branchname = podfile_module_data.get("branch", None)
        print(branchname)
        if not (branchname and len(branchname) > 0):
            logging.error("请指定分支名字，\n 1. 指令后面指定分支 \n2. 在PodfileLoacal.yaml中指定branch")
        if not (modules and len(modules) > 0):
            logging.error("请指定具体的模块")
        else:
            yhgit().install(branchname, modules)
    elif command == "status":
        # 查看本地代码的状态
        print("进入这里面了")
        yhgit().status()
    elif command == "commit":
        commit_msg = ''
        if len(argvs) > 1:
            subcommand = argvs[1]
            if subcommand and len(subcommand) > 0 and subcommand == "-m":
                # 需要获取具体的分支名
                commit_msg = argvs[2]
        if not (commit_msg and len(commit_msg) > 0):
            debugInfo("必须添加-m 和 commit_msg")
        else:
            yhgit().commit(commit_msg)

    elif command == "pull":
        yhgit().pull()

    elif command == "push":
        yhgit().push()

    elif command == "release":
        yhgit().release()

    elif command == "clean":
        yhgit().clean()

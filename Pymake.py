import LocalCmakeBuilder
from Message import *
from pathlib import Path
import CMakeListsTemplate
import HelloWorldCPP
import HelloWorldHPP
import MainCPP
import sys

def print_help(arg_list):
    INFO("pymake help\n\t-> prints help")
    INFO("pymake build [project name]\n\t-> builds a project folder in the current working directory")
    INFO("pymake scan\n\t-> scanns the current working directory for source files to add to a local.cmake file")
    pass

def scan_source_files(x):
    project_dir = Path("./")
    src = Path("./src")
    include = Path("./include")
    if not src.exists():
        ERR("Can not scan directory!\nMissing source path!")
        return
    
    if not include.exists():
        ERR("Can not scan directory!\nMissing include path!")
        return
    LocalCmakeBuilder.generate_local_cmake(project_dir, src, include)

def build_project_folder(arg_list):
    tname = ""
    if len(arg_list) > 2:
        tname = arg_list[2]
    project_name = input("-Project Name:") if tname == None else tname

    if not project_name:
        ERR("Can not create a project without a name!")
        return

    SRC_DIR = "./src"
    
    project_dir = Path(f"./{project_name}")
    src = Path(f"./{project_name}/src")
    include = Path(f"./{project_name}/include")
    build = Path(f"./{project_name}/build")
    lib = Path(f"./{project_name}/lib")

    for e in [src, include, build, lib]:
        if not e.exists():
            e.mkdir(parents=True)
            INFO(f"Created path: {e}")

    with open(project_dir/"CMakeLists.txt", "w+") as cmake:
        cmake.write(CMakeListsTemplate.TEMPLATE_CMAKE_TXT({"ProjectName": project_name}))
        INFO(f"Created CMakeLists.txt file in: {project_dir}")

    with open(src/"Main.cpp", "w+") as main:
        main.write(MainCPP.TXT)
        INFO(f"Created Main.cpp file in: {src/'Main.cpp'}")

    with open(src/"HelloWorld.cpp", "w+") as hellocpp:
        hellocpp.write(HelloWorldCPP.TXT)
        INFO(f"Created HelloWorld.cpp file in: {src/'HelloWorld.cpp'}")

    with open(include/"HelloWorld.hpp", "w+") as hellohpp:
        hellohpp.write(HelloWorldHPP.TXT)
        INFO(f"Created HelloWorld.hpp file in: {include/'HelloWorld.hpp'}")

    LocalCmakeBuilder.generate_local_cmake(project_dir, src, include)
    INFO("Done")

if __name__ == '__main__':

    Actions = {
        "build": build_project_folder,
        "help": print_help,
        "scan": scan_source_files
    }

    args = sys.argv
    if len(args) > 1:
        action = Actions.get(args[1].lower(), lambda x: ERR("Action not supported!"))
        action(args)
    else:
        ERR("No arguments supplied!")
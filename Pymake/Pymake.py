from . import LocalCmakeBuilder
from .Message import *
from pathlib import Path
from . import CMakeListsTemplate
from . import HelloWorldCPP
from . import HelloWorldHPP
from . import MainCPP
import sys

def print_help(arg_list):
    INFO("pymake help\n\t-> prints help")
    INFO("pymake build [project name]\n\t-> builds a project folder in the current working directory")
    INFO("pymake scan\n\t-> scanns the current working directory for source files to add to a local.cmake file")
    INFO("pymake file\n\t-> creates a new file")
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

def create_new_source_file(arg_list):
    name = input("File name:>")

    if not name:
        INFO("No files created.")
        INFO("Action was aborted.")
        return

    header = f'#ifndef {name.upper()}_HPP\n#define {name.upper()}_HPP\n\n//Define stuff :D\n\n#endif //{name.upper()}_HPP'
    srcfile = f'#include "{name}.hpp"\n\n//Implement stuff :D'

    with open(f"./include/{name}.hpp", "w+") as hppfile:
        hppfile.write(header)
        INFO(f"Created {name}.hpp file in: ./include/{name}.hpp")

    with open(f"./src/{name}.cpp", "w+") as cppfile:
        cppfile.write(srcfile)
        INFO(f"Created {name}.cpp file in: ./src/{name}.cpp")

def main():
    Actions = {
        "build": build_project_folder,
        "help": print_help,
        "scan": scan_source_files,
        "file": create_new_source_file
    }

    args = sys.argv
    if len(args) > 1:
        action = Actions.get(args[1].lower(), lambda x: ERR("Action not supported!"))
        action(args)
    else:
        ERR("No arguments supplied!")

if __name__ == '__main__':
    main()
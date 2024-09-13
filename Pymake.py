import LocalCmakeBuilder
from Message import *
from pathlib import Path
import CMakeListsTemplate
import HelloWorldCPP
import HelloWorldHPP
import MainCPP

def main():
    project_name = input("-Project Name:")

    if not project_name:
        ERR("Can not create ")
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
        cmake.write(CMakeListsTemplate.TEMPLATE_CMAKE_TXT)
        INFO(f"Created CMakeLists.txt file in: {project_dir}")

    with open(src/"Main.cpp", "w+") as main:
        main.write(MainCPP.TXT)
        INFO(f"Created Main.cpp file in: {src/"Main.cpp"}")

    with open(src/"HelloWorld.cpp", "w+") as hellocpp:
        hellocpp.write(HelloWorldCPP.TXT)
        INFO(f"Created HelloWorld.cpp file in: {src/"Main.cpp"}")

    with open(include/"HelloWorld.hpp", "w+") as hellohpp:
        hellohpp.write(HelloWorldHPP.TXT)
        INFO(f"Created HelloWorld.hpp file in: {include/"Main.hpp"}")

    LocalCmakeBuilder.generate_local_cmake(project_dir, src, include)
    INFO("Done")

if __name__ == '__main__':
    main()
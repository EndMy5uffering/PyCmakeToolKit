TEMPLATE_CMAKE_TXT = """cmake_minimum_required (VERSION 3.5)
project([[PROJECT_NAME]] VERSION 0.0.1 LANGUAGES CXX)

#find_package(PACKAGE_NAME REQUIRED)

#set(SOME_LIB_HEADERS "" CACHE PATH "Path to lib" )
#set(SOME_LIB_FILE "" CACHE FILEPATH "*.a or *.lib files" )

set(OTHER_HEADER_FILES
	# put all .h here.
)

set(OTHER_SOURCE_FILES
	# put all .c/.cpp here.
)

include("${CMAKE_SOURCE_DIR}/include/local.cmake")
include("${CMAKE_SOURCE_DIR}/src/local.cmake")

include_directories(
	"${CMAKE_SOURCE_DIR}/include/"
)
add_executable("${CMAKE_PROJECT_NAME}"
	${HEADER_FILES_INCLUDE_FOLDER}
	${SOURCE_FILES_SRC_FOLDER}
	${OTHER_HEADER_FILES}
	${OTHER_SOURCE_FILES}
)

# FOR ADDING IN THE REFS OF ALL HEADER FILES OF LIBRARYS
include_directories(
	#${SOME_LIB_HEADERS}
)

# FOR LINKING TO LIBRARY FILES (*.a | *.lib)
target_link_libraries("${CMAKE_PROJECT_NAME}"
	#${SOME_LIB_FILE} 
)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
	message("Building on Mac!")
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
	message("Building on Linux!")
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
	message("You're on Windows !")
endif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")

set(SOME_STUFF OFF CACHE BOOL "Some flag")

if(SOME_STUFF)
	add_definitions(
		-DCOMPILE_WITH_SOME_PREPROCESSOR_DIRECTIVE
	)
endif(SOME_STUFF)"""
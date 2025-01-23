cmake_minimum_required(VERSION 3.10)
project(backend)

set (CMAKE_CXX_STANDARD 20)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(src)
#add_subdirectory(tests)

add_custom_target(run
    COMMAND backend
    DEPENDS backend
    COMMENT "Run backend")
#add_custom_target(test
    #COMMAND tests
    #DEPENDS tests
    #COMMENT "Test backend")
# vim:ft=cmake

#add_library(backendsrc STATIC 
    # Non-executable files go here
#)
add_executable(backend backend/Main.cpp)

target_include_directories(backend PUBLIC ./)

# vim:ft=cmake

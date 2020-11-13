cmake_minimum_required(VERSION 3.4)

set(PROJECT_NAME "pybind11_test")
set(PYTHON_VERSION "3.9")

set(CMAKE_CXX_STANDARD 11)

project(${PROJECT_NAME} CXX)

set(S_FILES_PROJ "src/cpp/main.cpp")

set(
  PROJECT_HEADER_FILES
  ""
  CACHE INTERNAL ""
)

set(
  PROJECT_SOURCE_FILES
  ${S_FILES_PROJ}
  CACHE INTERNAL ""
)

set(
  PROJECT_SOURCE_FILES
  ${PROJECT_HEADER_FILES}
  ${PROJECT_SOURCE_FILES}
  CACHE INTERNAL ""
)

add_executable(${PROJECT_NAME} ${PROJECT_SOURCE_FILES})

target_link_directories(${PROJECT_NAME} PUBLIC "python")
target_link_directories(${PROJECT_NAME} PUBLIC "/usr/local/lib/")

target_link_libraries(${PROJECT_NAME} "python${PYTHON_VERSION}")
target_link_libraries(${PROJECT_NAME} "intl")

include_directories("pybind11/include")
include_directories("python")
include_directories("python/Include")

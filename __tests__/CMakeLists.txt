set(CMAKE_CONAN_EXPECTED_HASH 52a255a933397fdce3d0937f9c737e98)
set(CMAKE_CONAN_VERSION "0.17.0")

if(EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
  file(MD5 "${CMAKE_BINARY_DIR}/conan.cmake" CMAKE_CONAN_HASH)
endif()
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake"
   OR NOT "${CMAKE_CONAN_HASH}" MATCHES "${CMAKE_CONAN_EXPECTED_HASH}")
  # Put it in CMAKE_BINARY_DIR so we don't end up with two when building OpenStudioApplication
  message(
    STATUS
      "openstudio: Downloading conan.cmake ${CMAKE_CONAN_VERSION} from https://github.com/conan-io/cmake-conan"
  )
  file(
    DOWNLOAD
    "https://github.com/conan-io/cmake-conan/raw/${CMAKE_CONAN_VERSION}/conan.cmake"
    "${CMAKE_BINARY_DIR}/conan.cmake")
else()
  message(STATUS "openstudio: using existing conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_check(VERSION 1.43.0 REQUIRED)

# This will create the conanbuildinfo.cmake in the current binary dir, not the cmake_binary_dir
conan_cmake_run(
  REQUIRES
  "openssl/1.1.1m" # A comment
  "zlib/1.2.11#683857dbd5377d65f26795d4023858f9"
  "ruby_installer/2.5.3@bincrafters/stable"
  # "bzip2/1.0.6"
  BASIC_SETUP
  CMAKE_TARGETS
  NO_OUTPUT_DIRS)

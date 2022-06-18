cmake_minimum_required(VERSION 3.2)
include(FetchContent)

project(pyuncrustify)


FetchContent_Declare(
  uncrustify
  GIT_REPOSITORY https://github.com/uncrustify/uncrustify
  GIT_TAG        639856e61770c785b5b85612e9a431d720fd8e4f # uncrustify-0.75.1
)

FetchContent_MakeAvailable(uncrustify)

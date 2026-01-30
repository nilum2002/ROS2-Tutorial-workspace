# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_testpakage_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED testpakage_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(testpakage_FOUND FALSE)
  elseif(NOT testpakage_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(testpakage_FOUND FALSE)
  endif()
  return()
endif()
set(_testpakage_CONFIG_INCLUDED TRUE)

# output package information
if(NOT testpakage_FIND_QUIETLY)
  message(STATUS "Found testpakage: 0.0.0 (${testpakage_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'testpakage' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT testpakage_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(testpakage_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${testpakage_DIR}/${_extra}")
endforeach()

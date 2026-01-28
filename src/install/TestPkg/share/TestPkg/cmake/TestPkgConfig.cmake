# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_TestPkg_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED TestPkg_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(TestPkg_FOUND FALSE)
  elseif(NOT TestPkg_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(TestPkg_FOUND FALSE)
  endif()
  return()
endif()
set(_TestPkg_CONFIG_INCLUDED TRUE)

# output package information
if(NOT TestPkg_FIND_QUIETLY)
  message(STATUS "Found TestPkg: 0.0.0 (${TestPkg_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'TestPkg' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT TestPkg_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(TestPkg_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${TestPkg_DIR}/${_extra}")
endforeach()

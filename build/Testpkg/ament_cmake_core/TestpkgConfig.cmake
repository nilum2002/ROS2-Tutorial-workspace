# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_Testpkg_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED Testpkg_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(Testpkg_FOUND FALSE)
  elseif(NOT Testpkg_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(Testpkg_FOUND FALSE)
  endif()
  return()
endif()
set(_Testpkg_CONFIG_INCLUDED TRUE)

# output package information
if(NOT Testpkg_FIND_QUIETLY)
  message(STATUS "Found Testpkg: 0.0.0 (${Testpkg_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'Testpkg' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT Testpkg_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(Testpkg_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${Testpkg_DIR}/${_extra}")
endforeach()

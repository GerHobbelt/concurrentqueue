cmake_minimum_required(VERSION 3.9)
project(concurrentqueue VERSION 0.0.99)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(concurrentqueue INTERFACE
                           "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
                           "$<INSTALL_INTERFACE:include>"
)

install(FILES
        blockingconcurrentqueue.h
        concurrentqueue.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}
)
install(TARGETS concurrentqueue
        EXPORT concurrentqueueTargets
        INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(EXPORT concurrentqueueTargets
        FILE concurrentqueueTargets.cmake
        NAMESPACE moodycamel::
        DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/cmake/concurrentqueue
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/concurrentqueueConfig.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_DEFAULT_DATAROOTDIR}/cmake/concurrentqueue
)
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/concurrentqueueConfigVersion.cmake"
    VERSION "${PROJECT_VERSION}"
    COMPATIBILITY AnyNewerVersion
)
install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/concurrentqueueConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/concurrentqueueConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/cmake/concurrentqueue
)

from conans import ConanFile, CMake, tools


class MytestpkgConan(ConanFile):
    name = "mytestpkg"
    version = "0.0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

#     def source(self):
#         self.run("git clone https://github.com/conan-io/hello.git")
#         # This small hack might be useful to guarantee proper /MT /MD linkage
#         # in MSVC if the packaged project doesn't have variables to set it
#         # properly
#         tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(HelloWorld)",
#                               '''PROJECT(HelloWorld)
# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()''')

#    def build(self):
#        cmake = CMake(self)
#        cmake.configure(source_folder="hello")
#        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.components["required_component"].names["cmake_find_package"] = "required_component"
        self.cpp_info.components["not_required_component"].names["cmake_find_package"] = "not_required_component"



from conans import ConanFile, CMake, tools


class MytestpkgConan(ConanFile):
    name = "mytestpkg"
    version = "0.0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    exports = "required.lib", "not_required.lib"

    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.components["required"].libs = ["required"]                             
        self.cpp_info.components["required"].names["cmake_find_package"] = "required"        
        self.cpp_info.components["not_required"].libs = ["not_required"]                     
        self.cpp_info.components["not_required"].names["cmake_find_package"] = "not_required"



from conans import ConanFile, CMake, tools
import shutil
import os
import subprocess

class BuildSkipPackage(ConanFile):
    name = "MyProject"
    version = "1.0"
    license = ""
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    short_paths = True
    exports_sources = "*", "test_package/*", "!conanfile.py", "!.gitignore"
    options = { "myOption" : [True, False]}
    default_options = "myOption=True"
	
    def build_id(self) :
        self.info_build.options.myOption = "Whatever"

    def build(self):
        print("BUILDING")
        cmake = CMake(self, generator="Visual Studio 15 2017 Win64")
        args = ['-DCMAKE_CONFIGURATION_TYPES=%s' % self.settings.build_type]
        cmake.configure(args=args)

    def package(self):
        print("PACKAGING")
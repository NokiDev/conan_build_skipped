from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "build_id_test" : [True, False], 
        "package_id_test" : [True, False]
    }
    default_options = "shared=False", "build_id_test=True", "package_id_test=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/memsharded/hello.git")
        self.run("cd hello && git checkout static_shared")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(MyHello)",
                              '''PROJECT(MyHello)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build_id(self):
        self.info_build.settings.build_type="Any"

    def build(self):
        self.output.info("BUILD CALLED")
        cmake = CMake(self)
        cmake.configure(source_folder="hello")
        if self.options.build_id_test : 
            i = 1/0 # Should raise ZeroDivisionError: division by zero comment it out to check package_id
        cmake.build()

        
    def package_id(self):
        self.info.settings.build_type="Any"
        
    def package(self):
        if self.options.package_id_test :
            i = 1/0 # Should raise ZeroDivisionError: division by zero
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]


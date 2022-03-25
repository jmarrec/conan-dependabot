from conans import ConanFile, CMake

class PocoTimerConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "poco/1.9.4"  # comma-separated list of requirements
    generators = "cmake", "gcc", "txt"
    default_options = {"poco:shared": True, "openssl:shared": True}

    def requirements(self):
        """
        Declare required dependencies
        """
        self.requires("zlib/1.2.11#683857dbd5377d65f26795d4023858f9")
        self.requires("openssl/1.1.1m")
        # self.requires("bzip2/1.0.6")
    def build_requirements(self):
        self.build_requires("ruby_installer/2.5.3@bincrafters/stable")

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")  # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib")  # From lib to bin

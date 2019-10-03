from conans import ConanFile, CMake, tools


class GcemConan(ConanFile):
    name = "gcem"
    version = "1.12.0"
    license = "Apache-2.0"
    author = "Andrew Marshall <planetmarshalluk@gmail.com>"
    url = "https://github.com/planetmarshall/conan-gcem"
    homepage = 'https://github.com/kthohr/gcem'
    description = "GCE-Math (Generalized Constant Expression Math) is a templated C++ library enabling compile-time computation of mathematical functions."
    topics = ("math", "compile-time")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = ['CMakeLists.txt']
    staging_folder = 'stage'

    def source(self):
        tools.get('https://github.com/kthohr/gcem/archive/v{version}.tar.gz'.format(version=self.version),
                  md5='3f0aa157c81f037cd82664cd9e031403')
        tools.replace_in_file('CMakeLists.txt', 'VERSION', self.version)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions.update(
            {
                'CMAKE_INSTALL_PREFIX': self.staging_folder,
                'BUILD_TESTS': 'ON'
            }
        )
        cmake.configure(source_folder='gcem-{version}'.format(version=self.version))
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build(target='gcem_tests')

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy('*', src=self.staging_folder)

    def package_id(self):
        self.info.header_only()

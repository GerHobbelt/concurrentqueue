from conans import ConanFile

class ConcurrentQueueConan(ConanFile):
    name = "concurrentqueue"
    version = "1.0.3"
    url = "https://github.com/Esri/concurrentqueue/tree/runtimecore"
    license = "https://github.com/Esri/concurrentqueue/blob/runtimecore/LICENSE.md"
    description = (
        "A fast multi-producer, multi-consumer lock-free concurrent queue."
    )

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/concurrentqueue/"

        # headers
        self.copy("concurrentqueue.h", src=base, dst=relative)

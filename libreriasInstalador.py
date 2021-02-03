import pip

def packetInstaller(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


libs = ["beautifulsoup4", "requests", "openpyxl", "lxml"]

for lib in libs:
    packetInstaller(str(lib))

import tarfile
tar = tarfile.open("sample.tar.gz", "w:gz")
for name in ["module_hello"]:
	tar.add(name)
tar.close()
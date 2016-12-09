import tarfile
tar = tarfile.open("sample.tar.gz", "w:gz")
for name in ["getlib.py"]:
	tar.add(name)
tar.close()
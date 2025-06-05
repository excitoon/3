import os
import subprocess
import unittest
import unittest.mock


class Test3(unittest.TestCase):
    def test_simple(self):
        env = {k: v for k, v in os.environ.items() if not k.endswith("_COLORS")}
        env["PYTHONUTF8"] = "1"
        process = subprocess.run(
            [os.path.abspath("3")],
            env=env,
            stdout=subprocess.PIPE,
        )
        self.assertEqual(process.returncode, 0)
        self.assertEqual(
            process.stdout,
            """
[01;34m.[0m
├── [01;32m3[0m
├── [01;32m3.cmd[0m
├── [01;34mexamples[0m
│   └── [00m3.png[0m
├── [00mLICENSE.md[0m
├── [00mMANIFEST.in[0m
├── [00mpyproject.toml[0m
├── [00mREADME.md[0m
├── [00mrequirements.txt[0m
├── [00msetup.py[0m
└── [00mtests.py[0m

1 directories, 10 files
""".lstrip().encode(),
        )

    def test_all(self):
        env = {k: v for k, v in os.environ.items() if not k.endswith("_COLORS")}
        env["PYTHONUTF8"] = "1"
        process = subprocess.run(
            [os.path.abspath("3"), "-a"],
            env=env,
            stdout=subprocess.PIPE,
        )
        self.assertEqual(process.returncode, 0)
        self.assertEqual(
            process.stdout,
            """
[01;34m.[0m
├── [01;34m.github[0m
│   └── [01;34mworkflows[0m
│       ├── [00mblack.yml[0m
│       ├── [00mmacos.yml[0m
│       ├── [00msetup.yml[0m
│       ├── [00mubuntu.yml[0m
│       └── [00mwindows.yml[0m
├── [00m.gitignore[0m
├── [01;32m3[0m
├── [01;32m3.cmd[0m
├── [01;34mexamples[0m
│   └── [00m3.png[0m
├── [00mLICENSE.md[0m
├── [00mMANIFEST.in[0m
├── [00mpyproject.toml[0m
├── [00mREADME.md[0m
├── [00mrequirements.txt[0m
├── [00msetup.py[0m
└── [00mtests.py[0m

3 directories, 16 files
""".lstrip().encode(),
        )

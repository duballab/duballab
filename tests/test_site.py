import pathlib
import re
import subprocess
import unittest

ROOT = pathlib.Path(__file__).parent.parent
ALT = r"""\balt=(?:[^\s>"']|"[^"]|'[^'])"""


class SiteTest(unittest.TestCase):
    def test_build_titles_and_alt(self):
        subprocess.run(["hugo", "--minify"], cwd=ROOT, check=True)
        for md in ROOT.glob("content/**/*.md"):
            self.assertRegex(md.read_text(encoding="utf-8"), r"(?m)^title:\s*\S", md)
        for html in ROOT.glob("public/**/*.html"):
            for img in re.findall(r"<img\b[^>]*>", html.read_text(encoding="utf-8")):
                self.assertRegex(img, ALT, f"{html}: {img}")


if __name__ == "__main__":
    unittest.main()

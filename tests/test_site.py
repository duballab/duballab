import pathlib
import re
import subprocess
import tempfile
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

    def test_links_respect_base_url(self):
        with tempfile.TemporaryDirectory() as out:
            subprocess.run(["hugo", "--minify", "--baseURL", "https://x.test/sub/", "-d", out], cwd=ROOT, check=True)
            for html in pathlib.Path(out).glob("**/*.html"):
                bad = re.findall(r"""(?:href|src)=["']?/(?!sub/)[a-z]\S*""", html.read_text(encoding="utf-8"))
                self.assertEqual(bad, [], html)


if __name__ == "__main__":
    unittest.main()

from setuptools import setup
import re


with open(
  "README.md",
  "r"
) as f:
  long_description = f.read()

def get(
  arg: str
):
  with open(
    'sblpy/__init__.py'
  ) as f:
    return re.search(
      fr'^__{arg}__\s*=\s*[\'"]([^\'"]*)[\'"]',
      f.read(),
      re.MULTILINE
    ).group(
      1
    )

version = get(
  'version'
)

if version.endswith(
  (
    'a',
    'b',
    'rc'
  )
):
  # append version identifier based on commit count
  try:
    import subprocess
    p = subprocess.Popen(
      [
        'git',
        'rev-list',
        '--count',
        'HEAD'
      ],
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE
    )
    out, err = p.communicate()
    if out:
      version += out.decode(
        'utf-8'
      ).strip()
      p = subprocess.Popen(
        [
          'git',
          'rev-parse',
          '--short',
          'HEAD'
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
      )
      out, err = p.communicate()
      if out:
        version += '+g' + out.decode(
          'utf-8'
        ).strip()
  except Exception:
    pass

setup(
  name="SBL.py",
  version=version,
  description="A Python api wrapper for https://smartbots.tk/ api",
  long_description=long_description,
  long_description_content_type="text/markdown",
  project_urls={
    "Documentation": "https://py.docs.smartbots.tk/en/latest/",
    "Issue tracker": "https://github.com/Rishiraj0100/SBL.py/issues",
  },
  url="https://github.com/Rishiraj0100/SBL.py",
  author=get(
    'author'
  ),
  license=get(
    'license'
  ),
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
  ],
  python_requires=">=3.8",
  keywords="SBL SmartBotList SmartBots",
  packages=[
    "sblpy",
    "sblpy.webhook"
  ]
)

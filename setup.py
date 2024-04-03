from setuptools import setup, find_packages

requirements = [
    "tqdm",
    "kaldiio",
    "torch>=1.12.0",
    "torchaudio>=0.12.0",
    "silero-vad @ git+https://github.com/pengzhendong/silero-vad.git@b9a8ecbd293dbf46697fcb3cec54c7235e14b6c2",
]

setup(
    name="wespeaker",
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "wespeaker = wespeaker.cli.speaker:main",
        ]
    },
)

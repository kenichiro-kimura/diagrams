import setuptools

setuptools.setup(
    name="diagrams",
    version="0.16.1",
    author="kkimura",
    author_email="kimura@sokohiki.org",
    description="patched diagrams",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/kenichiro-kimura/",
    packages=['resources'],
    package_dir={'resources':'resources'},
    package_data={'resources': ['*.png','*/*.png']},
    data_files=[('resources', ['resources/*.png','resources/*/*.png'])],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

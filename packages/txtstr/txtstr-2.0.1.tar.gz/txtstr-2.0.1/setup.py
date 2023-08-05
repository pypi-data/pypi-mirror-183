import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()



setuptools.setup(
    name="txtstr",
    version="2.0.1",
    author="PingüiMaya",
    description="Edit text file, encrypt and decrypt with python easily!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PinguiMaya/txtstr",
    project_urls={
        "Bug Tracker": "https://github.com/PinguiMaya/txtstr/issues",

        "Author Website" : "https://pingui.tk",
        "Donate" : "https://www.paypal.com/donate/?hosted_button_id=V6V32NHTVP4GG",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["cryptography","docx","fpdf"],
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">3.8",
)
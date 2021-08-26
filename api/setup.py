import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Wheeltrack",
    author_email="juacrojasm@correo.udistrital.edu.co",
    name="api",
    url = "www.wheeltrack.com.co",
    description="interfaces del sistema",
    version="1.0",
    long_description = README,
    packages= setuptools.find_namespace_packages(),
    zip_safe=False
)
import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Wheeltrack",
    author_email="juacrojasm@correo.udistrital.edu.co",
    name="core",
    url = "www.wheeltrack.com.co",
    description="interfaces del sistema",
    version="1.0",
    data_files=[('',['configuracion.inf'])],
    long_description = README,
    packages= setuptools.find_namespace_packages(),
    zip_safe=False
)
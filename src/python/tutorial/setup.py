import os
import setuptools

readme_path = os.path.join("..", "README.md")
with open(readme_path, "r") as f:
    long_description = f.read()

setuptools.setup(
    name                            = "z-scikit-learn",
    version                         = "0.1.0",
    author                          = "Zapata Computing, Inc.",
    author_email                    = "info@zapatacomputing.com",
    description                     = "Training models with scikit-learn in orquestra.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/luisguiserrano/tutorial-1-resource",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {"" : "python"},
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "pandas",
        "sklearn",
        "numpy"
   ],
)

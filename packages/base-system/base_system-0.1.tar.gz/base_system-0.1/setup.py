from setuptools import setup, find_packages

# with open("README.md") as f:
#     long_description = f.read()

setup(
    name="base_system",
    version='0.1',
    description="Medical system base data",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    author='zcjwin',
    author_email='win_zcj@163.com',
    url="https://devcloud.huaweicloud.com/",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    # install_requires=["djangorestframework>=3.14",],
    setup_requires=["setuptools_scm"],
    # use_scm_version=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 2",
        "Framework :: Django :: 3",
        "Framework :: Django :: 4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)

# 打包上传
# python setup.py bdist_wheel --universal
# python setup.py bdist_wheel upload

# pip install twine
# twine upload dist/SongUtils-0.0.1.tar.gz

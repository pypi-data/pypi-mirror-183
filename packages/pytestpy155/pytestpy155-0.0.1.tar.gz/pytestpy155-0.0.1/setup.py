from setuptools import setup

setup(
    # 插件的名称
    name="pytestpy155",
    # 插件的版本
    version='0.0.1',
    # 插件本地源码目录
    packages=["pytest_py155"],
    # 指定插件文件
    entry_points={
        'pytest11': [
            "pytest_py155 = pytest_py155.pytest_py15"
        ],
    },
    # pypi插件分类器
    classifiers=["Framework :: Pytest"],
)
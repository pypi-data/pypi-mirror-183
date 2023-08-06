# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mango']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['motor>=3.0.0,<4.0.0', 'pydantic>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'mango-odm',
    'version': '0.3.0',
    'description': '🥭 Async MongoDB ODM with type hints in Python',
    'long_description': '<p align="center">\n    <a name="readme-top"></a>\n    <a href="https://github.com/A-kirami/mango">\n        <img width="140px" src="https://raw.githubusercontent.com/A-kirami/mango/main/assets/mango-logo.svg" align="center" alt="Mango" />\n    </a>\n    <h1 align="center">Mango</h1>\n    <p align="center">🥭 带有类型提示的 Python 异步 MongoDB 对象文档映射器</p>\n</p>\n    <p align="center">\n        <a href="./LICENSE">\n            <img src="https://img.shields.io/github/license/A-kirami/mango.svg" alt="license">\n        </a>\n        <a href="https://pypi.python.org/pypi/mango-odm">\n            <img src="https://img.shields.io/pypi/v/mango-odm.svg" alt="pypi">\n        </a>\n        <a href="https://www.python.org/">\n            <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">\n        </a>\n    </p>\n    <p align="center">\n        <a href="#-示例">查看演示</a>\n        ·\n        <a href="https://github.com/A-kirami/mango/issues/new?assignees=&labels=bug&template=bug_report.yml&title=%5BBUG%5D%3A+">错误报告</a>\n        ·\n        <a href="https://github.com/A-kirami/mango/issues/new?assignees=&labels=enhancement&template=feature_request.yml&title=%5BFeature%5D%3A+">功能请求</a>\n    </p>\n    <p align="center">\n        <strong>简体中文</strong>\n        ·\n        <a href="/docs/README_EN.md">English</a>\n        ·\n        <a href="/docs/README_JA.md">日本語</a>\n    </p>\n</p>\n<p align="center">\n\n## 🔖 目录\n\n<details open="open">\n  <summary>目录</summary>\n  <ul>\n    <li>\n        <a href="#-简介">简介</a>\n        <ul>\n            <li><a href="#-核心特性">核心特性</a></li>\n        </ul>\n    </li>\n    <li>\n        <a href="#-安装">安装</a>\n        <ul>\n            <li><a href="#PIP">PIP</a></li>\n            <li><a href="#Poetry">Poetry</a></li>\n        </ul>\n    </li>\n    <li>\n        <a href="#-示例">示例</a>\n        <ul>\n            <li><a href="#创建您的第一个模型">创建您的第一个模型</a></li>\n            <li><a href="#将数据保存到数据库">将数据保存到数据库</a></li>\n            <li><a href="#查找符合条件的文档">查找符合条件的文档</a></li>\n            <li><a href="#修改数据库中的文档">修改数据库中的文档</a></li>\n            <li><a href="#嵌入式模型">嵌入式模型</a></li>\n            <li><a href="#连接数据库">连接数据库</a></li>\n        </ul>\n    </li>\n    <li>\n        <a href="#-贡献">贡献</a>\n        <ul>\n            <li><a href="#-鸣谢">鸣谢</a></li>\n        </ul>\n    </li>\n    <li><a href="#-支持">支持</a></li>\n    <li><a href="#-许可证">许可证</a></li>\n  </ul>\n</details>\n\n## 📖 简介\n\nMango 是一个带有类型提示的 Python 异步 MongoDB 对象文档映射器(ODM)，它构建在 [Motor](https://motor.readthedocs.io/en/stable/) 和 [Pydantic](https://pydantic-docs.helpmanual.io/) 之上。\n\nMango 使得数据建模和查询变得非常容易，帮助您关注应用程序中真正重要的部分。\n\n### ✨ 核心特性：\n\n- **完善的类型标注**：利用静态分析来减少运行时问题\n- **简洁流畅的 API**：更易于学习和使用，提高开发效率\n- **优雅的编辑器支持**：自动完成无处不在，从对象创建到查询结果\n\n<p align="right">[<a href="#readme-top">⬆回到顶部</a>]</p>\n\n## 🚀 安装\n\n### PIP\n\n```shell\npip install mango-odm\n```\n### Poetry\n\n```shell\npoetry add mango-odm\n```\n\n<p align="right">[<a href="#readme-top">⬆回到顶部</a>]</p>\n\n## 🌟 示例\n\n```python\nimport asyncio\n\nfrom mango import Document, EmbeddedDocument, Field, Mango\n\n\n# 嵌入式文档\nclass Author(EmbeddedDocument):\n    name: str\n    profile: str | None = None\n\n\n# Mango 文档模型\nclass Book(Document):\n    name: str = Field(primary_key=True)  # 将字段设置为主键，如果不显式指定主键，则会自动创建 id 字段作为主键\n    summary: str | None = None\n    author: Author  # 嵌入文档\n    price: int = Field(index=True)  # 为字段添加索引\n\n\nasync def main():\n    # 初始化 Mango，它会创建连接并初始化文档模型，你可以传入 db 或者 uri 参数来指定连接\n    await Mango.init()\n\n    # 像 pydantic 的模型一样使用\n    book = Book(name="book", author=Author(name="author"), price=10)\n    # 将它插入到数据库中\n    await book.save()\n\n    # Mango 提供了丰富的查询语言，允许您使用 Python 表达式来查询\n    if book := await Book.find(Book.price <= 20, Book.author.name == "author").get():\n        # 更新文档的 summary 字段\n        book.summary = "summary"\n        await book.update()\n\n\nif __name__ == "__main__":\n    asyncio.run(main())\n\n```\n\n<p align="right">[<a href="#readme-top">⬆回到顶部</a>]</p>\n\n## 🤝 贡献\n\n想为这个项目做出一份贡献吗？[点击这里]()阅读并了解如何贡献。\n\n### 🎉 鸣谢\n\n感谢以下开发者对该项目做出的贡献：\n\n<a href="https://github.com/A-kirami/mango/graphs/contributors">\n  <img src="https://contrib.rocks/image?repo=A-kirami/mango" />\n</a>\n\n<p align="right">[<a href="#readme-top">⬆回到顶部</a>]</p>\n\n## 💖 支持\n\n喜欢这个项目？请点亮 star 并分享它！\n\n<p align="right">[<a href="#readme-top">⬆回到顶部</a>]</p>\n\n## 📝 许可证\n\n在 `MIT` 许可证下分发。请参阅 [LICENSE](./LICENSE) 以获取更多信息。\n\n<p align="right">[<a href="#readme-top">⬆回到顶部</a>]</p>',
    'author': 'Akirami',
    'author_email': 'akiramiaya@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/A-kirami/mango',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

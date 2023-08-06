# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acac']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pydantic>=1.10.1,<2.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'readchar>=4.0.3,<5.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.5.1,<14.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0',
 'typing-extensions>=4.3.0,<5.0.0']

entry_points = \
{'console_scripts': ['acac = acac.__main__:main']}

setup_kwargs = {
    'name': 'acac',
    'version': '0.4.0',
    'description': '競プロ便利 CLI ツール。AtCoder と アルゴ式 に対応。',
    'long_description': '# acac\n\n競プロ便利 CLI ツール。[AtCoder](https://atcoder.jp/) と [アルゴ式](https://algo-method.com/) に対応。\n\n[![PyPI](https://img.shields.io/pypi/v/acac)](https://pypi.python.org/pypi/acac)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/acac)](https://pypi.python.org/pypi/acac)\n[![Tests](https://github.com/seijinrosen/acac/actions/workflows/tests.yml/badge.svg)](https://github.com/seijinrosen/acac/actions/workflows/tests.yml)\n[![CodeQL](https://github.com/seijinrosen/acac/actions/workflows/codeql.yml/badge.svg)](https://github.com/seijinrosen/acac/actions/workflows/codeql.yml)\n[![codecov](https://codecov.io/gh/seijinrosen/acac/branch/main/graph/badge.svg)](https://codecov.io/gh/seijinrosen/acac)\n[![Downloads](https://pepy.tech/badge/acac)](https://pepy.tech/project/acac)\n[![Downloads](https://pepy.tech/badge/acac/month)](https://pepy.tech/project/acac)\n[![Downloads](https://pepy.tech/badge/acac/week)](https://pepy.tech/project/acac)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n＊現在 Pre-release のため、挙動やコマンドは変更される場合があります。\n\n## 概要\n\n競技プログラミングの過去問を解くときの（個人的に）典型的なワークフローを CLI として自動化したものです。\n\n過去問だけでなく開催中のコンテストでも使えますが、ログイン機能は実装されていないため、手動で HTML ファイルを取得する必要があります。\n\n## インストール\n\nPython 3.7 以上がインストールされていれば利用可能です。\n\n```sh\npip install acac\n```\n\n## 事前準備\n\n作業ディレクトリに移動して、`acac init` を実行します。\n\n```sh\n# 例\nmkdir kyopro\ncd kyopro\nacac init\n```\n\n`acac.toml` が作成されます。これが設定ファイルです。\n\n## 使用例\n\n1. まず、ブラウザで問題ページ（例えば、[ABC 280 A - Pawn on a Grid](https://atcoder.jp/contests/abc280/tasks/abc280_a)）にアクセスします。\n\n1. URL をコピーします\n\n   - 使用可能な場合、以下のショートカットキーが便利です。\n     - Windows: <kbd>Ctrl</kbd>+<kbd>L</kbd>, <kbd>Ctrl</kbd>+<kbd>C</kbd>\n     - Mac: <kbd>command</kbd>+<kbd>L</kbd>, <kbd>command</kbd>+<kbd>C</kbd>\n\n1. ターミナルで以下のようなコマンドを実行すると、問題用のフォルダ（以下、問題フォルダ）に環境が自動作成されます。\n\n   ```sh\n   acac https://atcoder.jp/contests/abc280/tasks/abc280_a\n   ```\n\n   <details><summary>処理の詳細</summary>\n\n   - 問題フォルダを作成します。\n   - ソースコードのテンプレートファイルが用意されていれば、そのファイルをコピーします。そうでなければ、ソースコード用の空ファイルを作成します。\n   - （`cache.html` が無ければ）問題ページにアクセスし、HTML ファイルを `cache.html` として保存します。\n   - `metadata.toml` を作成します。\n     - 問題ページのタイトルと URL が格納されます。\n   - 問題ページ中からテストケースのサンプルを抽出し、テキストファイルとして保存します。\n   - `acac.toml` で設定したコマンドを実行します。\n   - `acac.toml` で設定したメッセージをクリップボードにコピーします。\n     - 私は Git のコミットメッセージを設定しています。\n\n   </details>\n\n1. コードを書いて問題を解きます。\n\n1. ターミナルで以下のようなコマンドを実行します。\n\n   ```sh\n   acac https://atcoder.jp/contests/abc280/tasks/abc280_a -j\n   ```\n\n   すると、以下のように処理されます。\n\n   - `acac.toml` で設定したコマンドを実行します（バージョン確認、コンパイル等）。\n   - 用意されたテストケースに対してジャッジを行います。\n   - `acac.toml` で設定したコマンドを実行します（クリーンアップ等）。\n   - すべて AC であれば、ソースコードがクリップボードにコピーされますので、ブラウザに貼り付けて提出してください。\n   - 「他の人の提出を確認しますか？」と聞かれるので、`y` と答えれば、同じ言語で AC した提出の一覧ページをブラウザで開きます。\n   - `acac.toml` で設定したメッセージをクリップボードにコピーします。\n\n## 設定ファイル\n\n私が実際に使用している設定ファイルは [こちら](https://github.com/seijinrosen/kyopro/blob/main/acac.toml) です。\n\n```toml\n# 設定ファイルの例\n\n[create]\n# 環境作成後に実行されるコマンドのリスト（以下は git add をして、VSCode でソースコード用のファイルを開いている）\npost_create_commands = [\n    "git add ${dir_path}/in ${dir_path}/out ${dir_path}/metadata.toml",\n    "code . ${dir_path}/${source_file_name}",\n]\n# 環境作成後にクリップボードにコピーされるメッセージ\nclipboard_message = "Create: ${url}"\n\n\n[judge]\n# ジャッジ後にソースコードをクリップボードにコピーするかどうか\ncopy_source_code_when_ac = true\n# ジャッジ後にクリップボードにコピーされるメッセージ\nclipboard_message = "AC: ${url} ${source_file_name}"\n\n\n[language]\n# デフォルトの使用言語\ndefault = "cpp"\n\n\n[language.settings.cpp]\n# ソースコードのファイル名\nsource_file_name = "main.cpp"\n# テンプレートファイルのパス\ntemplate_file_path = "templates/main.cpp"\n[language.settings.cpp.commands]\n# ジャッジ前に実行するコマンドのリスト（以下はバージョンを表示し、コンパイルしている）\npre_execute = [\n    "g++ --version",\n    "g++ ${dir_path}/${source_file_name} -o ${dir_path}/a.out",\n]\n# 実行コマンド\nexecute = "${dir_path}/a.out"\n# ジャッジ後に実行するコマンドのリスト（以下は `a.out` を削除している）\npost_execute = ["rm ${dir_path}/a.out"]\n\n\n[language.settings.python3]\n# ...\n```\n\n### `${var}` の置換リスト\n\n| 置換前              | 置換後                                         |\n| ------------------- | ---------------------------------------------- |\n| ${dir_path}         | 問題フォルダのパス                             |\n| ${lang}             | 言語名                                         |\n| ${source_file_name} | ソースコードのファイル名（パスではありません） |\n| ${url}              | 問題ページの URL                               |\n\n## コマンドオプション\n\n### モード指定\n\n| オプション   | モード                                                                  |\n| ------------ | ----------------------------------------------------------------------- |\n| -c, --create | 作業環境構築（デフォルト）                                              |\n| -j, --judge  | ジャッジ                                                                |\n| -m, --manual | URL にアクセスせず、HTML ファイルを手動で配置してテストケースを作成する |\n\nログインが必要な場合、`acac <url> -m` を実行後、問題フォルダに問題ページの HTML ファイルを配置してください。\n\n### その他\n\n`acac.toml` に指定したデフォルト値を一時的に上書きするような動きをします。イコールは必須です。\n\n| オプション                            | 上書きされるもの         |\n| ------------------------------------- | ------------------------ |\n| -l, --lang, lang=LANG_NAME            | 使用言語                 |\n| -s, --source, source=SOURCE_FILE_NAME | ソースコードのファイル名 |\n\n```sh\n# 例\nacac https://atcoder.jp/contests/abc280/tasks/abc280_a -l=python3 --source=main2.py\nacac https://atcoder.jp/contests/abc280/tasks/abc280_a -s=main2.py lang=python3 --judge\n```\n\n## コンセプト\n\n### なぜ `acac create <url>` や `acac judge <url>` のような一般的な CLI の慣例に沿っていないのか\n\n1. `acac <url>` で環境作成\n1. コードを書く\n1. ターミナルで <kbd>Ctrl</kbd>+<kbd>P</kbd>\n1. 末尾に `-j` をつけてジャッジ\n\nという流れを高速で行うためです。基本的に、一つの問題に対し複数のコマンドを実行することが多いので、URL のあとにコマンドやオプションを指定する方式を採っています。\n\n### 問題フォルダ構成が URL そのままで冗長なのはなぜか\n\n開発当初は `AtCoder/ABC/280/A/` のようなフォルダ構成にしていましたが、過去のコンテストの URL 規則との整合性や、未来への拡張性、[ghq](https://github.com/x-motemen/ghq) のような厳密性を保持するため、現在のような形にしました。\n',
    'author': 'seijinrosen',
    'author_email': '86702775+seijinrosen@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/seijinrosen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

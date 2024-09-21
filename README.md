# My Shogi Project

このプロジェクトは、Pythonで将棋の局面を扱うための `cshogi` ライブラリを使用しています。

## Set up

仮想環境を作成し、必要な依存関係をインストールします。

```bash
python3 -m venv venv
source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
pip install -r requirements.txt
```

## 使用方法

プログラムを実行するには、以下のコマンドを使用します。

```bash
python shogi_module/main.py
```

テストを実行するには、以下のコマンドを使用します。

```bash
python -m unittest discover tests
```

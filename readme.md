Flask mongodb 
======================
FlaskとMongoDBのオレオレ構成を上げていきます。

##get_db  
* view内でデータを取り出さないようにするためのデコレータ

使い方
------
usersというコレクションが存在してその中に
	{
		"_id": int,
		"name": str,
		"age": int,
	}
というデータが入っているとする。

### get_dbの使い方 ###
	from flask_mongodb_tools import get_db
	@app.route("/user/<int:id>")
	@get_db("users")
	def user_page(id, users):
		return users["name"] + str( users["age"] )

パラメータの解説
----------------
リストの間に空行を挟むと、それぞれのリストに `<p>` タグが挿入され、行間が
広くなります。

def get_db(collection, id_name="id", arg_name=None)

+   `collection` :
  dbのデータを引っ張ってくるコレクション名

+   `id_name` :
  routeから回ってくるidの名前 デフォルトでは"id"が適用される

+   `arg_name` :
  viewに渡す引数の名前 デフォルトではコレクション名が使われる

ライセンス
----------
Copyright &copy; 2013 2/17
Licensed under the [Apache License, Version 2.0][Apache]
Distributed under the [MIT License][mit].
Dual licensed under the [MIT license][MIT] and [GPL license][GPL].

[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
[GPL]: http://www.gnu.org/licenses/gpl.html

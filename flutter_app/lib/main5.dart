import 'package:flutter/material.dart';

// 路由参数传递

// 定义数据类型
class Product {
  final String title;
  final String description;
  Product(this.title, this.description);
}

// 生成数据列表
void main() {
  // 传递参数到页面
  runApp(MaterialApp(
    title: "数据传递案例",
    home: ProductList(
        products: List.generate(
            20, (i) => Product('商品  $i', "这是一个商品详情，编号为 :$i"))), //生成数据
  ));
}

class ProductList extends StatelessWidget {
  // 定义参数
  final List<Product> products;
  // 接收参数
  ProductList({Key key, @required this.products}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("商品列表")),
      body: ListView.builder(
        itemCount: products.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(products[index].title),
            onTap: () {
              // 跳转传参
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => new ProductDetail(
                            product: products[index],
                          )));
            },
          );
        },
      ),
    );
  }
}

// 接收页面
class ProductDetail extends StatelessWidget {
  final Product product;
  ProductDetail({Key key, @required this.product}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: AppBar(
        title: Text("${product.title}"),
      ),
      body: Center(
        child: Text('${product.description}'),
      ),
    );
  }
}

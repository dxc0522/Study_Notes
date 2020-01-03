import 'package:flutter/material.dart';

void main() => runApp(MyApp3());

// 不灵活排列方式，不会充满横排，而是根据内容大小自由排列的
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "list View Widget",
        home: Scaffold(
          appBar: new AppBar(
            title: new Text('水平方向布局'),
          ),
          body: new Row(
            children: <Widget>[
              new RaisedButton(
                onPressed: () {},
                color: Colors.redAccent,
                child: new Text("红色按钮"),
              ),
              new RaisedButton(
                onPressed: () {},
                color: Colors.orangeAccent,
                child: new Text("黄色按钮"),
              ),
              new RaisedButton(
                onPressed: () {},
                color: Colors.pinkAccent,
                child: new Text("粉色按钮"),
              ),
            ],
          ),
        ));
  }
}

// 扩展包裹，充满横屏
class MyApp2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "listView widget",
        home: Scaffold(
          appBar: new AppBar(
            title: new Text("水平方向布局"),
          ),
          body: new Row(
            children: <Widget>[
              new RaisedButton(
                onPressed: () {},
                color: Colors.redAccent,
                child: new Text("红色按钮"),
              ),
              Expanded(
                //扩展组件
                child: new RaisedButton(
                  onPressed: () {},
                  color: Colors.orangeAccent,
                  child: new Text("黄色按钮"),
                ),
              ),
              new RaisedButton(
                onPressed: () {},
                color: Colors.pinkAccent,
                child: new Text("粉色按钮"),
              ),
            ],
          ),
        ));
  }
}

// 垂直组件
class MyApp3 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "List View widget",
        home: Scaffold(
          appBar: new AppBar(
            title: new Text("垂直方向布局"),
          ),
          body: Column(
            // 交叉轴/横轴/副轴对齐 cross是副轴的意思方向看容器而言
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Text("i love money"),
              Text("i very love swim"),
              Text("i love china"),
            ],
          ),
        ));
  }
}

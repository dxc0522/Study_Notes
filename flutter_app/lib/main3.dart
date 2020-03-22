import 'package:flutter/material.dart';

void main() => runApp(MyApp5());

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
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Center(
                child: Text("i love money"),
              ),
              Expanded(
                child: Text("i very love swim"),
              ),
              Center(
                child: Text("i love china"),
              ),
            ],
          ),
        ));
  }
}

// 层叠布局
class MyApp4 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "listView",
      home: Scaffold(
        appBar: new AppBar(
          title: new Text("垂直布局"),
        ),
        body: Center(
          child: new Stack(
            //叠放的意思，层叠组件多个层叠
            alignment: const FractionalOffset(0.5, 0.8), //传入坐标比例
            children: <Widget>[
              new CircleAvatar(
                backgroundImage: new NetworkImage(
                    "https://cdn.jsdelivr.net/gh/dxc0522/cdn_assets@3.7/img/custom/avatar.jpeg"),
                radius: 50.0,
              ),
              new Container(
                decoration: new BoxDecoration(color: Colors.lightBlue),
                padding: EdgeInsets.all(5.0),
                child: new Text('娃哈哈'),
              ),
              new Positioned(
                //定位组件，自行更改位置
                top: 10.0,
                left: 10.0,
                child: new Text("第一行"),
              ),
              new Positioned(
                top: 30.0,
                left: 10.0,
                child: new Text("第二行"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// 卡片布局
class MyApp5 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var card = new Card(
      child: Column(
        children: <Widget>[
          ListTile(
            title: new Text(
              "河南省漯河市",
              style: TextStyle(fontWeight: FontWeight.w500),
            ),
            subtitle: new Text("doudou"),
            leading: new Icon(
              Icons.account_box,
              color: Colors.lightBlue,
            ),
          ),
          new Divider(),
          ListTile(
            title: new Text(
              "河南省漯河市",
              style: TextStyle(fontWeight: FontWeight.w500),
            ),
            subtitle: new Text("doudou"),
            leading: new Icon(
              Icons.account_box,
              color: Colors.lightBlue,
            ),
          ),
          new Divider(),
        ],
      ),
    );
    return MaterialApp(
      title: "list view",
      home: Scaffold(
        appBar: new AppBar(
          title: new Text("卡片布局"),
        ),
        body: Center(
          child: card,
        ),
      ),
    );
  }
}

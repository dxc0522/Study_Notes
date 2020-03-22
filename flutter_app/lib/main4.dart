import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    title: "导航演示",
    home: new FristScreen(),
  ));
}

class FristScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text("导航页面"),
      ),
      body: Center(
        child: new RaisedButton(
          child: Text("查看商品详情"),
          onPressed: () {
            Navigator.push(
                context,
                new MaterialPageRoute(
                    builder: (context) => new SecondScreen()));
          },
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(
        title: new Text("详情页"),
      ),
      body: Center(
        child: RaisedButton(
          child: Text("返回"),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}

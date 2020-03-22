import 'package:flutter/material.dart';
import 'home_screen.dart';
import 'pages_screen.dart';
import 'airplay_screen.dart';

import 'each_view.dart';

class BottomAppBarDemo extends StatefulWidget {
  @override
  _BottomAppBarDemoState createState() => _BottomAppBarDemoState();
}

class _BottomAppBarDemoState extends State<BottomAppBarDemo> {
  List<Widget> _eachView;
  int _index = 0;
  @override
  void initState() {
    super.initState();
    _eachView = List();
    _eachView..add(EachView("home"))..add(EachView("Me"));
  }

  Widget build(BuildContext context) {
    return Scaffold(
      body: _eachView[_index],
      // 浮动按钮
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.of(context)
              .push(MaterialPageRoute(builder: (BuildContext context) {
            return EachView("New Page");
          }));
        },
        tooltip: "Increment",
        // 工具提示
        child: Icon(
          Icons.add,
          color: Colors.white,
        ),
      ),
      // 浮动按钮位置：中心对接
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      bottomNavigationBar: BottomAppBar(
        color: Colors.lightBlue,
        shape: CircularNotchedRectangle(),
        // 形状：圆形缺口矩阵
        child: Row(
          // 主轴大小
          mainAxisSize: MainAxisSize.max,
          // 主轴对齐方式
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[
            IconButton(
              icon: Icon(Icons.home),
              color: Colors.white,
              onPressed: () {
                setState(() {
                  _index = 0;
                });
              },
            ),
            IconButton(
              icon: Icon(Icons.airport_shuttle),
              color: Colors.white,
              onPressed: () {
                setState(() {
                  _index = 1;
                });
              },
            ),
          ],
        ),
      ),
    );
  }
}

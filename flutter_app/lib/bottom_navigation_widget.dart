import 'package:flutter/material.dart';
import 'home_screen.dart';
import 'pages_screen.dart';
import 'email_screen.dart';
import 'airplay_screen.dart';

class BottomNavigationWidget extends StatefulWidget {
  @override
  _BottomNavigationWidgetState createState() => _BottomNavigationWidgetState();
}

class _BottomNavigationWidgetState extends State<BottomNavigationWidget> {
  // 定义同一颜色
  final _BottomNavigationColor = Colors.blue;
  // 定义下标
  int _currentIndex = 0;
  // 定义页面列表
  List<Widget> list = List();
  @override
  // 扩展运算填入页面
  void initState() {
    list
      ..add(HomeScreen())
      ..add(EmailScreen())
      ..add(PagesScreen())
      ..add(AirplayScreen());
    super.initState();
  }

  Widget build(BuildContext context) {
    return Scaffold(
      body: list[_currentIndex],
      // 根据下标展示页面
      bottomNavigationBar: BottomNavigationBar(
        items: [
          BottomNavigationBarItem(
              icon: Icon(Icons.home, color: _BottomNavigationColor),
              title: Text("Home",
                  style: TextStyle(color: _BottomNavigationColor))),
          BottomNavigationBarItem(
              icon: Icon(Icons.email, color: _BottomNavigationColor),
              title: Text("Email",
                  style: TextStyle(color: _BottomNavigationColor))),
          BottomNavigationBarItem(
              icon: Icon(Icons.pages, color: _BottomNavigationColor),
              title: Text("Pages",
                  style: TextStyle(color: _BottomNavigationColor))),
          BottomNavigationBarItem(
              icon: Icon(Icons.airplay, color: _BottomNavigationColor),
              title: Text("Airplay",
                  style: TextStyle(color: _BottomNavigationColor))),
        ],
        currentIndex: _currentIndex,
        // 显示指定下标
        onTap: (int index) {
          // 点击方法并定义接收参数
          setState(() {
            _currentIndex = index;
          });
        },
      ),
    );
  }
}

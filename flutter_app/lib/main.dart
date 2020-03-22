import 'package:flutter/material.dart';
import 'bottom_navigation_widget.dart';
import 'bottom_appbar_demo.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "flutter bottom navigationbar",
      // theme: ThemeData.light(),
      // home: BottomNavigationWidget(),
      // 主题颜色
      theme: ThemeData(primarySwatch: Colors.lightBlue),
      home: BottomAppBarDemo(),
    );
  }
}

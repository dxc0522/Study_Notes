import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(title: "页面跳转返回值", home: FirstPage()));
  //意思好像是只有一层路由就没法往回退of了，所以要加一个基础的widget在runApp
}

class FirstPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("去要号码"),
        ),
        body: Column(
          children: <Widget>[
            RouterButton(),
            Image.asset(
              "img/jd.png",
              width: 100.0,
              height: 100.0,
            ),
            Image.asset(
              "img/jd.png",
              width: 100.0,
              height: 100.0,
            ),
          ],
        ));
  }
}

class RouterButton extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return RaisedButton(
      onPressed: () {
        _navigateToGetNumber(context);
      },
      child: Text("点击跳转要号码"),
    );
  }

// 自有方法的调用
  _navigateToGetNumber(BuildContext context) async {
    final result = await Navigator.push(
        context, MaterialPageRoute(builder: (context) => SecendPage()));
    // showSnackBar为展示弹框记录下个页面退出后的返回值
    Scaffold.of(context).showSnackBar(SnackBar(
      content: Text("$result"),
    )); //意思好像是只有一层路由就没法往回退of了，所以要加一个基础的widget在runApp
  }
}

class SecendPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: new Text("我是号码页面"),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            RaisedButton(
              child: Text("一号种子选手"),
              onPressed: () {
                // 返回上一页，并且带参数
                Navigator.pop(context, '一号：111111');
              },
            ),
            RaisedButton(
              child: Text("二号种子选手"),
              onPressed: () {
                Navigator.pop(context, '三号：222222');
              },
            ),
            RaisedButton(
              child: Text("三号种子选手"),
              onPressed: () {
                Navigator.pop(context, '三号：333333');
              },
            ),
          ],
        ),
      ),
    );
  }
}

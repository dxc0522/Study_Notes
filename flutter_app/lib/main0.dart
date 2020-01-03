import 'package:flutter/material.dart';

void main() => runApp(MyApp3());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Text',
        home: Scaffold(
          body: Center(
            child: Container(
              child: new Text(
                'Hello JSPang',
                textAlign: TextAlign.left, //文字样式
                maxLines: 1, //最多几行
                style: TextStyle(
                    //css样式
                    fontSize: 25.0,
                    color: Color.fromARGB(255, 255, 150, 150),
                    decoration: TextDecoration.underline,
                    decorationStyle: TextDecorationStyle.solid),
              ),
              alignment: Alignment.topLeft, //children对齐方式
              padding:
                  const EdgeInsets.fromLTRB(10.0, 30.0, 0.0, 0.0), //padding
              margin: const EdgeInsets.all(10.0), //margin
              decoration: new BoxDecoration(
                  gradient: const LinearGradient(colors: [
                    Colors.lightBlue,
                    Colors.greenAccent,
                    Colors.purple
                  ]), //背景
                  border: Border.all(width: 4.0, color: Colors.red)), //边框
            ),
          ),
        ));
  }
}

class MyApp1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Text",
      home: Scaffold(
        body: Center(
          child: Container(
            child: new Image.network(
              'https://www.dd6688.club/assets/img/system.jpg',
              scale: 1.0,
              // fit: BoxFit.cover,//图片是否拉伸
              color: Colors.greenAccent, //图片颜色
              colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
              repeat: ImageRepeat.repeatY, //平铺
            ),
            width: 600.0,
            height: 600.0,
            color: Colors.lightBlue,
          ),
        ),
      ),
    );
  }
}

class MyApp2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "flutter Demo",
        home: Scaffold(
            appBar: new AppBar(
              title: new Text("List Widget"),
            ),
            body: new ListView(
              children: <Widget>[
                new ListTile(
                  leading: new Icon(Icons.access_time),
                  title: new Text("access_time"),
                ),
                new ListTile(
                  leading: new Icon(Icons.account_balance),
                  title: new Text("account_balance"),
                ),
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  scale: 1.0,
                  height: 200.0,
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  scale: 1.0,
                  height: 200.0,
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  scale: 1.0,
                  height: 200.0,
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
              ],
            )));
  }
}

class MyApp3 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Text widget",
      home: Scaffold(
        body: Center(
          child: Container(
            height: 200.0,
            child: new ListView(
              scrollDirection: Axis.horizontal,
              children: <Widget>[
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
                new Image.network(
                  'https://www.dd6688.club/assets/img/system.jpg',
                  fit: BoxFit.cover, //图片是否拉伸
                  color: Colors.greenAccent, //图片颜色
                  colorBlendMode: BlendMode.darken, //图片与颜色的混合模式
                  // repeat: ImageRepeat.repeat, //平铺
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

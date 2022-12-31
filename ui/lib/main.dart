import 'package:flutter/material.dart';
import 'package:window_size/window_size.dart';
import 'dart:io';

extension ColorExtension on String {
  toColor() {
    var hexString = this;
    final buffer = StringBuffer();
    if (hexString.length == 6 || hexString.length == 7) buffer.write('ff');
    buffer.write(hexString.replaceFirst('#', ''));
    return Color(int.parse(buffer.toString(), radix: 16));
  }
}

void main() {
  if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
    setWindowTitle('Податковий помічий 23.');
    setWindowMaxSize(const Size(1200, 765));
    setWindowMinSize(const Size(1200, 765));
  }
  runApp(VatReport());
}

class VatReport extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Container(
              color: '#DDDDDD'.toColor(),
              width: 1200.0,
              height: 125.0,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  TextButton(
                    style: TextButton.styleFrom(
                        backgroundColor: '#E41E12'.toColor(),
                        padding: EdgeInsets.fromLTRB(14, 25, 14, 25),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(
                          15,
                        ))),
                    onPressed: () {},
                    child: Text('Податкові накладні',
                        style: TextStyle(
                            fontSize: 30, color: '#EFEFEF'.toColor())),
                  ),
                  SizedBox(width: 100),
                  TextButton(
                    style: TextButton.styleFrom(
                        backgroundColor: '#E41E12'.toColor(),
                        padding: EdgeInsets.fromLTRB(14, 25, 14, 25),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(
                          15,
                        ))),
                    onPressed: () {},
                    child: Text('Акциз',
                        style: TextStyle(
                            fontSize: 30, color: '#EFEFEF'.toColor())),
                  ),
                ],
              )),
          Row(
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  IntrinsicWidth(
                      child: Container(
                    decoration: BoxDecoration(
                        border: Border.all(color: Colors.blueAccent)),
                    child: Text('My Awesome Border'),
                  ))
                ],
              ),
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Row(
                    children: [Text("TEST")],
                  )
                ],
              )
            ],
          )
        ],
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';
import 'package:ui/widgets/color_text_button.dart';

class Header extends StatefulWidget {
  final String _text;
  final double textSize;
  const Header(this._text, this.textSize, {super.key});

  @override
  State<Header> createState() => _HeaderState();
}

class _HeaderState extends State<Header> {
  @override
  Widget build(BuildContext context) {
    return Container(
        color: Style.LIGHT_GREY,
        width: 1200.0,
        height: 125.0,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [ColorTextButton(widget._text, widget.textSize)],
        ));
  }
}

import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';

class ColoredText extends StatelessWidget {
  final String _text;
  final double _textSize;
  final FontWeight _fontWeight;
  const ColoredText(this._text, this._textSize, this._fontWeight, {super.key});

  @override
  Widget build(BuildContext context) {
    return Text(_text,
        style: TextStyle(fontSize: _textSize, fontWeight: _fontWeight, color: Style.GREY));
  }
}

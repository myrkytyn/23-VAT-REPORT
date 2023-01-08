import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';

class ColorTextButton extends StatefulWidget {
  final String _text;
  final double textSize;
  const ColorTextButton(this._text, this.textSize, {super.key});

  @override
  State<ColorTextButton> createState() => _ColorTextButtonState();
}

class _ColorTextButtonState extends State<ColorTextButton> {
  @override
  Widget build(BuildContext context) {
    return TextButton(
      style: TextButton.styleFrom(
          backgroundColor: Style.LIGHT_RED,
          padding: const EdgeInsets.fromLTRB(24, 18, 24, 18),
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(15))),
      onPressed: () {},
      child: Text(widget._text,
          style: TextStyle(fontSize: widget.textSize, color: Style.WHITE)),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';
import 'package:ui/widgets/color_switch.dart';

class ColorSwitchTextRow extends StatefulWidget {
  final String _text;
  bool database;
  ColorSwitchTextRow(this.database, this._text, {super.key});

  @override
  State<ColorSwitchTextRow> createState() => _ColorSwitchTextRowState();
}

class _ColorSwitchTextRowState extends State<ColorSwitchTextRow> {
  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        ColorSwitch(widget.database),
        Text(widget._text, style: TextStyle(fontSize: 20, color: Style.GREY)),
      ],
    );
  }
}

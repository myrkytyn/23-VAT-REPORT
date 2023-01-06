import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';

class ColorSwitch extends StatefulWidget {
  bool database;
  ColorSwitch(this.database, {super.key});

  @override
  State<ColorSwitch> createState() => _ColorSwitchState();
}

class _ColorSwitchState extends State<ColorSwitch> {
  @override
  Widget build(BuildContext context) {
    return Switch(
      value: widget.database,
      activeColor: Style.RED,
      onChanged: (bool value) {
        setState(() {
          widget.database = value;
        });
      },
    );
  }
}

import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:ui/styles/colors.dart';
import 'package:ui/widgets/text.dart';

class CheckboxText extends StatefulWidget {
  bool isChecked = true;
  final String _text;
  final double _textSize;
  final _fontWeight;
  CheckboxText(this._text, this._textSize, this._fontWeight, {super.key});

  @override
  State<CheckboxText> createState() => _CheckboxTextState();
}

class _CheckboxTextState extends State<CheckboxText> {
  Color getColor(Set<MaterialState> states) {
    const Set<MaterialState> interactiveStates = <MaterialState>{
      MaterialState.pressed,
      MaterialState.hovered,
      MaterialState.focused,
    };
    if (states.any(interactiveStates.contains)) {
      return Style.GREY;
    }
    return Style.RED;
  }

  @override
  Widget build(BuildContext context) {
    return Row(children: [
      Checkbox(
        checkColor: Style.WHITE,
        fillColor: MaterialStateProperty.resolveWith(getColor),
        value: widget.isChecked,
        onChanged: (bool? value) {
          setState(() {
            widget.isChecked = value!;
          });
        },
      ),
      ColoredText(widget._text, widget._textSize, widget._fontWeight)
    ]);
  }
}

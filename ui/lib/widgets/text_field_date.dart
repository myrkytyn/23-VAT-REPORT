import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';

class TextFieldDate extends StatefulWidget {
  final String _hintText;
  final RegExp regExp = RegExp(
      r"(0[1-9]|[12][0-9]|3[01])\.(0[13578]|1[02])\.(2022|2023|2024|2025)|(0[1-9]|[12][0-9]|30)\.(0[469]|11)\.(2022|2023|2024|2025)|(0[1-9]|[12][0-9])\.02\.(2022|2023|2024|2025)");
  TextFieldDate(this._hintText, {super.key});

  @override
  State<TextFieldDate> createState() => _TextFieldDateState();
}

class _TextFieldDateState extends State<TextFieldDate> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 200,
        child: TextField(
          maxLength: 10,
          textAlign: TextAlign.center,
          cursorColor: Style.GREY,
          decoration: InputDecoration(
              counterText: "",
              border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                  borderSide: BorderSide(color: Style.GREY)),
              focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                  borderSide: BorderSide(color: Style.GREY)),
              hintText: widget._hintText),
        ));
  }
}

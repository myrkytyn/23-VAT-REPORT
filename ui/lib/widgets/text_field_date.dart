import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';

class TextFieldDate extends StatefulWidget {
  final String _hintText;
  final TextEditingController myController;
  const TextFieldDate(this._hintText, this.myController, {super.key});

  @override
  State<TextFieldDate> createState() => _TextFieldDateState();
}

class _TextFieldDateState extends State<TextFieldDate> {
  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    widget.myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 200,
        child: TextField(
          controller: widget.myController,
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

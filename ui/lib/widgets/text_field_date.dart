import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class TextFieldDate extends StatefulWidget {
  final String _hintText;
  final RegExp regExp = new RegExp(r'[A-Z]{5}[0-9]{4}[A-Z]{1}$');
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
          inputFormatters: <TextInputFormatter>[
            FilteringTextInputFormatter.allow(widget.regExp),
          ],
          decoration: InputDecoration(
            border: OutlineInputBorder(borderRadius: BorderRadius.circular(15)),
            hintText: widget._hintText,
          ),
        ));
  }
}

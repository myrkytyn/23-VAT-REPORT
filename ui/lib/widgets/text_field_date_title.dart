import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';
import 'package:ui/widgets/text_field_date.dart';

class TextFieldDateTitle extends StatefulWidget {
  final String _hintText;
  final String _text;
  final TextEditingController myController;
  const TextFieldDateTitle(this._hintText, this._text, this.myController,
      {super.key});

  @override
  State<TextFieldDateTitle> createState() => _TextFieldDateTitleState();
}

class _TextFieldDateTitleState extends State<TextFieldDateTitle> {
  @override
  Widget build(BuildContext context) {
    return Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            const SizedBox(width: 10),
            Text(widget._text,
                style: TextStyle(
                    fontWeight: FontWeight.w500,
                    fontSize: 20,
                    color: Style.GREY)),
          ]),
          const SizedBox(height: 2),
          TextFieldDate(widget._hintText, widget.myController)
        ]);
  }
}

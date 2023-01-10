import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';
import 'package:ui/widgets/text_field_date_title.dart';

class DateRow extends StatefulWidget {
  final String _hintText;
  final String _textFrom;
  final String _textTo;
  final TextEditingController fromDateController;
  final TextEditingController toDateController;
  const DateRow(this._hintText, this._textFrom, this._textTo,
      this.fromDateController, this.toDateController,
      {super.key});

  @override
  State<DateRow> createState() => _DateRowState();
}

class _DateRowState extends State<DateRow> {
  @override
  Widget build(BuildContext context) {
    return Row(children: [
      TextFieldDateTitle(
          widget._hintText, widget._textFrom, widget.fromDateController),
      const SizedBox(width: 35),
      Icon(Icons.east, color: Style.GREY),
      const SizedBox(width: 35),
      TextFieldDateTitle(
          widget._hintText, widget._textTo, widget.toDateController)
    ]);
  }
}

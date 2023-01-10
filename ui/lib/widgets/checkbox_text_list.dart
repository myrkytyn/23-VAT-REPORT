import 'package:flutter/material.dart';
import 'package:ui/widgets/checkbox_text.dart';

import '../use_case/restaurant_list.dart';

class CheckBoxTextList extends StatefulWidget {
  final double _textSize;
  final FontWeight _fontWeight;
  const CheckBoxTextList(this._textSize, this._fontWeight, {super.key});

  @override
  State<CheckBoxTextList> createState() => _CheckBoxTextListState();
}

class _CheckBoxTextListState extends State<CheckBoxTextList> {
  @override
  Widget build(BuildContext context) {
    List<Widget> list = [];
    var restaurants = GetRestaurnats.getRestaurnatsList();
    restaurants.forEach((item) {
      list.add(CheckboxText(item, widget._textSize, widget._fontWeight));
      list.add(const SizedBox(height: 15));
    });
    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: list,
    );
  }
}

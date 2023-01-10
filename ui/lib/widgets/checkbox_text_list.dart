import 'package:flutter/material.dart';
import 'package:ui/widgets/checkbox_text.dart';

import '../use_case/restaurant_list.dart';

class CheckBoxTextList extends StatefulWidget {
  final double _textSize;
  final FontWeight _fontWeight;
  static Map<String, bool> restaurantsMap = {};
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
      CheckBoxTextList.restaurantsMap[item] = true;
    });
    CheckBoxTextList.restaurantsMap.forEach((key, value) {
      list.add(CheckboxText(key, widget._textSize, widget._fontWeight, value));
      list.add(const SizedBox(height: 15));
    });
    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: list,
    );
  }
}

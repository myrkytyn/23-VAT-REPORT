import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';
import 'color_text_button.dart';

class TextButtonWithIcon extends StatefulWidget {
  final String _text;
  final double textSize;
  final VoidCallback onPressedIcon;
  final VoidCallback onPressedButton;
  const TextButtonWithIcon(this._text, this.textSize, this.onPressedIcon,this.onPressedButton,
      {super.key});

  @override
  State<TextButtonWithIcon> createState() => _TextButtonWithIconState();
}

class _TextButtonWithIconState extends State<TextButtonWithIcon> {
  @override
  Widget build(BuildContext context) {
    return Row(children: [
      ColorTextButton(widget._text, widget.textSize, widget.onPressedButton),
      const SizedBox(width: 10),
      IconButton(
          color: Style.GREY,
          icon: const Icon(
            Icons.folder_open,
          ),
          iconSize: 40,
          onPressed: widget.onPressedIcon)
    ]);
  }
}

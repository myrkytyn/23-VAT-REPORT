import 'package:flutter/material.dart';
import 'package:ui/styles/colors.dart';
import 'package:ui/use_case/open_folder.dart';
import 'color_text_button.dart';

class TextButtonWithIcon extends StatefulWidget {
  final String _text;
  final double textSize;
  final String _folder;
  const TextButtonWithIcon(this._text, this.textSize, this._folder,
      {super.key});

  @override
  State<TextButtonWithIcon> createState() => _TextButtonWithIconState();
}

class _TextButtonWithIconState extends State<TextButtonWithIcon> {
  @override
  Widget build(BuildContext context) {
    return Row(children: [
      ColorTextButton(widget._text, widget.textSize),
      const SizedBox(width: 10),
      IconButton(
        color: Style.GREY,
        icon: const Icon(
          Icons.folder_open,
        ),
        iconSize: 40,
        onPressed: () {
          OpenFolder.openFolder(widget._folder);
        },
      )
    ]);
  }
}

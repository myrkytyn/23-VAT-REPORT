import 'package:flutter/material.dart';

class LeftColumn extends StatelessWidget {
  const LeftColumn({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: const [SizedBox(width: 100)]);
  }
}

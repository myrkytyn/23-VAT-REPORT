import 'package:flutter/material.dart';
import 'package:ui/use_case/check_date.dart';
import 'package:ui/use_case/open_folder.dart';
import 'package:ui/widgets/checkbox_text_list.dart';
import 'package:ui/widgets/color_switch_text_row.dart';
import 'package:ui/widgets/date_row.dart';
import 'package:ui/widgets/header.dart';
import 'package:ui/widgets/left_column.dart';
import 'package:ui/widgets/text.dart';
import 'package:ui/widgets/text_button_with_icon.dart';
import 'package:window_size/window_size.dart';
import 'dart:io';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
    setWindowTitle('Податковий помічник 23.');
    setWindowMaxSize(const Size(1200, 900));
    setWindowMinSize(const Size(1200, 900));
  }

  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MainPage(),
      title: 'Податковий помічник 23.',
      debugShowCheckedModeBanner: false,
    );
  }
}

class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => MainPageState();
}

class MainPageState extends State<MainPage> {
  final fromDateController = TextEditingController();
  final toDateController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          const Header("Податкові накладні", 30),
          const SizedBox(height: 50),
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const LeftColumn(),
              Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const ColoredText("Ресторани", 40, FontWeight.w600),
                  const SizedBox(height: 40),
                  const CheckBoxTextList(25, FontWeight.w400),
                  const SizedBox(height: 20),
                  DateRow("дд.мм.рррр", "Від", "До", fromDateController,
                      toDateController),
                  const SizedBox(height: 20),
                  TextButtonWithIcon("Скачати звіти", 20, () {
                    OpenFolder.openFolder("iiko_reports");
                  }, () {
                    CheckDate.checkRegEx(
                        fromDateController.text, toDateController.text);
                  }),
                  const SizedBox(width: 700)
                ],
              ),
              Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const ColoredText("Статус", 30, FontWeight.w600),
                  const SizedBox(
                    height: 200,
                    width: 340,
                    child: Expanded(
                      child: Text(
                        'a long text',
                        overflow: TextOverflow.clip,
                      ),
                    ),
                  ),
                  const SizedBox(height: 100),
                  TextButtonWithIcon("Створити звіти Excel", 20, () {
                    OpenFolder.openFolder("excel_files_generated");
                  }, () {}),
                  ColorSwitchTextRow(true, "База даних"),
                  const SizedBox(height: 45),
                  TextButtonWithIcon("Створити звіти XML", 20, () {
                    OpenFolder.openFolder("xml_files_generated");
                  }, () {})
                ],
              )
            ],
          )
        ],
      ),
    );
  }
}

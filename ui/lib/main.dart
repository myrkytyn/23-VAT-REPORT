import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:ui/widgets/color_switch_text_row.dart';
import 'package:ui/widgets/color_text_button.dart';
import 'package:ui/widgets/header.dart';
import 'package:ui/widgets/text_button_with_icon.dart';
import 'package:window_size/window_size.dart';
import 'dart:io';
import 'package:url_launcher/url_launcher.dart';

extension ColorExtension on String {
  toColor() {
    var hexString = this;
    final buffer = StringBuffer();
    if (hexString.length == 6 || hexString.length == 7) buffer.write('ff');
    buffer.write(hexString.replaceFirst('#', ''));
    return Color(int.parse(buffer.toString(), radix: 16));
  }
}

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
    setWindowTitle('Податковий помічий 23.');
    setWindowMaxSize(const Size(1200, 900));
    setWindowMinSize(const Size(1200, 900));
  }

  runApp(App());
}

getRestaurnats() {
  File file = File('/home/maksym/Maks/Projects/23-VAT-REPORT/config.json');
  String contents = file.readAsStringSync();
  var restaurants = [];
  var config = jsonDecode(contents) as Map;
  var entities = config['legal_entities'] as Map;

  for (var entity in entities.keys) {
    if (config["legal_entities"][entity]["name"] is List) {
      config["legal_entities"][entity]["name"]
          .forEach((element) => restaurants.add(element));
    } else {
      restaurants.add(config["legal_entities"][entity]["name"]);
    }
  }
  return restaurants;
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MainPage(),
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
  String dir = Directory.current.path;
  bool isChecked = false;

  Color getColor(Set<MaterialState> states) {
    const Set<MaterialState> interactiveStates = <MaterialState>{
      MaterialState.pressed,
      MaterialState.hovered,
      MaterialState.focused,
    };
    if (states.any(interactiveStates.contains)) {
      return Colors.blue;
    }
    return Colors.red;
  }

  Widget restaurant_list() {
    List<Widget> list = [];
    var restaurants = getRestaurnats();
    restaurants.forEach((item) {
      list.add(Row(children: [
        Checkbox(
          checkColor: Colors.white,
          fillColor: MaterialStateProperty.resolveWith(getColor),
          value: isChecked,
          onChanged: (bool? value) {
            setState(() {
              isChecked = value!;
            });
          },
        ),
        Text(item, style: TextStyle(fontSize: 25, color: '#595959'.toColor()))
      ]));
      list.add(const SizedBox(height: 15));
    });

    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: list,
    );
  }

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
              Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: const [SizedBox(width: 100)]),
              Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Ресторани:',
                      style: TextStyle(
                          fontWeight: FontWeight.w600,
                          fontSize: 40,
                          color: '#595959'.toColor())),
                  const SizedBox(height: 40),
                  restaurant_list(),
                  const SizedBox(height: 60),
                  Row(children: [
                    const SizedBox(width: 10),
                    Text('Від:',
                        style: TextStyle(
                            fontWeight: FontWeight.w500,
                            fontSize: 20,
                            color: '#595959'.toColor())),
                    const SizedBox(width: 250),
                    Text('До:',
                        style: TextStyle(
                            fontWeight: FontWeight.w500,
                            fontSize: 20,
                            color: '#595959'.toColor())),
                  ]),
                  const SizedBox(height: 5),
                  Row(children: [
                    SizedBox(
                      width: 200,
                      child: TextField(
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(15)),
                          hintText: 'дд.мм.рррр',
                        ),
                      ),
                    ),
                    const SizedBox(width: 35),
                    Text('-',
                        style: TextStyle(
                            fontWeight: FontWeight.w500,
                            fontSize: 30,
                            color: '#595959'.toColor())),
                    const SizedBox(width: 35),
                    SizedBox(
                      width: 200,
                      child: TextField(
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(15)),
                          hintText: 'дд.мм.рррр',
                        ),
                      ),
                    ),
                  ]),
                  const SizedBox(height: 20),
                  const TextButtonWithIcon("Скачати звіти", 20),
                  const SizedBox(width: 700)
                ],
              ),
              Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Статус:",
                      style: TextStyle(
                          fontWeight: FontWeight.w600,
                          fontSize: 30,
                          color: '#595959'.toColor())),
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
                  const TextButtonWithIcon("Створити звіти Excel", 20),
                  const SizedBox(height: 45),
                  const TextButtonWithIcon("Створити звіти XML", 20),
                  ColorSwitchTextRow(true, "База даних")
                ],
              )
            ],
          )
        ],
      ),
    );
  }
}

//TODO
//final Uri url =
//Uri.parse('file:$dir/excel_files_generated/');
//launchUrl(url);

//Create openfolder func for foldericons


//TextButton(
//                    style: TextButton.styleFrom(
//                        backgroundColor: '#E41E12'.toColor(),
//                        padding: const EdgeInsets.fromLTRB(14, 25, 14, 25),
//                        shape: RoundedRectangleBorder(
//                            borderRadius: BorderRadius.circular(
//                          15,
//                        ))),
//                    onPressed: () {},
//                    child: Text('Податкові накладні',
//                        style: TextStyle(
//                            fontSize: 30, color: '#EFEFEF'.toColor())),
//                  ),
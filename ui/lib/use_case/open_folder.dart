import 'dart:io';
import 'package:url_launcher/url_launcher.dart';

class OpenFolder {
  static void openFolder(String folder) {
    String dir = Directory.current.path;
    final Uri url = Uri.parse('file:$dir/$folder/');
    launchUrl(url);
  }
}

import 'dart:convert';
import 'dart:io';

class GetRestaurnats {
  static getRestaurnatsList() {
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
}

import 'package:intl/intl.dart';
import 'package:ui/widgets/checkbox_text_list.dart';

class CheckData {
  static checkRegEx(fromDate, toDate) {
    bool dateValid = false;
    RegExp regExp = RegExp(
        r"(0[1-9]|[12][0-9]|3[01])\.(0[13578]|1[02])\.(2022|2023|2024|2025)|(0[1-9]|[12][0-9]|30)\.(0[469]|11)\.(2022|2023|2024|2025)|(0[1-9]|[12][0-9])\.02\.(2022|2023|2024|2025)");
    if (regExp.hasMatch(fromDate) && regExp.hasMatch(toDate)) {
      dateValid = true;
    }
    return dateValid;
  }

  static checkDateExisted(fromDate, toDate) {
    bool dateExists = false;
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    var fromDateDate = DateFormat('dd.MM.yyyy').parse(fromDate);
    var toDateDate = DateFormat('dd.MM.yyyy').parse(toDate);
    final fromDateSplitted =
        DateTime(fromDateDate.year, fromDateDate.month, fromDateDate.day);
    final toDateSplitted =
        DateTime(toDateDate.year, toDateDate.month, toDateDate.day);
    if (fromDateSplitted.isBefore(today) ||
        fromDateSplitted.isAtSameMomentAs(today) &&
            toDateSplitted.isBefore(today) ||
        toDateSplitted.isAtSameMomentAs(today)) {
      if (fromDateSplitted.isBefore(toDateSplitted) ||
          fromDateSplitted.isAtSameMomentAs(toDateSplitted)) {
        dateExists = true;
      }
    }
    return dateExists;
  }

  static checkRestaurantsCheckbox() {
    bool isChecked = false;
    CheckBoxTextList.restaurantsMap.forEach((key, value) {
      if (value == true) {
        isChecked = true;
      }
    });
    return isChecked;
  }

  static getCheckBoxesValue() {
    var restaurantList = [];
    CheckBoxTextList.restaurantsMap.forEach((key, value) {
      if (value == true) {
        restaurantList.add(key);
      }
    });
    return restaurantList;
  }
}

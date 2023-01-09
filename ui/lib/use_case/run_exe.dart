import 'dart:io';

class RunExecutable {
  static runProgram() {
    Process.run('cmd', ["start iiko_reports"]);
  }
}
